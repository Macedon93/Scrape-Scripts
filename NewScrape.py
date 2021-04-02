# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 09:38:38 2021

@author: Steve
"""

import requests
from bs4 import BeautifulSoup   # install with 'pip install BeautifulSoup4'
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os # to get the resume file
import time # to sleep
import get_links


url = 'https://www.python.org/dev/peps/pep-0008/'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

# By inspecting the HTML in our browser, we find the introduction
# is contained in <div id='introduction'> ..... </div>
intro_div = soup.find(id='introduction')

print(intro_div.text)