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
        if trainNo[1:5] == 'SMRT': # 서울도시철도(5~8호선)
            company.send_keys(trainNo[1:5])
        elif trainNo[1] == 'C': # 9호선 일반
            company.send_keys("SNC")
        elif trainNo[1] == 'E': # 9호선 급행
            company.send_keys("SNE")
        else:
            company.send_keys(trainNo[1])

        train_No = driver.find_element(By.CSS_SELECTOR, '#txtTrainNumber')
        if trainNo[1:5] == 'SMRT':
            train_No.send_keys(trainNo[5:])
        elif trainNo[1] == 'C':
            train_No.send_keys(trainNo[2:])
        elif trainNo[1] == 'E':
            train_No.send_keys(trainNo[2:])
        else:
            train_No.send_keys(trainNo[2:])
        find = driver.find_element(By.CSS_SELECTOR, '#btnDefault')
        find.click()

        response = requests.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        try:
            trainDelay = soup.select_one('#spDrive > span').get_text()
            if trainDelay == "운행중":
                trainDelay = "지연 정보 확인 안 됨"
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

        if trainLocation == '덕계' and trainLocation2 == '마전':
            trainLocation2 = '양주'
        if trainLocation == '마전' and trainLocation2 == '덕계':
            trainLocation = '양주'
        if trainLocation == '양주' and trainLocation2 == '마전':
            trainLocation2 == '덕계'
        if trainLocation == '마전' and trainLocation2 == '양주':
            trainLocation = '덕계'

        if trainLocation2 == '':
            print(f'{trainLocation}역 도착, {trainDelay}')
        else:
            print(f'{trainLocation}역 - {trainLocation2}역, {trainDelay}')

    def getDeparture(driver, trainNo):
        url = 'https://rail.blue/railroad/logis/timetable.aspx'
        driver.get(url)
        company = driver.find_element(By.CSS_SELECTOR, '#txtTrainNo')
        if trainNo[1:5] == 'SMRT':
            company.send_keys(trainNo[1:5])
        elif trainNo[1] == 'C':
            company.send_keys("SNC")
        elif trainNo[1] == 'E':
            company.send_keys("SNE")
        else:
            company.send_keys(trainNo[1])
        train_No = driver.find_element(By.CSS_SELECTOR, '#txtTrainNumber')
        if trainNo[1:5] == 'SMRT':
            train_No.send_keys(trainNo[5:])
        elif trainNo[1] == 'C':
            train_No.send_keys(trainNo[2:])
        elif trainNo[1] == 'E':
            train_No.send_keys(trainNo[2:])
        else:
            train_No.send_keys(trainNo[2:])
        find = driver.find_element(By.CSS_SELECTOR, '#btnDefault')
        find.click()

        response = requests.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        departureStation = soup.select_one(f'#spDept > b > span > a').get_text()
        return departureStation
