from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

# Establishing connection, then reading the page and closing the client
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# HTML Parsing
page_soup = soup(page_html, "html.parser")

#Grabs Item containers
containers = page_soup.findAll("div", {"class":"item-container"})

# Opening a csv file to write to
filename ="products.csv"
f = open(filename, "w")

headers = ["Brand, Product_Name, Current_Price, Average_Rating, Rating_Amount, Original_Price, Offers, Shipping\n"]

f.write(headers)

# Loops through each item, grabbing wanted info. about each item.
# Made use of try and except just in case certain information is ungiven.
for container in containers:

	brand_name = 'N/A'
	item_name = 'N/A'
	current_price = 'N/A'
	rating_avg = 'N/A'
	rating_amt = 'N/A'
	original_price = 'N/A'
	offers = 'N/A'
	shipping = 'N/A'

	try:
		brand_name = container.find('div','item-info').div.a.img['title']
	except:
		pass

	try:
		item_name = container.find('a','item-title').text
	except:
		pass

	try:
		current_price = '$' + container.find('li','price-current').strong.text + container.find('li','price-current').sup.text
	except:
		pass

	try:
		rating_avg = container.find('a','item-rating').i['class'][1]
	except:
		pass

	try:
		rating_amt = container.find('a','item-rating').span.text
	except:
		pass

	try:
		original_price = container.find('li','price-was').span.text.strip()
	except:
		pass

	try:
		offers = container.find('a','price-current-num').text
	except:
		pass

	try:
		shipping = container.find('li','price-ship').text.strip()
	except:
		pass

	print("Brand name: " + brand_name)
	print("Item name: " + item_name)
	print("Current price: " + current_price)
	print("Rating avg: " + rating_avg)
	print("Rating amount: " + rating_amt)
	print("Original price: " + original_price)
	print("Offers: " + offers)
	print("Shipping: " + shipping)
	print('\n\n')
	
	
	f.write(brand_name + "," + 
			item_name + "," + 
			current_price + "," + 
			rating_avg.replace('rating-','') + "," + 
			rating_amt.replace('(','').replace(')','') + ",$" + 
			original_price + "," + 
			offers.replace('(','').replace(')','') + "," + 
			shipping + "\n")
	


f.close()