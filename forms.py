from django import forms  # Import modul forms dari Django
from .models import ProductImage, Testimoni  # Import model terkait

# Form untuk upload gambar produk
class ProductImageForm(forms.ModelForm):
    # Field opsional untuk nama file custom
    nama_file = forms.CharField(max_length=255, required=False, label='Nama File (Opsional)')

    class Meta:
        # Model yang digunakan oleh form
        model = ProductImage
        # Field yang digunakan di form
        fields = ['file']

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Simpan nama file custom jika diisi
        nama_file = self.cleaned_data.get('nama_file')
        if nama_file:
            instance.file.name = f'produk/{nama_file}'
        if commit:
            instance.save()
        return instance

# Form untuk testimoni
class TestimoniForm(forms.ModelForm):
    class Meta:
        # Model yang digunakan oleh form
        model = Testimoni
        # Field yang digunakan di form
        fields = ['nama', 'pesan']