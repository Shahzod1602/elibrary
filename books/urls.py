from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('katalog/', views.catalog, name='catalog'),
    path('kitob/<int:pk>/', views.book_detail, name='book_detail'),
    path('kitob/<int:pk>/sharh/', views.add_review, name='add_review'),
    path('kitob/<int:pk>/sevimli/', views.toggle_favorite, name='toggle_favorite'),
    path('kitob/<int:pk>/yuklab-olish/', views.download_book, name='download_book'),
    path('profil/', views.profile, name='profile'),
    path('biz-haqimizda/', views.about, name='about'),
]
