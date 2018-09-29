# -*- coding: utf-8 -*-
import requests 
from bs4 import BeautifulSoup as bs

#FORM PARA LOGIN
login ={
'email':'email',
'form_build_id':'form-9427b852e95009d16f1234ffea053714',
'form_id':'packt_user_login_form',
'op':'Login',
'password':'senha'
}

#CABECALHO DO REQUESTS
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}

#DEFININDO O OBJETO SESSION
s = requests.Session()
s.headers(head)

#REQUESTS LOGIN
r = s.post('https://www.packtpub.com/packt/offers/free-learning', headers=head , data=login)
r.encoding = 'utf-8'
print(r.cookies)
#print(r.status_code,r.headers)

date = bs(r.text,'html.parser')
a = date.find(id="free-learning-form").get('action')
#print(date)

r2 = s.get('https://www.packtpub.com/' + a)
print(r2.status_code,r2.headers)

with open('debug.txt','w') as p:
  for text in str(r.status_code), '\n' , str(r.headers).replace("',","'\n"):
    p.write(text)

#BASE PARA DONWLOAD
'''<div class="product-line seen" nid="29793" title="Mastering CSS [eBook]">
	/ebook_download/VAR/pdf
	https://www.packtpub.com/ebook_download/29355/pdf
'''
