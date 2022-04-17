from numpy import integer
from selenium import webdriver
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from googletrans import Translator


translator = Translator()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('disable-notifications')

driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)



driver.get("https://www.trendyol.com/kirtasiye-ofis-malzemeleri-x-c104125")
driver.maximize_window()
time.sleep(20)

scroll = 150

for i in range(750):
    
    driver.execute_script("window.scrollTo(0, {})".format(scroll))
    scroll = scroll + 150
    print(i)
    time.sleep(1)





x = driver.find_elements_by_class_name('prdct-desc-cntnr-ttl')
y = driver.find_elements_by_class_name('prdct-desc-cntnr-name')
z = driver.find_elements_by_class_name('prc-box-dscntd')

    
company = []
title = []
price = []
link = []
titleEng = []

for i in range(len(x)):
    a = x[i].text
    b = y[i].text
    c = b.replace(a, "")
    d = translator.translate(c, src='tr', dest='en').text
    price.append(z[i].text.replace("TL", ""))
    company.append(a)
    title.append(c)
    titleEng.append(d)
    



element = driver.find_elements_by_css_selector("div[class='p-card-chldrn-cntnr']>a")
# link = element.get_attribute("href")

for i in element:
    link.append(i.get_attribute("href"))


list_of_tuples = list(zip(company, title,titleEng, price, link))

df = pd.DataFrame(list_of_tuples,
                  columns = ['Company Name', 'ProductTurkTitle','ProductEngTitle', 'Trendyol Price', 'Product Link'])


df.to_excel('trendyol.xlsx')

driver.close()
reviews = []
ratings = []
selerCounts = []

driver1 = webdriver.Chrome('chromedriver.exe', options=chrome_options)
for i in range(len(link)):
    url = link[i]
    driver1.get(url)
    driver1.maximize_window()
    driver1.execute_script("window.scrollTo(0, 350)")
    time.sleep(2)
    driver1.execute_script("window.scrollTo(0, 700)")
    time.sleep(2)
    driver1.execute_script("window.scrollTo(0, 1050)")
    time.sleep(2)
    driver1.execute_script("window.scrollTo(0, 1400)")
    time.sleep(2)
    driver1.execute_script("window.scrollTo(0, 1750)")
    time.sleep(2)
    
    try:

        rating = driver1.find_element_by_class_name("pr-rnr-sm-p").text
        
        review = driver1.find_element_by_css_selector(".pr-rnr-sm-p-s > span:nth-child(1)").text.replace("Değerlendirme", "")
        # pricess = driver1.find_elements_by_class_name("mrc-new")
        
    except NoSuchElementException:
        rating = "0"
        review ="0"
        # pricess = "Nil"
    # for i in pricess:
    #         print(i.text) 
    try:    
    
        selerCount = driver1.find_element_by_class_name("pr-omc-tl").text.replace("Ürünün Diğer Satıcıları", "")
        selerCount = selerCount.replace("(","")
        selerCount = selerCount.replace(")","")

    except NoSuchElementException:
        selerCount = "0"

       

    reviews.append(review)
    ratings.append(rating)
    selerCounts.append(selerCount)
    # driver1.close()
    # progress = int((i*100)/len(link))
    # print(progress)
    print("{} / {}".format(i, len(link)))
    


list_of_tupless = list(zip(company, title, titleEng, price, reviews, ratings,selerCounts, link))
df1 = pd.DataFrame(list_of_tupless,
                  columns = ['Company Name', 'ProductTurkTitle','ProductEngTitle', 'Trendyol Price', 'Reviews', 'Ratings','Seler Count', 'Product Link'])

df1.to_excel("TrendyolOverview.xlsx")


driver1.close()