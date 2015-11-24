from bs4 import BeautifulSoup

import requests

url = input("Enter a  URL :  ")

r  = requests.get("http://" +url)

data = r.text

i=-1

choice=[]
soup = BeautifulSoup(data)

print("Stylesheets used on the page are : \n")
for link in soup.find_all('link'):
	str1 = link.get('rel')
	if(str1==['stylesheet']) :
		i=i+1
		k=str(i+1)
		print (k+" . " +link.get('href'))
		choice.append(link.get('href'))

m = i
i=0
n=int(input("enter the serial number of the css file to save ,or \n press 0 to save all files \n : "))
if n==0 :
	while i<=m :
		s=str(i+1)
		fl = open("css_file"+ s +".css",'w+')

		temp = str(choice[i])
		if temp[:7]=='http://' or temp[:8]=='https://' :
			r=requests.get(choice[i])
		else :
			r=requests.get("http://" + url +'/' +choice[i])
		code=r.text
		content=BeautifulSoup(code)

		r=requests.get("http://" +url +'/'+choice[i])
		code=r.text
		content=BeautifulSoup(code)
		fl.write(str(content))
		i=i+1
		fl.close()
else :
	s=str(n)
	temp = str(choice[n-1])
	fl= open("css_file"+ s + ".css",'w+')
	if temp[:7]=='http://' or temp[:8]=='https://' :
			r=requests.get(choice[n-1])
	else :
		r=requests.get("http://" + url +'/' +choice[n-1])
	code=r.text
	content=BeautifulSoup(code)
	fl.write(str(content))
	fl.close()
