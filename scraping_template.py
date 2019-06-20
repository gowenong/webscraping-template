from bs4 import BeautifulSoup
import requests
import csv
import copy

"""
***** Traversy Media Scraping Methods NOTES ******

# find_all() and findAll() are equivalent
el = soup.find_all('div')[1] #findAll() does same thing
el = soup.find(id='section-1')
el = soup.find(class_='items')
el = soup.find(attrs={"data-hello": "hi"})

# select - similar to JQuery
el = soup.select('#section-1')[0] // id, select always returns a list
el = soup.select('.item')[0] // class

# get_text()
el = soup.find(class_='item').get_text()
for item in soup.select('.item'):
    print(item.get_text())

# Navigation
el = soup.body.contents[1].contents[1].find_next_sibling() # line break is the 0th element
el = soup.find(id='section=2').find_previous_sibling()
el = soup.find(class_='item').find_parent()
el = soup.find('hs').find_next_sibling('p')

================================================================================================

***** SCRAPING ON A TEST FILE (see simple.html) ******
with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

print(soup.prettify()) # indents
match = soup.title.text
find_all returns list of all tags that match element
for article in soup.find_all('div', class_='article'): # _ because class is special keyword
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()

================================================================================================
================================================================================================

******************** OG SCRAPING TEMPLATE **************************

takes in a url and other info and creates csv file

url, file_name (.csv), container_tag, and container_class are Strings,
**kwargs are key=value pairs, where keys are column names and values
are targeted Strings in the HTML (should begin with a c.find(...))

"""

def og_scrape(url, file_name, container_class, container_tag='div', **kwargs):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'html.parser')

    if (container_class is None):
        containers = soup.find_all(container_tag)
    else:
        containers = soup.find_all(container_tag, class_=container_class)

    csv_file = open(file_name, 'w') #second arg is "write"
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(list(kwargs.keys()))

    for c in containers:
        targeted_values = copy.deepcopy(kwargs)
        for key, value in targeted_values.items():
            try:
                print(eval(value))
                targeted_values[key] = eval(value)
            except Exception as e:
                targeted_values[key] = None
        print()
        csv_writer.writerow(list(targeted_values.values()))

    csv_file.close()
