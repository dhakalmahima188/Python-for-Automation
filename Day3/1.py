#web data is in html format
#web page :a hypertext document on the World Wide Web.
#webscrapoing : requesting a web page from the internet and extracting information from it.
#Web browser :  retrieving, presenting, and traversing information resources on the World Wide Web.
#requests foo.html from example.com
#js gives logic, css: stylig, html: skeleton

import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Web_browser'

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the main text of the page by selecting the <div> with id 'mw-content-text'
main_text = soup.find('div', {'id': 'mw-content-text'})

# Print the text content of the <div>
print(main_text.get_text())
