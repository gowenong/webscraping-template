from bs4 import BeautifulSoup
import requests
import csv

"""
SOURCE: Corey Schafer on YouTube (https://www.youtube.com/user/schafer5)

Scrapes Corey's blog for headline, summary, and youtube video links
Walkthrough video: https://www.youtube.com/watch?v=ng2o98k983k

"""

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'html.parser') # can also use 'lxml'

csv_file = open('manual_blog_table.csv', 'w') #second arg is "write"

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video link'])

#using .find instead of find_all finds the FIRST instance
for article in soup.find_all('article'):
    headline = article.h2.a.text #article.a.text also works because headline is first link within article
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    #in case there is no yt link
    try:
        #access tags like a dictionary
        vid_src = article.find('iframe', class_='youtube-player')['src']

        #parsing
        vid_id = vid_src.split('/')[4] #splits string into a list of values based on character specified
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)
    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
