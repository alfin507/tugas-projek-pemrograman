"""
Konfigurasi utama Django untuk proyek alfinStore.

File ini dihasilkan oleh 'django-admin startproject' menggunakan Django 5.2.3.
Berisi semua pengaturan inti yang dibutuhkan oleh proyek.

Untuk dokumentasi lebih lanjut, lihat:
https://docs.djangoproject.com/en/5.2/topics/settings/

Daftar lengkap pengaturan dan nilainya:
https://docs.djangoproject.com/en/5.2/ref/settings/
"""


# Mengimpor Path dari pathlib untuk memudahkan manipulasi path berbasis objek
from pathlib import Path
# Mengimpor modul os untuk operasi sistem
import os


# Membangun path dasar proyek, BASE_DIR menunjuk ke folder utama proyek
BASE_DIR = Path(__file__).resolve().parent.parent



# Pengaturan cepat untuk development, tidak cocok untuk production
# Lihat https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/


# PERINGATAN KEAMANAN: rahasiakan SECRET_KEY di production!
SECRET_KEY = 'django-insecure-p6kj4(3d%1+si8bh&bxp&$n5zhn(7lefzf37xv8_!am3o0pq$5'


# PERINGATAN KEAMANAN: jangan aktifkan debug di production!
DEBUG = True


# Daftar host/domain yang diizinkan mengakses aplikasi
ALLOWED_HOSTS = []



# Definisi aplikasi yang terdaftar di proyek ini

INSTALLED_APPS = [
    'django.contrib.admin',           # Aplikasi admin bawaan Django
    'django.contrib.auth',            # Sistem autentikasi
    'django.contrib.contenttypes',    # Mendukung tipe konten
    'django.contrib.sessions',        # Manajemen sesi
    'django.contrib.messages',        # Framework pesan
    'django.contrib.staticfiles',     # Manajemen file statis
    'django.contrib.humanize',        # Filter template humanize
    'app',                            # Aplikasi utama custom
]


# Daftar middleware yang digunakan oleh aplikasi
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',           # Middleware keamanan
    'django.contrib.sessions.middleware.SessionMiddleware',    # Middleware sesi
    'django.middleware.common.CommonMiddleware',               # Middleware umum
    'django.middleware.csrf.CsrfViewMiddleware',              # Perlindungan CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Autentikasi
    'django.contrib.messages.middleware.MessageMiddleware',    # Pesan
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Perlindungan clickjacking
]


# File utama untuk konfigurasi URL
ROOT_URLCONF = 'alfinStore.urls'


# Pengaturan template (HTML)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', # Backend template
        'DIRS': [BASE_DIR / 'template'],                              # Direktori custom template
        'APP_DIRS': True,                                            # Cari template di setiap app
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',         # Menyediakan request di template
                'django.contrib.auth.context_processors.auth',        # Menyediakan user di template
                'django.contrib.messages.context_processors.messages',# Menyediakan pesan di template
            ],
        },
    },
]


# Entry point untuk WSGI (jika menggunakan WSGI server)
WSGI_APPLICATION = 'alfinStore.wsgi.application'



# Pengaturan database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',   # Engine database (sqlite3)
        'NAME': BASE_DIR / 'db.sqlite3',          # Lokasi file database
    }
}



# Validasi password
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # Validasi kemiripan dengan atribut user
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',          # Validasi panjang minimal
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',         # Validasi password umum
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',        # Validasi password numerik
    },
]



# Pengaturan internasionalisasi
# https://docs.djangoproject.com/en/5.2/topics/i18n/


# Kode bahasa default
LANGUAGE_CODE = 'en-us'


# Zona waktu default
TIME_ZONE = 'UTC'


# Aktifkan i18n (internasionalisasi)
USE_I18N = True


# Aktifkan timezone-aware datetimes
USE_TZ = True




# File statis (CSS, JavaScript, gambar)
# https://docs.djangoproject.com/en/5.2/howto/static-files/


# URL prefix untuk file statis
STATIC_URL = 'static/'


# File media (diunggah user)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Tipe primary key default untuk model baru
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

