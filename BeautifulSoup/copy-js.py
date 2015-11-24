from bs4 import BeautifulSoup

import requests

url = input("Enter a  URL :  ")

r  = requests.get("http://" +url)

data = r.text

i=-1

choice=[]
soup = BeautifulSoup(data)
k=0
print("Stylesheets used on the page are : \n")
for link in soup.find_all('script'):
	k=int(k)
	k=k+1
	k=str(k)
	print (k+" . " +link.get('src'))
	choice.append(link.get('src'))

m = i
i=0
n=int(input("enter the serial number of the js file to save ,or \n press 0 to save all files \n : "))
if n==0 :
	while i<=m :
		s=str(i+1)
		fl = open("js_file"+ s +".js",'w+')
		temp = str(choice[i])
		if temp[:7]=='http://' or temp[:8]=='https://' :
			r=requests.get(choice[i])
		else :
			r=requests.get("http://" + url +'/' +choice[i])
		code=r.text
		content=BeautifulSoup(code)
		fl.write(str(content))
		i=i+1
		fl.close()
else :
	s=str(n)
	temp = str(choice[n-1])
	fl= open("js_file"+ s + ".js",'w+')
	if temp[:7]=='http://' or temp[:8]=='https://' :
			r=requests.get(choice[n-1])
	else :
		r=requests.get("http://" + url +'/' +choice[n-1])
	code=r.text
	content=BeautifulSoup(code)
	fl.write(str(content))
	fl.close()

