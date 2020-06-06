import requests
from bs4 import BeautifulSoup

r=requests.get("http://www.empik.com/bestsellery")
soup=BeautifulSoup(r.content)

#print(soup.prettify())

#print(soup.find_all("a"))

for link in soup.find_all("a"):
    print(link)


for link in soup.find_all("a"):
    print(link.get("href"))

for link in soup.find_all("a"):
    print(link.text)

#for link in soup.find_all("div",{"class":"price"}):
 #   print(link.text)

obiekty=soup.find_all("div",{"class":"price"})
print(len(obiekty))
for item in obiekty:
    print(item.text)