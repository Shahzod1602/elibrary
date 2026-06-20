"""Microsoft Entra ID — OIDC (OpenID Connect) SSO.

Authorization Code flow, AXIO SSO uslubida:
  /api/sso/login    -> Microsoft Entra'ga yo'naltiradi
  /api/sso/callback -> token oladi, Django User yaratadi/yangilaydi, login qiladi

ENTRA_ENABLED False bo'lsa (env to'ldirilmagan) — oddiy username/parol rejimi.
"""

from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import redirect

from .models import StudentProfile

oauth = OAuth()

if settings.ENTRA_ENABLED:
    oauth.register(
        name='entra',
        server_metadata_url=settings.ENTRA_METADATA_URL,
        client_id=settings.ENTRA_CLIENT_ID,
        client_secret=settings.ENTRA_CLIENT_SECRET,
        client_kwargs={'scope': settings.ENTRA_SCOPE},
    )


def sso_login(request):
    """Microsoft Entra login sahifasiga yo'naltirish."""
    if not settings.ENTRA_ENABLED:
        return redirect('login')
    # @login_required dan kelgan ?next= ni saqlab qo'yamiz
    request.session['sso_next'] = request.GET.get('next', '')
    return oauth.entra.authorize_redirect(request, settings.ENTRA_REDIRECT_URI)


def sso_callback(request):
    """Entra'dan qaytgan code'ni token'ga almashtirib, foydalanuvchini kiritadi."""
    if not settings.ENTRA_ENABLED:
        return redirect('login')

    try:
        token = oauth.entra.authorize_access_token(request)
    except Exception as exc:  # noqa: BLE001 — har qanday OAuth/tarmoq xatosini ushlaymiz
        messages.error(request, f'Microsoft orqali kirishda xatolik: {exc}')
        return redirect('login')

    claims = token.get('userinfo') or {}
    email = (claims.get('email') or claims.get('preferred_username') or '').strip().lower()
    if not email:
        messages.error(request, 'Microsoft hisobidan email olinmadi.')
        return redirect('login')

    first_name = (claims.get('given_name') or '')[:100]
    last_name = (claims.get('family_name') or '')[:100]

    user, created = User.objects.get_or_create(
        username=email,
        defaults={'email': email, 'first_name': first_name, 'last_name': last_name},
    )

    # Mavjud foydalanuvchining ma'lumotlarini yangilab turamiz
    if not created:
        updates = {}
        if user.email != email:
            updates['email'] = email
        if first_name and user.first_name != first_name:
            updates['first_name'] = first_name
        if last_name and user.last_name != last_name:
            updates['last_name'] = last_name
        if updates:
            for field, value in updates.items():
                setattr(user, field, value)
            user.save(update_fields=list(updates))

    # Profil bo'lmasa — ism/familiya bilan yaratamiz (yo'nalish/guruh/ID adminda to'ldiriladi).
    # Mavjud profilni TEGINMAYMIZ (admin kiritgan ma'lumotni saqlash uchun).
    StudentProfile.objects.get_or_create(
        user=user,
        defaults={'first_name': first_name, 'last_name': last_name},
    )

    auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')

    next_url = request.session.pop('sso_next', '') or 'home'
    return redirect(next_url)
