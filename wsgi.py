"""
Konfigurasi WSGI untuk proyek alfinStore.

File ini mengekspor variabel 'application' yang digunakan oleh server WSGI.
Untuk dokumentasi lebih lanjut, lihat:
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os  # Mengimpor modul os untuk mengatur variabel lingkungan

from django.core.wsgi import get_wsgi_application  # Mengimpor fungsi untuk mendapatkan aplikasi WSGI dari Django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alfinStore.settings')  # Mengatur variabel lingkungan agar Django tahu file settings yang digunakan

application = get_wsgi_application()  # Membuat instance aplikasi WSGI yang akan digunakan oleh server WSGI
