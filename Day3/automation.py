import requests
from bs4 import BeautifulSoup
import datetime

# send a GET request to the timeanddate.com page for today's date
url = "https://www.timeanddate.com/date/today.html"
response = requests.get(url)

# parse the HTML response and extract the current date
soup = BeautifulSoup(response.content, 'html.parser')
date_str = soup.find('title').text.split()[-1]

# convert the date string to a datetime object and print it
date_obj = datetime.datetime.strptime(date_str, '%B %d, %Y')
print(date_obj.date())
