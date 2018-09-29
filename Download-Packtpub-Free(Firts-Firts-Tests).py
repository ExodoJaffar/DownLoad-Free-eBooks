import requests
from bs4 import BeautifulSoup as bs

head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}
a = requests.get('https://www.packtpub.com/packt/offers/free-learning#',  headers=head)
a.encoding = 'utf-8'
#print(a.status_code)
#print(a.text)

date = bs(a.text, 'html.parser')
print(date.find(id="free-learning-form").get('action'))



