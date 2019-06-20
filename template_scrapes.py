from scraping_template import og_scrape

""" Newegg CPUs """
url = 'https://www.newegg.com/p/pl?N=100007671'
csv_name = 'template_cpu_table.csv'
brand_value = "c.find('div', class_='item-branding').a.img['title']"
product_value = "c.find('a', class_='item-title').text"
price_value = "c.find('li', class_='price-current').strong.text + c.find('li', class_='price-current').sup.text"
rating_value = "c.find('div', class_='item-branding').find('a', class_='item-rating')['title'].split(" ")[2]"
num_ratings_value = "c.find('div', class_='item-branding').find('a', class_='item-rating').span.text[1: -1]"
shipping_value = "c.find('li', 'price-ship').text.split(' ')[8] + ' Shipping'"

# container_tag defaults to 'div'
og_scrape(url, csv_name, 'item-container', brand=brand_value, product=product_value, price=price_value, rating=rating_value, num_ratings=num_ratings_value, shipping=shipping_value)

""" coreyms website """
url = 'http://coreyms.com'
csv_name = 'template_blog_table.csv'
headline_value = "c.h2.a.text"
summary_value = "c.find('div', class_='entry-content').p.text"
yt_link_value = "'https://youtube.com/watch?v=' + c.find('iframe', class_='youtube-player')['src'].split('/')[4].split('?')[0]"

og_scrape(url, csv_name, None, 'article', headline=headline_value, summary=summary_value, yt_link=yt_link_value)
