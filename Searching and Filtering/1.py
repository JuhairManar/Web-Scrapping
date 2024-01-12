from bs4 import BeautifulSoup
import requests
import re

with open('index.html','r') as p:
    doc=BeautifulSoup(p,'html.parser')
    
tag=doc.find('option')


print(tag.attrs)

tags=doc.find_all(class_='btn-item')


tag=doc.find_all('input',type='text')
for t in tag:
    t['placeholder']="Changed"

with open('changed.html','w') as file:
    file.write(str(doc))    
