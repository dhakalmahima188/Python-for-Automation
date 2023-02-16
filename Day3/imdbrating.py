from bs4 import BeautifulSoup
import requests
import openpyxl

try:
    html=requests.get("https://www.imdb.com/chart/top")
    html.raise_for_status()
except Exception as e:
    print(e)
    
soup=BeautifulSoup(html.text,"html.parser")
movies = soup.find("tbody",{"class":"lister-list"}).find_all("tr")
# movies_data_title=movies.find_all("td",{"class":"titleColumn"})
# print(movies_data_title)
movies_data_title=['Rank','Title','Year','Rating']
movies_data=[]
for movie in movies:
    name=movie.find("td",{"class":"titleColumn"}).a.text
    rank=movie.find("td",{"class":"titleColumn"}).get_text()
    rank=movie.find("td",{"class":"titleColumn"}).get_text(strip=True).split(".")[0] #whitespace remove    
    year=movie.find("td",{"class":"titleColumn"}).span.text.strip("()")
    rating=movie.find("td",{"class":"ratingColumn imdbRating"}).strong.text
    movies_data.append([rank,name,year,rating])
print(movies_data)
# create a new workbook
workbook = openpyxl.Workbook()

# select the active worksheet
worksheet = workbook.active

# define some data to write to the worksheet
data = movies_data

# iterate over the data and write it to the worksheet
for row in data:
    worksheet.append(row)

# save the workbook
workbook.save('example.xlsx')