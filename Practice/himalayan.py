from bs4 import BeautifulSoup
import requests
import openpyxl

try:
    html=requests.get("https://thehimalayantimes.com/")
    html.raise_for_status()
except Exception as e:
    print(e)
    
soup=BeautifulSoup(html.text,"html.parser")
movies = soup.find("div",{"class":"alith_post_except"}).a.text.strip()
print(movies)

