from bs4 import BeautifulSoup
import requests

url="https://www.amazon.com/ASUS-Touchscreen-Processor-Kensington-M5401WYA-DH704T/dp/B0BDTSG2K1?ref_=Oct_DLandingS_D_3f1e67ef_14"

#print(requests.get(url).status_code) #check if fetching option is on
result=requests.get(url).text
doc=BeautifulSoup(result,'html.parser')

#print single
# tag=doc.find(text='$')
# parent=tag.parent
# next=parent.find_next()
# print(next.get_text().replace('.',''))

#single shortcut



#print multiple

# tags=doc.find_all(text='$')
# for i in tags:
#     parent=i.parent
#     next=parent.find_next()
#     print(next.get_text().replace('.',''))