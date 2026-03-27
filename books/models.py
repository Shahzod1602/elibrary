from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category name")
    icon = models.CharField(max_length=50, default="bi-book", verbose_name="Bootstrap icon")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Book title")
    author = models.CharField(max_length=200, verbose_name="Author")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name="Category", related_name="books"
    )
    description = models.TextField(blank=True, verbose_name="Description")
    cover = models.ImageField(upload_to='covers/', blank=True, verbose_name="Cover image")
    pdf_file = models.FileField(upload_to='books/', blank=True, verbose_name="PDF file")
    pages = models.PositiveIntegerField(default=0, verbose_name="Page count")
    language = models.CharField(max_length=50, default="Uzbek", verbose_name="Language")
    isbn = models.CharField(max_length=20, blank=True, verbose_name="ISBN")
    publisher = models.CharField(max_length=200, blank=True, verbose_name="Publisher")
    published_year = models.PositiveIntegerField(null=True, blank=True, verbose_name="Publication year")
    available = models.BooleanField(default=True, verbose_name="Available")
    views_count = models.PositiveIntegerField(default=0, verbose_name="View count")
    download_count = models.PositiveIntegerField(default=0, verbose_name="Downloads")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.author}"

    @property
    def avg_rating(self):
        avg = self.reviews.aggregate(avg=Avg('rating'))['avg']
        return round(avg, 1) if avg else 0

    @property
    def review_count(self):
        return self.reviews.count()


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)], verbose_name="Rating"
    )
    comment = models.TextField(verbose_name="Comment")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        unique_together = ['book', 'user']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.rating})"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='favorited_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"
        unique_together = ['user', 'book']

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"


class Exhibit(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    subtitle = models.CharField(max_length=300, blank=True, verbose_name="Subtitle")
    image = models.ImageField(upload_to='exhibits/', blank=True, verbose_name="Image")
    date_start = models.DateField(null=True, blank=True, verbose_name="Start date")
    date_end = models.DateField(null=True, blank=True, verbose_name="End date")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    order = models.PositiveSmallIntegerField(default=0, verbose_name="Order")

    class Meta:
        verbose_name = "Exhibit"
        verbose_name_plural = "Exhibits"
        ordering = ['order', '-date_end']

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    category = models.CharField(max_length=100, blank=True, verbose_name="Category")
    date = models.DateField(verbose_name="Date")
    time_start = models.TimeField(null=True, blank=True, verbose_name="Start time")
    time_end = models.TimeField(null=True, blank=True, verbose_name="End time")
    location = models.CharField(max_length=200, blank=True, verbose_name="Location")
    is_active = models.BooleanField(default=True, verbose_name="Active")

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['date']

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(upload_to='news/', blank=True, verbose_name="Image")
    date = models.DateField(verbose_name="Date")
    is_active = models.BooleanField(default=True, verbose_name="Active")

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ['-date']

    def __str__(self):
        return self.title
