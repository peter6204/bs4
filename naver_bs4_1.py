import urllib.request
import urllib.parse
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

baseUrl = 'https://en.dict.naver.com/#/search?range=all&query='
plusUrl = input('검색어를 입력하세요: ')
url = baseUrl +urllib.parse.quote_plus(plusUrl) 
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')


title = soup.find('div', {'id':'container'}).find('dd').find('span', {'class':'word_class'}).get_text()

print(title)





