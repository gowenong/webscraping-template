from bs4 import BeautifulSoup
import requests
import csv

"""
INSPIRATION: Data Science Dojo on YouTube (https://www.youtube.com/channel/UCzL_0nIe8B4-7ShhVPfJkgw)

Scrapes Newegg products for brand, product name, price, rating, # ratings, shipping
Walkthrough video: https://www.youtube.com/watch?v=XQgXKtPSzUI (CODE NOT EXACTLY LIKE VIDEO)

"""

source = requests.get('https://www.newegg.com/p/pl?N=100007671').text

# html parsing
soup = BeautifulSoup(source, 'html.parser')
containers = soup.find_all('div', class_='item-container')

csv_file = open('manual_gpu_table.csv', 'w') #second arg is "write"

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['brand', 'product name', 'price', 'rating', '# ratings', 'shipping'])

for c in containers:

    product_name = c.find('a', class_='item-title').text
    # print(product_name)

    price_current = c.find('li', class_='price-current')
    price = price_current.strong.text + price_current.sup.text
    print(price)

    try:
        brand = c.find('div', class_='item-branding').a.img['title']
        print(brand)

        ratings_container = c.find('div', class_='item-branding').find('a', class_='item-rating')
        rating = ratings_container['title'].split(" ")[2]
        print(rating)

        num_ratings = ratings_container.span.text
        num_ratings = num_ratings[1: len(num_ratings) - 1]
        print(num_ratings)

        shipping_price = c.find('li', 'price-ship').text.split(" ")[8]
        shipping = f'{shipping_price} Shipping'
        print(shipping)
    except Exception as e:
        brand = None
        rating = None
        num_ratings = None
        shipping = None

    print()
    csv_writer.writerow([brand, product_name, price, rating, num_ratings, shipping])

csv_file.close()
