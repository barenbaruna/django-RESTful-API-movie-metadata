import requests
from bs4 import BeautifulSoup
import urllib.request

# Fungsi untuk mendapatkan URL gambar dari URL halaman
def get_image_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_element = soup.find('img', {'class': 'img-responsive'})
    if image_element:
        return image_element['src']
    else:
        return None

# Baca file .txt yang berisi URL gambar (satu URL per baris)
with open('file_urls.txt', 'r') as file:
    urls = file.readlines()

# Menghapus karakter newline (\n) dari setiap URL
urls = [url.strip() for url in urls]

# Mengatur nomor awal untuk nama file gambar
start_number = 1

# Iterasi melalui setiap URL dan mengunduh gambar dengan urutan berurutan
for url in urls:
    image_url = get_image_url(url)
    if image_url:
        # Membentuk nama file gambar dengan urutan berurutan
        file_name = f"{start_number:04}.jpg"
        
        try:
            # Mengunduh gambar menggunakan urllib.request
            urllib.request.urlretrieve(image_url, file_name)
            print(f"Gambar {file_name} berhasil diunduh.")
        except Exception as e:
            # Jika terjadi kesalahan saat mengunduh gambar, tetap menyimpan file dengan nama dummy
            file_name = f"{start_number:04}_dummy.jpg"
            print(f"Terjadi kesalahan saat mengunduh gambar. Gambar {file_name} tidak dapat diunduh.")
        
        # Menambahkan nomor untuk nama file berikutnya
        start_number += 1
    else:
        print(f"URL Gambar tidak ditemukan untuk URL: {url.strip()}")
