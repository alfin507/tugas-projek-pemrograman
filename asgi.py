"""
Konfigurasi ASGI untuk proyek alfinStore

File ini mengekspor variabel 'application' yang digunakan oleh server ASGI.
Untuk dokumentasi lebih lanjut, lihat:
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os  # Mengimpor modul os untuk mengatur variabel lingkungan

from django.core.asgi import get_asgi_application  # Mengimpor fungsi untuk mendapatkan aplikasi ASGI dari Django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alfinStore.settings')  # Mengatur variabel lingkungan agar Django tahu file settings yang digunakan

application = get_asgi_application()  # Membuat instance aplikasi ASGI yang akan digunakan oleh server ASGI
