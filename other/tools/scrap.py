import requests
from bs4 import BeautifulSoup
import urllib.request

url = 'https://thetvdb.com/movies/6-underground'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
image_element = soup.find('img', {'class': 'img-responsive'})
image_url = image_element['src']

urllib.request.urlretrieve(image_url, '0003.jpg')
