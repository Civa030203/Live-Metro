from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import localtime
import time

class getLocation():
    def __init__(self, driver, trainNo):
        self.driver = driver
        self.trainNo = trainNo

    def process(driver, trainNo):
        url = 'https://rail.blue/railroad/logis/timetable.aspx'
        driver.get(url)
        company = driver.find_element(By.CSS_SELECTOR, '#txtTrainNo')
        if trainNo[1:5] == 'SMRT':
            company.send_keys(trainNo[1:5])
        else:
            company.send_keys(trainNo[1])
        train_No = driver.find_element(By.CSS_SELECTOR, '#txtTrainNumber')
        if trainNo[1:5] == 'SMRT':
            train_No.send_keys(trainNo[5:])
        else:
            train_No.send_keys(trainNo[2:])
        find = driver.find_element(By.CSS_SELECTOR, '#btnDefault')
        find.click()

        response = requests.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        try:
            trainDelay = soup.select_one('#spDrive > span').get_text()
        except:
            trainDelay = '지연 상태가 확인 안됨'

        trainLocation = soup.select_one('#spDrive > b > span > a').get_text()

        try:
            trainLocation2 = soup.select_one('#spDrive > b:nth-child(2) > span > a').get_text()
        except:
            trainLocation2 = ''

        if trainLocation == '지하서울역':
            trainLocation = '서울'
        if trainLocation == '지하청량리':
            trainLocation = '청량리'

        if trainLocation2 == '지하서울역':
            trainLocation2 = '서울'
        if trainLocation2 == '지하청량리':
            trainLocation2 = '청량리'

        if trainLocation2 == '':
            print(f'{trainLocation}역에 열차가 도착하였으며, {trainDelay}입니다.')
        else:
            print(f'{trainLocation}역과 {trainLocation2}역 사이를 운행 중이며, {trainDelay}입니다.')
