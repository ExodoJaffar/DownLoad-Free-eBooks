# -*- coding: utf-8 -*-
#IMPORTANDO OS MODULOS
import requests 
from bs4 import BeautifulSoup as bs

email = str(input('EMAIL --> ')) 
senha = str(input('SENHA -->'))

#DEFININDO O HOST
url = 'https://www.packtpub.com'

#FORM PARA LOGIN
login ={
'email': email,
'form_build_id':'form-ecf103a8d90be0ff61d9491510e16a30',
'form_id':'packt_user_login_form',
'op':'Login',
'password': senha
}

#FORM PARA SALVAR O LIVRO
#recaptcha = {'g-recaptcha-response':'03AL4dnxqUqqVAL6nZHP5JBdZFH4zRxWEJAQ3G9monrdPbZeADg6mOBiGWrkmEM_LzLk-7xlk3Gd_mRRO0zOk2o4w3M-1oCvLaO6ZKfMl5t9jPF0fdw-SRAWYOP0Q4nyahkw2CarV724MtdaHHAe1sI3gO6HuVV_TnkeWCB8s0u2fbpn-riOEENJ6dITi-oErR_Oh-H6PLwiCG4H5iHCMzT3gOJ0gTJEqYk8SE_TFMAL6ry7Xcd97iXIXhlBmFFEPePJ0caJzGPZ5Kr4S4EObYkQrrg6Bh62kaxg'}

#CABECALHO DO REQUESTS
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}

#DEFININDO O OBJETO SESSION
s = requests.Session()

#ATUALIZANDO O CABECALHO
s.headers.update(head)
#print(s.headers)

#REQUESTS LOGIN
r = s.post(f'{url}/packt/offers/free-learning', data=login)
r.encoding = 'utf-8'
#print(s.cookies)
#print(r.cookies)
#print(r.headers)

#PEGANDO BOOKID PARA BAIXAR O LIVRO
date = bs(r.text,'html.parser')
a = date.find(id="free-learning-form").get('action')
url2 = f'{url}{a}'
#print(a)

#PEGANDO O TITULO
titulo = date.find('div', class_='dotd-title').find('h2').text.strip()
#print(titulo)

#SALVANDO O LIVRO NA CONTA
r = s.post(url2)#, data=recaptcha)
print(r.status_code)
#print(r.headers)

#BAIXANDO O LIVRO
bookid = a.split('/')[2]
down = f'{url}/ebook_download/{bookid}/pdf'
r = s.get(down)#, data=recaptcha)
foto = open(f'{titulo}.pdf','wb')
foto.write(r.content)
foto.close()
#print(bookid)
#print(down)

