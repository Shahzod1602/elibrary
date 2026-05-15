# Microsoft Entra ID (Azure AD) — Enterprise Application bilan integratsiya

Bu loyiha `django-auth-adfs` orqali Microsoft Entra ID bilan SSO ulangan. Quyidagi qadamlar bo'yicha Azure tomonidagi sozlashni bajaring.

## 1) Azure portalda Enterprise Application yaratish

1. https://entra.microsoft.com → **Microsoft Entra ID** → **App registrations** → **New registration**
2. Maydonlarni to'ldiring:
   - **Name**: `AUT E-Library`
   - **Supported account types**: *Accounts in this organizational directory only* (single tenant)
   - **Redirect URI** (Platform = **Web**):
     - Production: `https://elibrary.autplatform.uz/oauth2/callback`
     - Local dev: `http://localhost:8000/oauth2/callback`
3. **Register** bosing.

## 2) Client Secret yaratish

1. Yangi yaratilgan app ichida → **Certificates & secrets** → **New client secret**
2. Description: `autlibrary-prod`, Expires: `24 months`
3. **Value** ustunidagi qiymatni nusxalang — bu **CLIENT_SECRET**. (Bir marta ko'rinadi!)

## 3) API permissions

1. **API permissions** → **Add a permission** → **Microsoft Graph** → **Delegated permissions**
2. Quyidagilarni qo'shing:
   - `openid`
   - `profile`
   - `email`
   - `User.Read`
3. **Grant admin consent for ...** tugmasini bosing.

## 4) (Ixtiyoriy) Token claims — guruhlar/rollar

Agar rol/guruhlar bilan ishlash kerak bo'lsa:
- **Token configuration** → **Add groups claim** → *Security groups* (yoki *App roles*)
- Yoki **App roles** → kerakli rollarni yarating va Enterprise Application → **Users and groups** orqali tayinlang.

## 5) Loyihadagi `.env` faylini to'ldirish

`Overview` sahifasidan quyidagilarni nusxalab `.env` ga yozing:

```env
ENTRA_TENANT_ID=<Directory (tenant) ID>
ENTRA_CLIENT_ID=<Application (client) ID>
ENTRA_CLIENT_SECRET=<2-qadamda olingan secret value>
```

## 6) Loyihani ishga tushirish

```bash
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

`/account/login/` sahifasida **Sign in with Microsoft** tugmasi ko'rinadi.
Tugma bosilganda foydalanuvchi Microsoft login sahifasiga yo'naltiriladi va muvaffaqiyatli login'dan keyin Django'ga `User` yozuvi avtomatik yaratiladi (claim mapping: `given_name`, `family_name`, `upn → email/username`).

## Texnik tafsilotlar

- **Callback URL**: `/oauth2/callback`
- **Login URL**: `/oauth2/login`
- **Logout**: oddiy Django logout (`/account/logout/`); single-sign-out kerak bo'lsa, `django_auth_adfs.views.OAuth2LogoutView` qo'shing.
- **Username manbasi**: `upn` claim (odatda foydalanuvchining email-formatdagi UPN'i).
- **Yangi foydalanuvchi**: `CREATE_NEW_USERS = True` — Entra'da bo'lgan har bir kishi avtomatik Django foydalanuvchisiga aylanadi.
- **Mahalliy login**: Entra env-lar bo'sh bo'lsa, loyiha eski username/password rejimida ishlaydi (`ENTRA_ENABLED = False`).

## Tekshirish

```bash
python manage.py check        # konfiguratsiya xatosiz
python manage.py runserver    # → http://localhost:8000/account/login/
```
