# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from IPython.display import clear_output
import os
from select_line import select_line
from up_and_low import up_low_info

class main:
    def start_options(url):
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = webdriver.Chrome("/Applications/chromedriver", options = options)
        driver.get(url)
        return driver

    def find_start(driver, station):
        find_timetable = driver.find_element(By.CSS_SELECTOR, '#txtStation')
        find_timetable.send_keys(station)
        other_trains = driver.find_element(By.CSS_SELECTOR, '#chkTrainTypeETC')
        other_trains.click()
        new_window = driver.find_element(By.CSS_SELECTOR, '#chkNewWindow')
        #new_window.click()
        pass_train = driver.find_element(By.CSS_SELECTOR, '#chkSkip')
        #pass_train.click()

    def info(self, url, driver, station, id, dir, dirkor, line_number):
        print(f'{station}역의 {dirkor}행선 도착 정보', '\n')
        try:
            response = requests.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            if station in ['서울', '광명', '지평', '임진강']:
                trains = 2
            elif station in ['봉명', '쌍용', '아산', '탕정', '배방', '온양온천', '신창', '신내', '소요산', '용문']:
                trains = 3
            else:
                trains = 4
            for x in range(1, trains):
                noDelayInfo = False
                isRapid = False
                isGwangmyeong = False
                dest = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdDest.tdLine > span.spMetroTrainDestination > span').get_text()
                if dest == '광운대역':
                    dest = '광운대'
                if dest == '지하청량리':
                    dest = '청량리'
                if dest == '지하서울역':
                    dest = '서울역'
                if id == 'tdResultMetroAllStop':
                    try:
                        trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultMetroAllStop > span > a').get_text()
                    except:
                        try:
                            trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultGwangmyeong > span > a').get_text()
                            isGwangmyeong = True
                        except:
                            isRapid = True
                            try:
                                trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultSemiRapid > span > a').get_text()
                            except:
                                try:
                                    trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultRedRapid > span > a').get_text()
                                except:
                                    try:
                                        trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultCommuterRapid > span > a').get_text()
                                    except:
                                        try:
                                            trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultGreenRapid > span > a').get_text()
                                        except:
                                            try:
                                                trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultGyeonguiRapid > span > a').get_text()
                                            except:
                                                trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultJungangRapid > span > a').get_text()
                elif id == 'tdResultSeoulMetro4':
                    try:
                        trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultSeoulMetro4 > span > a').get_text()
                    except:
                        try:
                            isRapid = True
                            trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultSemiRapid > span > a').get_text()
                        except:
                            x += 1
                elif id == 'tdResultMetro9':
                    try:
                        trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultMetro9 > span > a').get_text()
                    except:
                        isRapid = True
                        trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultRedRapid > span > a').get_text()
                else:
                    trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.{id} > span > a').get_text()
                if trainNo[5] in ['도', '출', '종']:
                    trainState = trainNo[5:7]
                    trainNo = trainNo[:5]
                elif trainNo[4] in ['도', '출', '종']:
                    trainState = trainNo[4:6]
                    trainNo = trainNo[:4]
                elif trainNo[3] in ['도', '출', '종']:
                    trainState = trainNo[3:5]
                    trainNo = trainNo[:3]
                elif trainNo[2] in ['도', '출', '종']:
                    trainState = trainNo[2:4]
                    trainNo = trainNo[:2]
                else:
                    trainState = trainNo[6:]
                    trainNo = trainNo[:6]
                try:
                    estTime = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdDest.tdLine > span.spMetroArriveDelayApply').get_text()
                except:
                    estTime = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdDest.tdLine > span.spMetroArriveDelayNone').get_text()
                    noDelayInfo = True

                if trainNo[1] in ['5', '6', '7', '8']:
                    trainNo = '#SMRT' + trainNo[1:5]
                if id == 'tdResultSeoulMetro2':
                    trainNo = '#S' + trainNo[1:5]
                if dest != station and not isRapid and not isGwangmyeong:
                    print(f'{dest}행 (열차번호 : {trainNo}) 열차가 약 {estTime} 후에 {trainState}합니다.')
                elif dest != station and isRapid and not isGwangmyeong:
                    print(f'{dest}행 (열차번호 : {trainNo}) 급행 열차가 약 {estTime} 후에 {trainState}합니다.')
                elif dest != station and not isRapid and isGwangmyeong:
                    print(f'{dest}행 (열차번호 : {trainNo}) 4량 편성 열차가 약 {estTime} 후에 {trainState}합니다.')
                else:
                    print(f'당역종착 (열차번호 : {trainNo}) 열차가 약 {estTime} 후에 도착합니다.')
                if noDelayInfo and trainState != '출발':
                    print('지연정보가 등록되지 않은 열차입니다. 시간표 기준으로 제공된 예상 시간이며 정확하지 않을 수 있으니 참고하시기 바랍니다.')
                elif noDelayInfo and trainState == '출발':
                    print('당역출발 열차의 경우 앞선 열차의 지연과 같은 이유 등으로 시간이 정확하지 않을 수 있으니 참고하시기 바랍니다.')
        except:
            print('운행 중인 열차가 없거나 데이터를 가져오는 중 오류가 발생하여 다시 시도합니다.')
            time.sleep(1)
            os.system('clear')
            clear_output()
            self(self, url, driver, station, id, dir, dirkor, line_number)

    clear_output()
    os.system('clear')
    url = "https://rail.blue/railroad/logis/metroarriveinfo.aspx"
    driver = start_options(url)
    id, line_number = select_line.process(driver)
    os.system('clear')
    clear_output()
    print(line_number)
    station = input('역 이름을 입력해주세요. ')
    find_start(driver, station)
    find = driver.find_element(By.CSS_SELECTOR, '#btnSubmit')
    find.click()
    ulinfo = up_low_info.process(id, line_number)
    direction = input(f'방향을 선택해주세요.\n1. 상행({ulinfo[0]} 방면)\n2. 하행({ulinfo[1]} 방면)\n선택 : ')
    if direction == '1':
        info(info, url, driver, station, id, 'U', '상', line_number)
    elif direction == '2':
        info(info, url, driver, station, id, 'D', '하', line_number)
