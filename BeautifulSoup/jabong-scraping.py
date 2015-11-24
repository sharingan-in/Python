from bs4 import BeautifulSoup
import requests
url = input("Enter the url")
req = requests.get("http://" + url)
content = req.text
code= BeautifulSoup(content)
fl = open("file"+'2'+".txt",'w+')
store = code.find('div',"all-brand-filters")
i=0
brand={}
num=[]
for i in store.find_all('label') :
	link = i.find('a','filter-link')
	brand_name = link.get('title')
	number = i.find('small')
	num = number.get_text()
	num = str(num)
	j=1
	num1="a"
	while num[j]!=']':

		j=j+1
	
	num1=num[1:j]

	
	brand[brand_name]=num1
fl.write(str(brand));
print(brand)
fl.close()