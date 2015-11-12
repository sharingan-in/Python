#this code only works for the images stored on the same server as of the web page
from bs4 import BeautifulSoup
import requests
url = input("Enter the url :  ")
req = requests.get("http://" +url)
content= req.text
code= BeautifulSoup(content)
print("link of all images in the page : \n")
for check in code.find_all('img'):
    print(url + "/" + check.get('src'))

