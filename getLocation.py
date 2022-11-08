from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import localtime
import time

class getLocation():
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def process(trainNo):
        url = f'https://rail.blue/railroad/logis/Default.aspx?date={time.localtime().tm_year}{time.localtime().tm_mon}{time.localtime().tm_mday}&train={trainNo}#!'
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome("/Applications/chromedriver", options = options)
        driver.get(url)
