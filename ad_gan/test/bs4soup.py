'''from bs4 import BeautifulSoup
#soup = BeautifulSoup('bs4.html', 'html5lib')
#print(soup.prettify())
with open("bs4.html") as fp:
    soup = BeautifulSoup(fp, features='html5lib')

#soup = BeautifulSoup("<html>data</html>", features='html5lib')
print(soup.find_all('a'))'''

from bs4 import BeautifulSoup
import requests
import os

def get_website_soup(url):
    r = requests.get(url)
    text = r.text
    soup = BeautifulSoup(text, 'html5lib')
    
    return soup

def find_clean_links(link):
    if 'https' in link or 'http' in link:
        return link
    else:
        return None

def split_queries(link):
    if '?' in link:
        new_link = link.split('?')[0]
        return new_link
    else:
        return link
        
def find_all_images_links(url):
    links = []
    soup = get_website_soup(url)
    for link in soup.find_all('img'):
        url = find_clean_links(link.get('src'))
        if url == None:
            continue
        else:
            new_link = split_queries(url)
            links.append(new_link)
    
    return links

url = 'https://www.adsoftheworld.com/?terms=&medium=1&industry=19&country=All'
links = find_all_images_links(url)

url2 = links[1]
page = requests.get(url2)
f_ext = os.path.splitext(url2)[-1]
f_name = 'img{}'.format(f_ext)
with open(f_name, 'wb') as f:
    f.write(page.content)

'''import requests

url = "https://www.adsoftheworld.com/media/print/exide_killer_colours_motorcycle_splash_suv_splash_hatchback_splash" 

r = requests.get(url)
text = r.text
print(text)'''

#This is the code to download the image but still needs some tweeking
'''import os
import requests

url = 'https://d3nuqriibqh3vw.cloudfront.net/tunnel.png'
page = requests.get(url)

f_ext = os.path.splitext(url)[-1]
f_name = 'img{}'.format(f_ext)
with open(f_name, 'wb') as f:
    f.write(page.content)'''

