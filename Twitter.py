import requests
from bs4 import BeautifulSoup
import os
import webbrowser

r = requests.get("http://www.twitter.com/karan_saxena")
soup = BeautifulSoup(r.content, "html.parser")

"""ans = soup.find_all("p",{"class":"tweet-text"})
print ans.string"""

ans=soup.find("p",{"class":"tweet-text"}).string
print soup.get_text()


