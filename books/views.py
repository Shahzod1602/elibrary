from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Avg, Count
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Book, Category, Review, Favorite
from .forms import ReviewForm


def home(request):
    new_books = Book.objects.filter(available=True)[:8]
    popular_books = Book.objects.filter(available=True).order_by('-views_count')[:8]
    categories = Category.objects.annotate(book_count=Count('books'))
    total_books = Book.objects.count()
    total_categories = Category.objects.count()
    total_authors = Book.objects.values('author').distinct().count()

    return render(request, 'books/home.html', {
        'new_books': new_books,
        'popular_books': popular_books,
        'categories': categories,
        'total_books': total_books,
        'total_categories': total_categories,
        'total_authors': total_authors,
        'physical_books': 603,
        'ebooks': 37,
    })


def catalog(request):
    books = Book.objects.filter(available=True)
    categories = Category.objects.annotate(book_count=Count('books'))

    # Qidiruv
    query = request.GET.get('q', '')
    if query:
        books = books.filter(
            Q(title__icontains=query) | Q(author__icontains=query) | Q(isbn__icontains=query)
        )

    # Kategoriya filter
    category_id = request.GET.get('category')
    if category_id:
        books = books.filter(category_id=category_id)

    # Til filter
    language = request.GET.get('language')
    if language:
        books = books.filter(language=language)

    # Yil filter
    year_from = request.GET.get('year_from')
    year_to = request.GET.get('year_to')
    if year_from:
        books = books.filter(published_year__gte=year_from)
    if year_to:
        books = books.filter(published_year__lte=year_to)

    # Saralash
    sort = request.GET.get('sort', '-created_at')
    sort_options = {
        'newest': '-created_at',
        'oldest': 'created_at',
        'title': 'title',
        'popular': '-views_count',
        'rating': '-avg_rating',
    }
    if sort == 'rating':
        books = books.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')
    elif sort in sort_options:
        books = books.order_by(sort_options[sort])

    # Tillar ro'yxati (filter uchun)
    languages = Book.objects.values_list('language', flat=True).distinct()

    # Sahifalash
    paginator = Paginator(books, 12)
    page = request.GET.get('page')
    books = paginator.get_page(page)

    return render(request, 'books/catalog.html', {
        'books': books,
        'categories': categories,
        'languages': languages,
        'query': query,
        'selected_category': category_id,
        'selected_language': language,
        'selected_sort': sort,
    })


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    # Ko'rishlar soni
    book.views_count += 1
    Book.objects.filter(pk=pk).update(views_count=book.views_count)

    reviews = book.reviews.select_related('user')
    related_books = Book.objects.filter(
        category=book.category, available=True
    ).exclude(pk=pk)[:4]

    is_favorite = False
    user_review = None
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, book=book).exists()
        user_review = Review.objects.filter(user=request.user, book=book).first()

    review_form = ReviewForm()

    return render(request, 'books/book_detail.html', {
        'book': book,
        'reviews': reviews,
        'related_books': related_books,
        'is_favorite': is_favorite,
        'user_review': user_review,
        'review_form': review_form,
    })


@login_required
def add_review(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if Review.objects.filter(user=request.user, book=book).exists():
        messages.warning(request, 'Siz allaqachon sharh qoldirgansiz.')
        return redirect('book_detail', pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            messages.success(request, 'Sharhingiz qo\'shildi!')
    return redirect('book_detail', pk=pk)


@login_required
def toggle_favorite(request, pk):
    book = get_object_or_404(Book, pk=pk)
    fav, created = Favorite.objects.get_or_create(user=request.user, book=book)
    if not created:
        fav.delete()
        status = 'removed'
    else:
        status = 'added'

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': status})
    return redirect('book_detail', pk=pk)


@login_required
def download_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.pdf_file:
        Book.objects.filter(pk=pk).update(download_count=book.download_count + 1)
        return redirect(book.pdf_file.url)
    messages.error(request, 'PDF fayl mavjud emas.')
    return redirect('book_detail', pk=pk)


@login_required
def profile(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('book', 'book__category')
    user_reviews = Review.objects.filter(user=request.user).select_related('book')
    return render(request, 'accounts/profile.html', {
        'favorites': favorites,
        'user_reviews': user_reviews,
    })


def about(request):
    total_categories = Category.objects.count()
    total_authors = Book.objects.values('author').distinct().count()
    return render(request, 'books/about.html', {
        'physical_books': 603,
        'ebooks': 37,
        'total_categories': total_categories,
        'total_authors': total_authors,
    })
