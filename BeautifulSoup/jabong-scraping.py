from bs4 import BeautifulSoup
import operator
import requests
url = input("Enter the url")
if url[0:4]=="http":
	req = requests.get(url)
else :
	req = requests.get("http://" + url)
content = req.text
code= BeautifulSoup(content)
fl = open("file"+'2'+".txt",'w+')
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
n =str(input("enter the product name or enter 0 for all out of" + str(sum1)))
if n=='0':
 	for value in brand :
 		print(value + " has total of \t"+ brand[value] +" products on jabong")
 		i=i+1
 		
else :
	print(n +" has total of " + brand[n] +" products")
	price =brand[n]
	price=int(price)
	k=int(price*100/sum1)
	print("\n " + n + " contributes to approximately " + k + " percentage of products on jabong")
print("\n\n\n top 5 brands on jabong for current category are :")
sorted_brand = sorted(brand.items(), key=operator.itemgetter(1))
sorted_brand.reverse()
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