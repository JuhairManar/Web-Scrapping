from bs4 import BeautifulSoup
import requests

url="https://coinmarketcap.com"
result=requests.get(url).text
doc=BeautifulSoup(result,'html.parser') 


tbody=doc.tbody
trs=tbody.contents #table rows #all info as list
prices={}

for tr in trs:
    if len(tr.contents)>=4:
        name,price=tr.contents[2],tr.contents[3]
        if name.p and price.a:
            a=name.p.string  #p tag and its string
            b=price.a.string
            if a and b:
                prices.update({a:b})

#print(prices)    
