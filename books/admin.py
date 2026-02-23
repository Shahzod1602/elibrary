from django.contrib import admin
from .models import Book, Category, Review, Favorite


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon']
    search_fields = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'language', 'available', 'views_count', 'created_at']
    list_filter = ['category', 'language', 'available', 'published_year']
    search_fields = ['title', 'author', 'isbn']
    list_editable = ['available']
    readonly_fields = ['views_count', 'download_count']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'rating', 'created_at']
    list_filter = ['rating']


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'created_at']
