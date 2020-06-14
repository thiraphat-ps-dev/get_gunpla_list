from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import os

chrome_options = Options()
# Set Option to run chrome not open browser
chrome_options.add_argument("--headless")

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))  # Root directory
# Path to chromedriver file
DRIVER_BIN = os.path.join(PROJECT_ROOT, "./../chromedriver")

# Make browser with webdriver chrome
browser = webdriver.Chrome(executable_path=DRIVER_BIN, options=chrome_options)
browser.maximize_window()  # Maximize_window browser

kits = []  # Make Array
dictionary = {}  # Make Dictionary
pk = 1  # PK for id

# Link of data
mg = 'https://gundam.wikia.com/wiki/Master_Grade#Lineup'
rg = 'https://gundam.fandom.com/wiki/Real_Grade'
hg = 'https://gundam.fandom.com/wiki/High_Grade_Universal_Century'
pg = 'https://gundam.fandom.com/wiki/Perfect_Grade'
sd = 'https://gundam.fandom.com/wiki/SD_Gundam_Cross_Silhouette'

# Open browser with link
browser.get(mg)

# len of td
mg_td = 1284
rg_td = 272
hg_td = 552
pg_td = 120
sd_td = 119

# number of td in tr
mg_len = 6
sd_len = 7
pg_len = 6
hg_len = 6
rg_len = 8

# set td len and
td_len = mg_len
td_total = mg_td

# Get td
tds = browser.find_elements_by_css_selector("tr > td")

# for in 1 - 1284
for i in range(td_total):
    if(i % td_len == 0):  # td 1  image
        dictionary['id'] = pk  # create id
        print(pk)
        pk += 1
        try:
            image = tds[0].find_elements_by_css_selector(
                'div > a')[0].get_attribute('href')
        except IndexError:
            image = "No image available"
        dictionary['image'] = image

    elif(i % td_len == 1):  # td2 title and link
        title = tds[i].find_element_by_tag_name('a').get_attribute("title")
        link = tds[i].find_element_by_tag_name('a').get_attribute("href")
        print("title: " + title)
        print("link: " + link)
        dictionary['title'] = title
        dictionary['link'] = link

    elif(i % td_len == 2):  # td3     series
        series = tds[i].find_element_by_css_selector(
            'a').get_attribute("title")
        dictionary['series'] = series
        kits.append(dictionary)
        dictionary = {}

# Success and Close browser
print("==================================")
browser.close()

# Save data to file mg.json
with open('mg.json', 'w') as fp:
    json.dump(kits, fp)
