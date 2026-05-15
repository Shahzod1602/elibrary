from django.conf import settings


def entra_status(request):
    return {
        'entra_enabled': getattr(settings, 'ENTRA_ENABLED', False),
    }
