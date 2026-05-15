from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('account/', include('accounts.urls')),
]

if getattr(settings, 'ENTRA_ENABLED', False):
    urlpatterns.insert(1, path('saml2/', include('djangosaml2.urls')))

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
