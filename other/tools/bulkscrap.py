import requests
from bs4 import BeautifulSoup
import urllib.request

# Baca file .txt yang berisi URL gambar (satu URL per baris)
with open('file_urls.txt', 'r') as file:
    urls = file.readlines()

# Menghapus karakter newline (\n) dari setiap URL
urls = [url.strip() for url in urls]

# Mengatur nomor awal untuk nama file gambar
start_number = 1

# Iterasi melalui setiap URL dan mengunduh gambar dengan urutan berurutan
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_element = soup.find('img', {'class': 'img-responsive'})
    image_url = image_element['src']
    
    # Membentuk nama file gambar dengan urutan berurutan
    file_name = f"{start_number:04}.jpg"
    
    # Mengunduh gambar menggunakan urllib.request
    urllib.request.urlretrieve(image_url, file_name)
    
    # Menambahkan nomor untuk nama file berikutnya
    start_number += 1
