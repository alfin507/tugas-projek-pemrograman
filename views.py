

# =============================
# Import library dan model/form
# =============================
# Import decorator untuk membatasi method HTTP POST saja
from django.views.decorators.http import require_POST
# Import forms untuk membuat form custom dan ModelForm
from django import forms
# Import fungsi-fungsi shortcut untuk view (render, redirect, get_object_or_404)
from django.shortcuts import render, redirect, get_object_or_404
# Import reverse untuk membalikkan URL dari nama
from django.urls import reverse
# Import paginator untuk membagi data menjadi beberapa halaman
from django.core.paginator import Paginator
# Import messages untuk menampilkan notifikasi flash
from django.contrib import messages
# Import model yang digunakan di aplikasi
from .models import Product, ModelProduk, ProductImage, Testimoni
# Import form yang digunakan di aplikasi
from .forms import ProductImageForm, TestimoniForm


# =============================
# View untuk menghapus gambar produk
# =============================
@require_POST  # Hanya menerima request POST
def delete_product_image(request, product_id):
    # Ambil objek produk berdasarkan id, jika tidak ada akan 404
    product = get_object_or_404(Product, id=product_id)
    # Jika produk punya gambar, hapus file gambar dari storage
    if product.image:
        product.image.delete(save=False)
        product.image = None  # Set field image ke None
        product.save()        # Simpan perubahan ke database
    # Redirect ke halaman galeri produk
    return redirect('galeri_produk')


# =============================
# View untuk menghapus model produk
# =============================
@require_POST  # Hanya menerima request POST
def delete_modelproduk(request, produk_id):
    # Ambil objek ModelProduk berdasarkan id
    produk = get_object_or_404(ModelProduk, id=produk_id)
    # Jika model produk punya gambar, hapus file gambar
    if produk.gambar:
        produk.gambar.delete(save=False)
    # Hapus objek produk dari database
    produk.delete()
    # Redirect ke halaman daftar barang
    return redirect('daftar_barang')


# =============================
# View untuk menampilkan daftar barang dengan paginasi
# =============================
def daftar_barang(request):
    # Ambil semua data ModelProduk, urutkan dari terbaru
    daftar_produk = ModelProduk.objects.all().order_by('-id')
    # Paginasi: 12 produk per halaman
    paginator = Paginator(daftar_produk, 12)
    # Ambil nomor halaman dari query string
    page_number = request.GET.get('page')
    # Ambil objek halaman sesuai nomor
    page_obj = paginator.get_page(page_number)
    # Render template dengan data page_obj
    return render(request, 'daftar_barang.html', {'page_obj': page_obj})


# =============================
# View untuk menampilkan detail produk
# =============================
def detail_produk(request, pk):
    # Ambil produk berdasarkan primary key (pk)
    produk = get_object_or_404(ModelProduk, pk=pk)
    # Render halaman detail produk
    return render(request, 'detail_produk.html', {'produk': produk})


# =============================
# Form dan View untuk Order Produk
# =============================


# Form order produk (bukan ModelForm)
class OrderForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())  # ID produk (hidden)
    nama = forms.CharField(max_length=100, label='Nama Pemesan') # Nama pemesan
    kontak = forms.CharField(max_length=100, label='Kontak (WA/HP)') # Kontak pemesan
    jumlah = forms.IntegerField(min_value=1, label='Jumlah', initial=1) # Jumlah beli
    catatan = forms.CharField(widget=forms.Textarea, required=False, label='Catatan') # Catatan opsional


# View untuk memproses order produk
def order_product(request, product_id):
    # Ambil produk berdasarkan id
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        # Jika form disubmit, validasi data
        form = OrderForm(request.POST)
        if form.is_valid():
            jumlah = form.cleaned_data['jumlah']
            total_belanja = jumlah * product.price
            # Tampilkan halaman sukses order dengan detail pesanan
            return render(request, 'order_sukses.html', {
                'product': product,
                'form': form,
                'total_belanja': total_belanja
            })
    else:
        # Jika GET, tampilkan form order dengan product_id
        form = OrderForm(initial={'product_id': product.id})
    # Render halaman order produk
    return render(request, 'order_produk.html', {'product': product, 'form': form})


# =============================
# Form dan View untuk Tambah Produk
# =============================
# Form tambah produk (ModelForm)
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']  # Field yang ditampilkan di form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Tambahkan class pada widget image agar konsisten dengan Bootstrap
        self.fields['image'].widget.attrs.update({'class': 'form-control'})


# View untuk menampilkan daftar produk (Product) dengan paginasi
def product_list_page(request):
    products = Product.objects.all().order_by('-id')  # Ambil semua produk terbaru
    paginator = Paginator(products, 12)               # 12 produk per halaman
    page_number = request.GET.get('page')             # Ambil nomor halaman dari query string
    page_obj = paginator.get_page(page_number)        # Ambil objek halaman
    return render(request, 'list_produk.html', {'page_obj': page_obj})


# View untuk menambah produk baru
def product_add_page(request):
    print(">>> MASUK KE VIEW product_add_page")  # Debug: menandakan view ini dipanggil
    if request.method == 'POST':
        # Jika form disubmit, validasi dan simpan produk
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list_page')
    else:
        # Jika GET, tampilkan form kosong
        form = ProductForm()
    # Render halaman tambah produk
    return render(request, 'tambah_produk.html', {'form': form})


# View untuk menampilkan galeri produk (hanya produk yang punya gambar)
def galeri_produk(request):
    products = Product.objects.exclude(image='').order_by('-created_at')  # Produk dengan gambar saja
    return render(request, 'galeri_produk.html', {'products': products})


# =============================
# Form dan View untuk Kontak
# =============================
# Form kontak sederhana
class KontakForm(forms.Form):
    nama = forms.CharField(max_length=100)         # Nama pengirim
    email = forms.EmailField()                     # Email pengirim
    pesan = forms.CharField(widget=forms.Textarea) # Pesan


# View untuk halaman kontak
def kontak(request):
    if request.method == 'POST':
        # Jika form disubmit, validasi dan proses pesan
        form = KontakForm(request.POST)
        if form.is_valid():
            # Simpan ke database atau kirim email (implementasi opsional)
            messages.success(request, "Pesan berhasil dikirim!")
            form = KontakForm()  # Reset form setelah sukses
    else:
        # Jika GET, tampilkan form kosong
        form = KontakForm()
    # Render halaman kontak
    return render(request, 'kontak.html', {'form': form})


# View untuk upload file gambar produk
def upload_file(request):
    if request.method == 'POST':
        # Jika form disubmit, validasi dan simpan gambar
        form = ProductImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        # Jika GET, tampilkan form kosong
        form = ProductImageForm()
    # Ambil semua gambar yang sudah diupload, urut terbaru
    images = ProductImage.objects.order_by('-uploaded_at')
    # Render halaman upload file
    return render(request, 'upload_file.html', {'form': form, 'images': images})


# View untuk halaman testimoni pengunjung
def testimoni_page(request):
    if request.method == 'POST':
        # Jika form disubmit, validasi dan simpan testimoni
        form = TestimoniForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        # Jika GET, tampilkan form kosong
        form = TestimoniForm()
    # Ambil semua testimoni terbaru
    daftar_testimoni = Testimoni.objects.order_by('-tanggal')
    # Render halaman testimoni
    return render(request, 'testimoni.html', {'form': form, 'daftar_testimoni': daftar_testimoni})


# View untuk halaman utama (landing page)
def index(request):
    return render(request, 'index.html')

