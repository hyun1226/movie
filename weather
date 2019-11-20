import requests
from bs4 import BeautifulSoup

location= input("지역을 입력해 주세요:")
URL = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query='+location+"날씨"
html = requests.get(URL).text
print(html)

soup = BeautifulSoup(html,'html.parser')
info = soup.find("p",{"class":"cast_txt"}).text
print(info)

min = soup.find("span",{"class":"min"}).text
print(min)
max = soup.find("span",{"class":"max"}).text
print(max)

all_li = soup.find_all("li")
print(all_li)
