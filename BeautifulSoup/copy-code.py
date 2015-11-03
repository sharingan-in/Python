from bs4 import BeautifulSoup
import requests
url = input("Enter the url")
req = requests.get("http://" + url)
content = req.text
code= BeautifulSoup(content)
fl = open("file.txt",'w+')
fl.write(str(code))
fl.close()