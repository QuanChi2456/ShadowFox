import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Adolf_Hitler'

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.content, 'html.parser')

    headings = soup.find_all('h1') 
    for heading in headings:
        print(heading.text)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")