from django.contrib import admin  # Import modul admin bawaan Django
from .models import Product       # Import model Product dari file models.py

# Registrasi model Product ke admin site dengan konfigurasi khusus
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Kolom yang akan ditampilkan di list admin
    list_display = ('name', 'price', 'description')
    # Kolom yang bisa dicari di admin
    search_fields = ('name',)
