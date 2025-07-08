from django.db import models  # Import model dari Django

# Model untuk produk utama
class Product(models.Model):
    name = models.CharField(max_length=100)  # Nama produk
    price = models.DecimalField(max_digits=12, decimal_places=0)  # Harga produk
    image = models.ImageField(upload_to='produk/', blank=True, null=True)  # Gambar produk (opsional)
    description = models.TextField(blank=True)  # Deskripsi produk (opsional)
    created_at = models.DateTimeField(auto_now_add=True)  # Tanggal dibuat otomatis

    def __str__(self):
        return self.name  # Tampilkan nama produk di admin

# Model untuk daftar produk custom
class ModelProduk(models.Model):
    nama = models.CharField(max_length=100)  # Nama produk
    harga = models.DecimalField(max_digits=12, decimal_places=0)  # Harga produk
    gambar = models.ImageField(upload_to='produk/', blank=True, null=True)  # Gambar produk (opsional)
    deskripsi = models.TextField(blank=True)  # Deskripsi produk (opsional)
    dibuat_pada = models.DateTimeField(auto_now_add=True)  # Tanggal dibuat otomatis

    def __str__(self):
        return self.nama  # Tampilkan nama produk di admin

# Model untuk gambar produk tambahan
class ProductImage(models.Model):
    file = models.ImageField(upload_to='produk/')  # File gambar
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Tanggal upload otomatis

# Model untuk testimoni pelanggan
class Testimoni(models.Model):
    nama = models.CharField(max_length=100)  # Nama pemberi testimoni
    pesan = models.TextField()  # Isi testimoni
    tanggal = models.DateTimeField(auto_now_add=True)  # Tanggal testimoni dibuat
