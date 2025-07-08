from django.apps import AppConfig  # Import AppConfig dari Django

# Konfigurasi aplikasi utama untuk Django
class AppConfig(AppConfig):
    # Tipe primary key default untuk model baru
    default_auto_field = 'django.db.models.BigAutoField'
    # Nama aplikasi yang didaftarkan
    name = 'app'
