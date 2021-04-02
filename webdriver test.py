# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 12:02:42 2021

@author: Steve
"""
# testing for webdriver 
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = 'https://www.webscraper.io/test-sites/e-commerce/ajax/computers/laptops'

# Change argument to the location you installed the chrome driver
# (see selenium installation instructions, or get the driver for your
# system from https://sites.google.com/a/chromium.org/chromedriver/downloads)
driver = webdriver.Chrome(executable_path= r'C:\\ProgramData\\chocolatey\\bin\\chromedriver.exe')
driver.get(url)

# Give the javascript time to render
time.sleep(1)

# Now we have the page, let BeautifulSoup do the rest!
soup = BeautifulSoup(driver.page_source)

# The text containing title and price are in a
# div with class caption.
for caption in soup.find_all(class_='caption'):
    product_name = caption.find(class_='title').text
    price = caption.find(class_='pull-right price').text
    print(product_name, price)