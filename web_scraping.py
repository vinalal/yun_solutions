from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
import requests

root = "https://www.google.com/"
link = "https://www.google.com/search?q=reliance+industries+limited&sca_esv=ad13dc3ec98af71c&tbm=nws&prmd=inmsvbtz&sxsrf=ACQVn0-9YgiKt8equTN5J4pW8eVny1dTPw:1710684090778&source=lnt&sa=X&ved=2ahUKEwip2rbsuvuEAxVymq8BHQ20Brg4ChCnBXoECAIQFA&tbas=0&biw=786&bih=268&dpr=1.25"

data ={}
def news(link,n):
  if(n == 0):
    return 0
  req = Request(link,headers={'User-Agent' : 'Chrome'})
  webpage = urlopen(req).read()
  with requests.Session() as c:
    soup = BeautifulSoup(webpage,'html5lib')
    for item in soup.find_all('div',attrs = {'class':'Gx5Zad fP1Qef xpd EtOod pkphOe'}):
      raw_link = (item.find('a',href = True)['href'])
      link = raw_link.split("/url?q=")[1].split('&sa=U&')[0]
      sit = link.split("//")[1]
      site = sit.split("/")[0]
      #print(item)
      title = (item.find('div',attrs = {'class':'BNeawe vvjwJb AP7Wnd'}).get_text())
      des = (item.find('div',attrs = {'class':'BNeawe s3v9rd AP7Wnd'}).get_text())
      des = des[0:len(des)-10]
      #print(des)
      #print(title)
      #print(link)
      data[site] = des
    
    next = soup.find('a',attrs = {'aria-label':'Next page'})
    next = (next['href'])
    link = root + next
    news(link,n-1)

news(link,10)

with open("urls.txt", "w") as file:
  for key, value in data.items():
    print(f"{key}: {value}", file=file)
    
    
