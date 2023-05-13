from url_2_dt import url_2_binary_array
from add_csv import add_df_to_csv
import requests
from bs4 import BeautifulSoup


def char_to_int(char):
    if char == 'A':
        return 0
    elif char == 'D':
        return 1
    elif char == 'G':
        return 2
    elif char == 'H':
        return 3
    elif char == 'R':
        return 4
    elif char == 'S':
        return 5
    elif char == 'W':
        return 6
    elif char == 'Y':
        return 7
    else:
        return 8

def get_nav_links(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Use Beautiful Soup to parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the divs with class 'nav-col'
    nav_cols = soup.find_all('div', {'class': 'nav-col'})

    # Initialize an empty list to store the href links
    hrefs = []
    # Loop through each nav-col div
    for nav_col in nav_cols:
        # Find all the <a/> elements with class 'toc-item' within the nav-col div
        toc_items = nav_col.find_all('a')
        # Loop through each    toc-item <a/> element and extract the href link
        for toc_item in toc_items:
            href = toc_item['href']
            text = toc_item.text.strip()
            hrefs.append([href, text[0]])

    # Return the list of href links
    return hrefs

def get_thumbnail_images(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    thumbnail_images = []
    for img in soup.find_all('img', {'class': 'thumbnail'}):
        thumbnail_images.append(img['src'])
    return thumbnail_images

urls = get_nav_links('https://www.medievalscribes.com/index.php?page=about&nav=off')

for url in urls:
    if url[0].endswith('nav=off'):
        if not url[1].startswith('Various'):
            i = get_thumbnail_images(url[0])
            print(url, 'url of urls')
            for num, my_url in enumerate(i):
                my_class = int(char_to_int(url[1]))
                df = url_2_binary_array(my_class, my_url)
                add_df_to_csv(df, 'data.csv')
        

#i = get_thumbnail_images('https://www.medievalscribes.com/index.php?navtype=letters&letter=1&n=0&browse=letters&nav=off')
#
#for url in i:
#    my_class = 0
#    print(url, 'url from pup')
#    df = url_2_binary_array(my_class, url)
#    add_df_to_csv(df, 'data.csv')