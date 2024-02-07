# CompSci Create Project
# Version 1.0
import requests
from bs4 import BeautifulSoup

# Example URL for the Library of Congress: https://catalog.loc.gov/vwebv/search?searchArg=SEARCHARGUMENTGOESHERE&searchCode=GKEY%5E*&searchType=0&recCount=25
endpoint = 'books'
url = f'https://www.loc.gov/{endpoint}/?fo=json'
PARAMETERS = {
    'q' : "all the light we cannot see",
    'format' : 'books',
    'fa=language' : 'english',
    'fa=subject' : 'Saint-Malo',
    'sp' : '1'
}
request = requests.get(url=url,params = PARAMETERS)
data = request.json()
print()
print()
print(data)


"""URL = "https://catalog.loc.gov/vwebv/search?searchArg=a+man+called+ove&searchCode=GKEY%5E*&searchType=0&recCount=25"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"} 
request = requests.get(URL, headers=headers)
soup = BeautifulSoup(request.content, 'html5lib')
item_class = "search-results-list-description-item "
item_a = soup.findAll('div', class_="search-results-list-description-item search-results-list-description-title")
date = soup.findAll('div', class_='search-results-list-description-date')
location_a = soup.findAll('div', class_='search-results-list-description-item search-results-list-description-request')

print(soup.prettify())
for item in location_a:
    
    print(item)
    location = str(item)
    print(location)
    print(len(location_a))
for x in item_a:
    print(item)
for item in date:
    print(date)"""
