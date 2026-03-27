from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, reverse

from openpyxl import load_workbook

from .models import Book, Category, Review, Favorite, Exhibit, Event, News


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon']
    search_fields = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'category',
        'isbn',
        'barcode',
        'quantity',
        'language',
        'available',
        'views_count',
        'created_at',
    ]
    list_filter = ['category', 'language', 'available', 'published_year']
    search_fields = ['title', 'author', 'isbn', 'barcode']
    list_editable = ['available', 'quantity']
    readonly_fields = ['views_count', 'download_count']
    change_list_template = 'admin/books/book/change_list.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'import-xlsx/',
                self.admin_site.admin_view(self.import_xlsx_view),
                name='books_book_import_xlsx',
            ),
        ]
        return custom_urls + urls

    @staticmethod
    def _normalize_header(value):
        if value is None:
            return ''
        return str(value).strip().lower().replace(' ', '').replace('_', '')

    @staticmethod
    def _to_text(value):
        if value is None:
            return ''
        text = str(value).strip()
        if text.endswith('.0') and text.replace('.', '', 1).isdigit():
            return text[:-2]
        return text

    @staticmethod
    def _to_int(value, default=1):
        if value is None or str(value).strip() == '':
            return default
        try:
            parsed = int(float(str(value).strip()))
            return max(parsed, 0)
        except (TypeError, ValueError):
            return default

    def import_xlsx_view(self, request):
        if request.method == 'POST':
            file_obj = request.FILES.get('xlsx_file')
            if not file_obj:
                self.message_user(request, 'Please select an .xlsx file.', level=messages.ERROR)
                return HttpResponseRedirect(request.path)

            if not file_obj.name.lower().endswith('.xlsx'):
                self.message_user(request, 'Only .xlsx files are supported.', level=messages.ERROR)
                return HttpResponseRedirect(request.path)

            try:
                workbook = load_workbook(file_obj, data_only=True)
                sheet = workbook.active
            except Exception as exc:
                self.message_user(request, f'Failed to read file: {exc}', level=messages.ERROR)
                return HttpResponseRedirect(request.path)

            rows = list(sheet.iter_rows(values_only=True))
            if not rows:
                self.message_user(request, 'The file is empty.', level=messages.ERROR)
                return HttpResponseRedirect(request.path)

            headers = [self._normalize_header(h) for h in rows[0]]
            index_by_name = {name: i for i, name in enumerate(headers) if name}

            title_idx = index_by_name.get('title')
            author_idx = index_by_name.get('auth')
            if author_idx is None:
                author_idx = index_by_name.get('author')
            isbn_idx = index_by_name.get('isbn')
            barcode_idx = index_by_name.get('barcode')
            quantity_idx = index_by_name.get('quantiy')
            if quantity_idx is None:
                quantity_idx = index_by_name.get('quantity')

            if title_idx is None or author_idx is None:
                self.message_user(
                    request,
                    'Required columns missing. Expected at least: title, auth.',
                    level=messages.ERROR,
                )
                return HttpResponseRedirect(request.path)

            created_count = 0
            updated_count = 0
            skipped_count = 0

            for row in rows[1:]:
                title = self._to_text(row[title_idx] if title_idx < len(row) else None)
                author = self._to_text(row[author_idx] if author_idx < len(row) else None)
                isbn = self._to_text(row[isbn_idx] if isbn_idx is not None and isbn_idx < len(row) else None)
                barcode = self._to_text(
                    row[barcode_idx] if barcode_idx is not None and barcode_idx < len(row) else None
                )
                quantity = self._to_int(
                    row[quantity_idx] if quantity_idx is not None and quantity_idx < len(row) else None,
                    default=1,
                )

                if not title or not author:
                    skipped_count += 1
                    continue

                lookup = None
                if isbn:
                    lookup = Book.objects.filter(isbn=isbn).first()
                elif barcode:
                    lookup = Book.objects.filter(barcode=barcode).first()
                if lookup is None:
                    lookup = Book.objects.filter(title=title, author=author).first()

                payload = {
                    'title': title,
                    'author': author,
                    'isbn': isbn,
                    'barcode': barcode,
                    'quantity': quantity,
                    'available': quantity > 0,
                }

                if lookup:
                    for key, value in payload.items():
                        setattr(lookup, key, value)
                    lookup.save()
                    updated_count += 1
                else:
                    Book.objects.create(**payload)
                    created_count += 1

            self.message_user(
                request,
                f'Import finished: created={created_count}, updated={updated_count}, skipped={skipped_count}.',
                level=messages.SUCCESS,
            )
            return HttpResponseRedirect(reverse('admin:books_book_changelist'))

        context = dict(
            self.admin_site.each_context(request),
            opts=self.model._meta,
            title='Import books from XLSX',
        )
        return render(request, 'admin/books/book/import_xlsx.html', context)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'rating', 'created_at']
    list_filter = ['rating']


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'created_at']


@admin.register(Exhibit)
class ExhibitAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'date_start', 'date_end', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['title']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'date', 'time_start', 'time_end', 'location', 'is_active']
    list_editable = ['is_active']
    list_filter = ['is_active', 'date']
    search_fields = ['title', 'category', 'location']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'is_active']
    list_editable = ['is_active']
    list_filter = ['is_active', 'date']
    search_fields = ['title']
