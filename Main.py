from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from selenium.webdriver.common.by import By


driver =  webdriver.Chrome()
driver.get("https://www.mercadolibre.com.co/")
search_bar = driver.find_element(By.CLASS_NAME, "nav-search-input")
search_bar.clear()
search_bar.send_keys("iphone12")
search_bar.send_keys(Keys.RETURN)

pagination = driver.find_element(By.XPATH,"//li[@class='andes-pagination__page-count']").text
pagination = [ int(s) for s in pagination.split() if s.isdigit()][0]

records = []

for product in range(1,pagination+1):
    if product != pagination:
        next_page_button = driver.find_element(By.CSS_SELECTOR, "a[title='Siguiente']")

    title_products = driver.find_elements(By.XPATH, "//h2[@class='ui-search-item__title shops__item-title']")
    title_products = [     title.text  for title in title_products            ]


    try:
        price_products = driver.find_elements(By.XPATH, "//div[@class='ui-search-result__content-columns shops__content-columns']//div[@class='ui-search-result__content-column ui-search-result__content-column--left shops__content-columns-left']/div[1]/div//div[@class='ui-search-price__second-line shops__price-second-line']//span[@class='andes-money-amount ui-search-price__part shops__price-part ui-search-price__part--medium andes-money-amount--cents-superscript']//span[@class='andes-money-amount__fraction']")
        price_products = [ price.text for price in price_products ]
    except:
        price_products = ['0']


    links_products = driver.find_elements(By.XPATH, "//div[@class='andes-carousel-snapped__slide andes-carousel-snapped__slide--active']//a[1]")
    links_products = [ link.get_attribute("href") for link in links_products   ]


    data_products = {

        "name_product":title_products,
        "price_product":price_products,
        "link_product":links_products

    }

    print(len(title_products))
    print(len(price_products))
    print(len(links_products))
    df =  pd.DataFrame(data_products)
    print(product)
    print(pagination)
    records.append(df)
    if product != pagination:
        driver.execute_script("arguments[0].click()", next_page_button)

df = pd.concat(records)
df.to_csv("PRODUCTOS.csv")
time.sleep(2)
driver.close()