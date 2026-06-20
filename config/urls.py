from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Microsoft Entra OIDC SSO (AXIO uslubidagi /api/sso/callback naqshi)
    path('api/sso/login', account_views.sso_login, name='sso_login'),
    path('api/sso/callback', account_views.sso_callback, name='sso_callback'),
    path('', include('books.urls')),
    path('account/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
