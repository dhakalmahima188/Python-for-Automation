import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Web_browser'

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(response.content, 'html.parser')
