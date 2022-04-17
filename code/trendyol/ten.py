from selenium import webdriver
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from googletrans import Translator

translator = Translator()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('disable-notifications')

driver = webdriver.Chrome('chromedriver.exe', options= chrome_options)

driver.maximize_window()

driver.get("https://www.trendyol.com/no-name/6-adet-100-metre-akrilik-koli-bandi-45mmx100-m-kopmayan-koli-bandi-guclu-koli-bandi-p-96952142")
companys = []
titles = []
prices = []
links = []
titleEngs = []
reviews = []
ratings = []
selerCounts = []
# time.sleep(20)

for i in range(2):

    try:
        company = driver.find_element_by_class_name('prdct-desc-cntnr-ttl').text
        title = driver.find_element_by_class_name('prdct-desc-cntnr-name').text.replace(company, "")
        titleEng = translator.translate(title, src='tr', dest = 'en')
        price = driver.find_element_by_class_name('prc-box-dscntd').text
        rating = driver.find_element_by_class_name("pr-rnr-sm-p").text
        review = driver.find_element_by_css_selector(".pr-rnr-sm-p-s > span:nth-child(1)").text.replace("Değerlendirme", "")
        link = driver.find_element_by_class_name("")
        
    except NoSuchElementException:
        company = "N/A"
        title = "N/A"        
        titleEng = "N/A"        
        price = "0"        
        rating = "0"
        review = "0"
        link = "N/A"
        
    try:    
    
        selerCount = driver.find_element_by_class_name("pr-omc-tl").text.replace("Ürünün Diğer Satıcıları", "")
        selerCount = selerCount.replace("(","")
        selerCount = selerCount.replace(")","")

    except NoSuchElementException:
        selerCount = "0"

    time.sleep(10)
    print("{}/250".format(i))

companys.append(company)
titles.append(title)
titleEngs.append(titleEng)
prices.append(price)
reviews.append(review)
ratings.append(rating)
selerCounts.append(selerCount)
links.append(link)


list_of_tuples = list(zip(companys, titles, titleEngs, prices, reviews, ratings, selerCounts,links))

df = pd.DataFrame(list_of_tuples, columns= ['Company Name', 'ProductTurkTitle', 'ProductEngTitle', 'Product Price', 'Review', 'Ratings', 'Seler Counts', 'Product Link'])

df.to_excel('trendyolNew.xlsx')