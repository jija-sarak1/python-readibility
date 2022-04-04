import requests
from readability import Document
from bs4 import BeautifulSoup
response= requests.get("https://www.artofmanliness.com/style/accessories/guide-to-fragrance/")
doc = Document(response.text)
print(doc.title())

summary = doc.summary()
from bs4 import BeautifulSoup
cleantext = BeautifulSoup(summary, "lxml").text
print(cleantext)