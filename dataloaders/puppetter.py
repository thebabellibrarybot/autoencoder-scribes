from url_2_dt import url_2_binary_array
from add_csv import add_df_to_csv
import requests
from bs4 import BeautifulSoup


def alphabet_to_numbers(s):
    # convert to lowercase to handle uppercase letters
    s = s.lower()
    # initialize empty result list
    result = []
    # loop through each character in the string
    for c in s:
        # check if the character is a letter
        if c.isalpha():
            # convert the letter to its alphabetical position (0-indexed)
            num = ord(c) - 97
            # append the number to the result list
            result.append(num)
    # return the result list
    return result

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
            print(url, 'url in urls')
            for num, my_url in enumerate(i):
                my_class = int(alphabet_to_numbers(url[1])[0])
                df = url_2_binary_array(my_class, my_url)
                add_df_to_csv(df, 'data.csv')
        

#i = get_thumbnail_images('https://www.medievalscribes.com/index.php?navtype=letters&letter=1&n=0&browse=letters&nav=off')
#
#for url in i:
#    my_class = 0
#    print(url, 'url from pup')
#    df = url_2_binary_array(my_class, url)
#    add_df_to_csv(df, 'data.csv')