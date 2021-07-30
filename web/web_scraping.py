from bs4 import BeautifulSoup
import requests

uri = 'https://www.avare.sp.gov.br'
website = requests.get(uri)

soup = BeautifulSoup(website.content, 'html.parser')

min_temperture = soup.find('span', class_='minClima')
max_temperture = soup.find('span', class_='maxClima')

print(min_temperture.text)
print(max_temperture.text)

page_title = soup.find('title')
print(page_title.text)