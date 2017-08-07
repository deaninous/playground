import requests
import re 
from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup           
import json

site = 'https://www.packtpub.com/packt/offers/free-learning/feelearning-claim/19444/21478'
# site = "http://www.lepays.bf"
headers ={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"}
req = requests.post(site, headers = headers)

print(req.status_code)

# b = BeautifulSoup(req.text, 'html.parser')
# f = b.find(id='free-learning-form')
# print(f)
# the_form = b.find('form', attrs = {'id' : 'free-learning-form'})
# print(the_form)
