# Microsoft Entra ID — OIDC SSO bilan integratsiya

Loyiha `authlib` orqali Microsoft Entra ID bilan **OpenID Connect (OIDC) /
OAuth2 Authorization Code** oqimida ulangan — xuddi **AXIO SSO** kabi
(`/api/sso/callback`, ID token). Bu confidential web app — **client secret**
ishlatiladi.

## 1) App registration yaratish

1. https://entra.microsoft.com → **App registrations** → **New registration**
2. Nomi: `AUT E-Library`
3. **Supported account types**: odatda *Accounts in this organizational directory only* (single tenant)
4. **Redirect URI**: platforma **Web**, qiymat:
   - Production: `https://elibrary.autplatform.uz/api/sso/callback`
   - Lokal dev: `http://localhost:8000/api/sso/callback`
5. **Register** bosing.

> Keyin xohlagancha **Authentication** bo'limidan yana Redirect URI qo'shsa
> bo'ladi (masalan, lokal va production'ni bir vaqtda saqlash uchun).

## 2) Authentication sozlamalari

**Authentication** bo'limida (screenshotdagidek):

- **Platform configurations → Web → Redirect URIs**: yuqoridagi callback URL.
- **Settings** tab → **Implicit grant and hybrid flows**:
  - ☑ **ID tokens (used for implicit and hybrid flows)**
  - ☐ Access tokens — kerak emas (kod o'rtada token oladi)
- **Allow public client flows**: **Disabled** (confidential app).

## 3) Client secret yaratish

**Certificates & secrets** → **Client secrets** → **New client secret**:

- Description: `elibrary`
- Expires: tashkilot siyosatiga ko'ra (masalan, 24 oy)
- **Value**'ni darhol nusxalang — bu `ENTRA_CLIENT_SECRET` bo'ladi (keyin ko'rinmaydi!).

## 4) Token configuration (claim'lar)

Standart `openid email profile` scope'lari quyidagilarni beradi:

| Claim | Manba | Django maydoni |
|---|---|---|
| `email` / `preferred_username` | user.mail / UPN | `username` + `email` |
| `given_name` | user.givenname | `first_name` |
| `family_name` | user.surname | `last_name` |

Agar `email` claim'i kelmasa, **Token configuration → Add optional claim →
ID → email** orqali qo'shish mumkin (kod baribir `preferred_username`'ga
fallback qiladi).

## 5) Foydalanuvchilarni biriktirish

**Enterprise applications → AUT E-Library → Users and groups → Add user/group**
orqali kerakli xodim/talaba yoki guruhni qo'shing.
(App roles'da Microsoft avtomatik `User` va `msiam_access` rollarini yaratadi.)

## 6) Loyihadagi `.env`ni to'ldirish

```env
SSO_BASE_URL=https://elibrary.autplatform.uz
ENTRA_TENANT_ID=<Directory (tenant) ID>
ENTRA_CLIENT_ID=<Application (client) ID>
ENTRA_CLIENT_SECRET=<client secret Value>
# ixtiyoriy (default: {SSO_BASE_URL}/api/sso/callback):
# ENTRA_REDIRECT_URI=https://elibrary.autplatform.uz/api/sso/callback
```

- `ENTRA_TENANT_ID`, `ENTRA_CLIENT_ID` — App registration **Overview** sahifasida.
- `ENTRA_CLIENT_SECRET` — 3-qadamdagi **Value**.
- Lokal dev uchun `SSO_BASE_URL=http://localhost:8000`.

Uchala qiymat to'ldirilsa `ENTRA_ENABLED = True` bo'ladi va login sahifasida
**Sign in with Microsoft** tugmasi paydo bo'ladi. Bo'sh bo'lsa — oddiy
username/parol rejimi (`ENTRA_ENABLED = False`).

## 7) Ishga tushirish

```bash
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

`/account/login/` → **Sign in with Microsoft** → Microsoft login →
muvaffaqiyatdan keyin Django'da `User` avtomatik yaratiladi/yangilanadi va
tizimga kiritiladi (`given_name → first_name`, `family_name → last_name`,
`email`/`preferred_username → username`).

## SSO endpoint'lari

- **Login**:    `https://elibrary.autplatform.uz/api/sso/login`
- **Callback (Redirect URI)**: `https://elibrary.autplatform.uz/api/sso/callback`
- **Logout**:   `https://elibrary.autplatform.uz/account/logout/` (Django sessiyasini tozalaydi)

## Tekshirish

```bash
python manage.py check
python manage.py runserver
# /account/login/ sahifasida Microsoft tugmasini bosib oqimni sinab ko'ring
```

## Eslatma

- **Client secret muddati**: tugashidan oldin yangisini yarating va `.env`ni
  yangilang (eski va yangi secret bir muddat birga turishi mumkin).
- **HTTPS**: production'da `SESSION_COOKIE_SECURE`/`CSRF_COOKIE_SECURE`
  avtomatik yoqiladi (`DEBUG=False` bo'lganda). Redirect URI ham `https://`
  bo'lishi shart.
- **xmlsec1 kerak emas**: OIDC SAML emas — Docker image'dan `xmlsec1` olib
  tashlandi.
- **Admin login**: superuser'lar baribir `/admin/login/` orqali parol bilan
  kira oladi (SSO'dan mustaqil).
