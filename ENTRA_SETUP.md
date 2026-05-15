# Microsoft Entra ID — SAML SSO bilan integratsiya

Loyiha `djangosaml2` orqali Microsoft Entra ID bilan **SAML 2.0 SSO** ulangan
(AXIO SSO uslubidagi sozlama). Client secret kerak emas — autentifikatsiya
sertifikat orqali amalga oshiriladi.

## Tizim talablari

Serverda `xmlsec1` binarisi bo'lishi shart:

```bash
# Ubuntu/Debian
sudo apt install xmlsec1 libxmlsec1-dev libxmlsec1-openssl

# macOS
brew install libxmlsec1 xmlsec1
```

## 1) Azure portalda Enterprise Application yaratish

1. https://entra.microsoft.com → **Enterprise applications** → **New application**
2. **Create your own application** bosing.
3. Nomi: `AUT E-Library`
4. **Integrate any other application you don't find in the gallery (Non-gallery)** ni tanlang → **Create**.

## 2) SAML Single Sign-On sozlash

App yaratilgach:

1. Chap menyudan **Single sign-on** → **SAML** ni tanlang.
2. **Basic SAML Configuration** bo'limini tahrirlang:
   - **Identifier (Entity ID)**: `https://elibrary.autplatform.uz/saml2/metadata/`
     - (Lokal dev uchun: `http://localhost:8000/saml2/metadata/`)
   - **Reply URL (ACS URL)**: `https://elibrary.autplatform.uz/saml2/acs/`
     - (Lokal dev uchun: `http://localhost:8000/saml2/acs/`)
   - **Sign on URL** (ixtiyoriy): `https://elibrary.autplatform.uz/account/login/`
   - **Logout URL**: `https://elibrary.autplatform.uz/saml2/ls/`
3. **Save** bosing.

## 3) User Attributes & Claims

Bo'limni tahrirlang va quyidagi claim'larni qo'shing (Microsoft Entra'da
odatda standart bo'lib turadi):

| Claim name | Source attribute |
|---|---|
| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name` | `user.userprincipalname` |
| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` | `user.mail` |
| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname` | `user.givenname` |
| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname` | `user.surname` |

Unique User Identifier (Name ID) = `user.userprincipalname` (format: Email).

## 4) Foydalanuvchilarni biriktirish

1. **Users and groups** → **Add user/group** → kerakli xodimlar yoki guruhni qo'shing.
2. **App roles** bo'limida (xohlasangiz) `User` va `msiam_access` rollarini ko'rasiz.

## 5) Metadata URL'ni nusxalash

SAML SSO sahifasida **App Federation Metadata Url** bor:

```
https://login.microsoftonline.com/<TENANT_ID>/federationmetadata/2007-06/federationmetadata.xml?appid=<APP_ID>
```

Bu URL'ni nusxalang.

## 6) Loyihadagi `.env`ni to'ldirish

```env
SAML_BASE_URL=https://elibrary.autplatform.uz
SAML_ENTRA_METADATA_URL=https://login.microsoftonline.com/<TENANT_ID>/federationmetadata/2007-06/federationmetadata.xml?appid=<APP_ID>
SAML_ENTRA_ENTITY_ID=https://sts.windows.net/<TENANT_ID>/
```

- `SAML_BASE_URL` — sizning domeningiz (lokal dev uchun `http://localhost:8000`).
- `SAML_ENTRA_METADATA_URL` — 5-qadamdan olingan URL.
- `SAML_ENTRA_ENTITY_ID` — Azure tomonida ko'rinadigan Microsoft Entra Identifier (odatda `https://sts.windows.net/<TENANT_ID>/`).

## 7) Loyihani ishga tushirish

```bash
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

`/account/login/` sahifasida **Sign in with Microsoft** tugmasi ko'rinadi.
Bosish → Microsoft login → muvaffaqiyatdan keyin Django'ga avtomatik
`User` yozuvi yaratiladi (claim mapping: `givenname → first_name`,
`surname → last_name`, `emailaddress → email`, `name → username`).

## SAML endpoint'lari

- **Metadata**: `https://elibrary.autplatform.uz/saml2/metadata/`
- **ACS (Reply URL)**: `https://elibrary.autplatform.uz/saml2/acs/`
- **Login**: `https://elibrary.autplatform.uz/saml2/login/`
- **Logout**: `https://elibrary.autplatform.uz/saml2/ls/`

## Tekshirish

```bash
python manage.py check          # konfiguratsiya xatosiz
curl -s http://localhost:8000/saml2/metadata/ | head -20   # SP metadata XML
python manage.py runserver
```

## Eslatma

- **Sertifikat**: SAML responselari Microsoft tomondan sertifikat bilan
  imzolanadi. Sertifikat metadata URL ichida avtomatik yangilanadi —
  qo'lda yuklab olish shart emas.
- **Lokal HTTPS**: Production'da `SAML_SESSION_COOKIE_SAMESITE='None'` ishlatish
  uchun HTTPS zarur (`SESSION_COOKIE_SECURE=True` avtomatik o'rnatiladi).
- **Mahalliy login**: SAML env-lar bo'sh bo'lsa, loyiha eski username/password
  rejimida ishlaydi (`ENTRA_ENABLED = False`).
