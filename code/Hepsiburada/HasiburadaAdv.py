from matplotlib import collections
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('disable-notifications')

driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
driver.maximize_window()

driver.get("https://www.hepsiburada.com/kirtasiye-ofis-urunleri-c-2147483643")


scroll = 150
for i in range(200):
    driver.execute_script("window.scrollTo(0, {})".format(scroll))
    scroll = scroll + 150
    print(i)
    time.sleep(1)

Title =[]
Brand = []
Price = []
Rating = []
Evaluation = []
Link = []
links = driver.find_elements_by_class_name("moria-ProductCard-gyqBb")
for i in links:
    Link.append(i.get_attribute("href"))
    print(i.get_attribute("href"))
print(len(Link))

list_of_tuples = list(zip(Link))
df = pd.DataFrame(list_of_tuples, columns= ['Product Link'])
df.to_excel("hasiburada.xlsx")



# for i in range(len(Link)):
#     driver.get(Link[i])
#     try:

#         title= driver.find_element_by_css_selector("#product-name").text
#     except NoSuchElementException:
#         title = "N/A"
#     try:

#         brand = driver.find_element_by_css_selector("body > div.wrapper > main > div.product-detail-module > section.detail-main > div.container.contain-lg-4.contain-md-4.contain-sm-1.fluid > div > div.productDetailRight.col.lg-2.md-2.sm-1.grid-demo-fluid > div.product-information.col.lg-5.sm-1 > span").text
#     except NoSuchElementException:
#         brand = "N/A"
#     try:

#         price = driver.find_element_by_css_selector("#offering-price").text.replace("TL", "")
#     except NoSuchElementException:
#         price = "N/A"

#     try:
#         rating = driver.find_element_by_class_name("rating-star").text
#     except NoSuchElementException:
#         rating = "N/A"

#     try:
#         evaluation = driver.find_element_by_id("comments-container").text.replace("Değerlendirme", "")
#     except NoSuchElementException:
#         evaluation = "N/A"
#     Title.append(title)
#     Brand.append(brand)
#     Price.append(price)
#     Rating.append(rating)
#     Evaluation.append(evaluation)
#     print("{} / {}".format(i+1,len(Link)))

# list_of_tuples = list(zip(Title, Brand, Price, Rating, Evaluation, Link))
# df = pd.DataFrame(list_of_tuples, columns= ['Product Title', 'Brand Name', 'Price', 'Rating', 'Evaluations', 'Product Link'])
# df.to_excel("HasiburadaOverview.xlsx")