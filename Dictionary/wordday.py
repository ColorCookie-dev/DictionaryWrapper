from bs4 import BeautifulSoup as bs
import requests

data = requests.get("https://randomwordgenerator.com/")

soup = bs(data,"html5lib")

word = soup.findAll(".support")
print(word)