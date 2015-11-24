# *** Python script to  scrape any jabong page and displays the top 5 brands with 
#their total products and the percentage of the brand products
#  		Example : 
#				$ Python3 jabong-scraping..py					
#				Enter the url :  http://www.jabong.com/men/shoes/sneakers/
#				Currently there are 2679 products for this category
#				Enter the product name or enter 0 for the list of all brands
#				Nike
#				Nike has total of 74 products

 #				Nike contributes to approximately 2.7622 % of products on jabong
#
#				Top 5 brands on jabong for current category are :
#				Vans has total of 315 products on jabong which is about 11.7581% of all products
#				Puma has total of 126 products on jabong which is about 4.7032% of all products
#				Fila has total of 111 products on jabong which is about 4.1433% of all products
#				DC has total of 93 products on jabong which is about 3.4714% of all products
#				Yepme has total of 93 products on jabong which is about 3.4714% of all products

from bs4 import BeautifulSoup

import operator

import requests

url = input("Enter the url :   ")

if url[0:4]=="http":
	req = requests.get(url)

else :
	req = requests.get("http://" + url)
fl = open("jabong-brand.txt",'w+') #this file stores the name all brand with thier product count as dictionary 
content = req.text
code= BeautifulSoup(content)
store = code.find('div',"all-brand-filters")

i=0
sum1=0
count=0

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
	sum1+=int(num1)
	count+=1
	
	brand[brand_name]=num1

fl.write(str(brand));
i=0
print("Currently there are " +str(sum1) +" products for this category")
n =str(input("Enter the product name or enter 0 for the list of all brands\n \t"))

if n=='0':

 	for value in brand :
 		print(value + " has total of \t"+ brand[value] +" products on jabong")

 		i=i+1
 		
else :

	print(n +" has total of " + brand[n] +" products")
	price =brand[n]
	price=int(price)

	k=int(price*100/sum1*10000)
	k/=10000

	print("\n " + n + " contributes to approximately " + str(k) + " percentage of products on jabong")

print("\n\n Top 5 brands on jabong for current category are :")

sorted_brand = sorted(brand.items(), key=lambda x: (-int(x[1]), x[0]))

i=0
for value in sorted_brand :
	price=int(value[1])

	price=int(price)

	k=int((price*100/sum1)*10000)
	k=k/10000

	print(str(value[0]) + " has total of " + str(value[1]) +" products on jabong which is about " +str(k) + "percentage of all products")

	i=i+1
	if i>=5:
		break

fl.close()