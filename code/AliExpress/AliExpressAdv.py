from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import openpyxl
from googletrans import Translator

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('disable-notifications')

driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)

# driver.get("https://www.aliexpress.com/category/1509/jewelry-accessories.html?trafficChannel=main&catName=jewelry-accessories&CatId=1509&ltype=wholesale&SortType=default&page=1&isrefine=y")
driver.maximize_window()

# driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/div[4]/div/a/span[5]").click()
# # driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/div[4]/div/div/div/div[3]/div/span").click()
# # driver.find_element_by_css_selector("#nav-global > div.ng-item-wrap.ng-item.ng-switcher.active > div > div > div > div.switcher-currency.item.util-clearfix > div > ul > li:nth-child(1) > a").click()
# # time.sleep(5)

link = []
for j in range(1,26,1):
    driver.get("https://www.aliexpress.com/category/21/education-office-supplies.html?trafficChannel=main&catName=education-office-supplies&CatId=21&ltype=wholesale&SortType=default&page={}".format(j))
    scroll = 150   
    for i in range(30):
        
        driver.execute_script("window.scrollTo(0, {})".format(scroll))
        scroll = scroll + 150
        # print(i)
        time.sleep(1)

    element = driver.find_elements_by_css_selector("#root > div.glosearch-wrap > div > div.main-content > div.right-menu > div > div.JIIxO > a")
    

    for i in element:
        link.append(i.get_attribute("href"))

    print(j)

# print(link)
print(len(link))
driver.close()

list_of_tuples = list(zip(link))

df = pd.DataFrame(list_of_tuples, columns= ['Product Link'])
df.to_excel("AliExpressStationaryLinks.xlsx")