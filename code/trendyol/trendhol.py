from selenium import webdriver
import time
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('disable-notifications')

driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)



# driver = webdriver.Chrome()
driver.get("https://www.trendyol.com/taki--mucevher-x-c28")
driver.maximize_window()
time.sleep(1)
# driver.find_element_by_class_name("overlay").click()
scroll =150
for i in range(100):
    
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
for i in range(len(x)):
    a = x[i].text
    b = y[i].text
    c = b.replace(a, "")
    price.append(z[i].text)
    company.append(a)
    title.append(c)

driver.close()

list_of_tuples = list(zip(company, title, price))

df = pd.DataFrame(list_of_tuples,
                  columns = ['Company Name', 'ProductTurkTitle', 'Trendyol Price'])


df.to_excel('trendyol.xlsx')







