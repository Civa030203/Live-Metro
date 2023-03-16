# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from IPython.display import clear_output
from pyvirtualdisplay import Display

from webdriver_manager.chrome import ChromeDriverManager
from select_line import select_line
from up_and_low import up_low_info
from getLocation import getLocation
from searchStationInfo import searchStationInfo

import requests
import time
import os
import traceback
import logging

class main:
    def start_options(url):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--single-process")
        chrome_options.add_argument("--disable-dev-shm-usage")
        display = Display(visible=0, size= (800, 600))
        display.start()
        driver = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)
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

    def info(self, url, driver, station, id, dir, dirkor, line_number, destin):
        if destin != "no행":
            print(f'{station}역의 {dirkor}선 {destin} 도착 정보', '\n')
        else:
            print(f'{station}역의 {dirkor}선 도착 정보', '\n')
        time.sleep(1)
        response = requests.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        x = 1
        count = 0
        while True:
            try:
                noDelayInfo = False
                rapidText = ''
                semiRapidText = ''
                commuterRapidText = ''
                gyeonguiRapidText = ''
                jungangRapidText = ''
                gwangmyeongText = ''
                trainNo = ''
                dest = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdDest.tdLine > span.spMetroTrainDestination > span').get_text()

                if dest == '광운대역':
                    dest = '광운대'
                if dest == '지하청량리':
                    dest = '청량리'
                if dest == '지하서울역':
                    dest = '서울역'
                if dest == '지하인천':
                    dest = '인천'
                if dest == '서울' and line_number == 'gj':
                    dest = '서울역'
                    gwangmyeongText = '4량 편성'
                if dest == station:
                    dest = '당역종착'
                elif dest in ['내선순환', '외선순환']:
                    pass
                else:
                    dest = dest + '행'

                if id == 'tdResultMetroAllStop': # 1호선, 경의중앙선, 수인분당선 등 코레일 관할 노선
                    try:
                        trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultMetroAllStop > span > a').get_text()
                        if trainNo[:3] == '#K2':
                            gwangmyeongText = '4량 편성'
                    except:
                        try:
                            trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultGwangmyeong > span > a').get_text()
                            gwangmyeongText = '4량 편성'
                        except:
                            try:
                                trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultRedRapid > span > a').get_text()
                                if trainNo[:3] == '#K2':
                                    gwangmyeongText = '4량 편성 '
                                rapidText = '급행'
                            except:
                                try:
                                    trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultCommuterRapid > span > a').get_text()
                                    commuterRapidText = '통근 급행'
                                except:
                                    try:
                                        trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultSemiRapid > span > a').get_text()
                                        semiRapidText = '준급행'
                                    except:
                                        try:
                                            trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultGyeonguiRapid > span > a').get_text()
                                            gyeonguiRapidText = '경의선 구간(문산 ~ 효창공원앞) 급행'
                                        except:
                                            try:
                                                trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultJungangRapid > span > a').get_text()
                                                jungangRapidText = '중앙선 구간(용산 ~ 용문) 급행'
                                            except:
                                                try:
                                                    trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultGreenRapid > span > a').get_text()
                                                    rapidText = '경부1선 급행'
                                                except:
                                                    pass
                elif id == 'tdResultSeoulMetro4':
                    try:
                        trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultSeoulMetro4 > span > a').get_text()
                    except:
                        try:
                            semiRapidText = '준급행'
                            trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultSemiRapid > span > a').get_text()
                        except:
                            pass
                elif id == 'tdResultMetro9':
                    try:
                        trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultMetro9 > span > a').get_text()
                    except:
                        rapidText = '급행'
                        trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultRedRapid > span > a').get_text()
                elif id == 'tdResultAREXCommuter':
                    try:
                        trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultAREXCommuter > span > a').get_text()
                    except:
                        rapidText = '직통'
                        trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.tdResultAREXExpress > span > a').get_text()
                else:
                    try:
                        trainNo = soup.select_one(f'#tblTrainList{dir} > tbody > tr:nth-child({x}) > td.tdTrainNo.tdLine.{id} > span > a').get_text()
                    except:
                        pass

                try:
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

                    if trainNo[1] in ['5', '6', '7', '8'] and id != 'tdResultSeoulMetro2':
                        trainNo = '#SMRT' + trainNo[1:5]
                    if id == 'tdResultSeoulMetro2':
                        trainNo = '#S' + trainNo[1:5]

                    try:
                        if destin == dest or destin == "no행":
                            print(f'{dest} (열차번호 : {trainNo}) {gwangmyeongText}{rapidText}{semiRapidText}{commuterRapidText}{gyeonguiRapidText}{jungangRapidText} 열차가 약 {estTime} 후에 {trainState}합니다.')
                            x += 1
                            count += 1
                            if getLocation.getDeparture(driver, trainNo) == station:
                                print('당역출발 열차의 경우 이전 열차의 지연 등으로 인하여 제대로 된 출발 시각 제공이 어려울 수 있습니다.')
                            elif noDelayInfo:
                                print('지연정보가 등록되지 않은 열차입니다. 시간표 기준으로 추정한 예상 시간이니 정확하지 않을 수 있습니다.')
                            if trainNo != '' and not noDelayInfo:
                                getLocation.process(driver, trainNo)
                            print('\n')
                        else:
                            x += 1
                    except:
                        x += 1
                except:
                    x += 1
            except:
                if x == 1:
                    print("현재 운행 중인 열차가 없습니다.")
                elif count == 0 and destin != "no행":
                    print(f'현재 운행 중인 {destin} 열차가 없습니다.')
                break

    sel = input('1. 실시간 지하철 도착 정보 조회\n2. 지하철 역 정보 조회(수도권 1, 2, 4호선 지원)\nexit. 프로그램 종료\n선택 : ')
    if sel == '1':
        while True:
            try:
                clear_output()
                os.system('clear')
            except:
                os.system('cls')
            url = "https://rail.blue/railroad/logis/metroarriveinfo.aspx"
            driver = start_options(url)
            id, line_number = select_line.process(driver)
            if id == 'exit':
                break
            os.system('clear')
            clear_output()
            station = input('역 이름을 입력해주세요. "exit" 입력 시 프로그램이 종료됩니다.\n')
            if station in ['서울', '서울역'] and line_number == '1':
                station = '지하서울역'
            elif station == '청량리' and line_number == '1':
                station = '지하청량리'
            elif station == '수원' and line_number == 'sub':
                station = '지하수원'
            elif station == '인천' and line_number == 'sub':
                station = '지하인천'
            elif station == '총신대입구':
                station = '이수'
            elif station == 'exit':
                break
            find_start(driver, station)
            find = driver.find_element(By.CSS_SELECTOR, '#btnSubmit')
            find.click()
            if line_number not in ["2", "8", "9", "sh", "gk", "dh", "ui", "sl", "ul", "ev"]:
                destin = input('찾으시는 행선지가 있으신가요? 없으실 경우 "no"를 입력해주세요.\n입력 : ')
                if destin == station:
                    destin = '당역종착'
                else:
                    destin = destin + '행'
            else:
                destin = 'no행'
            if id == 'tdResultSMRT6' and station in ['역촌', '불광', '독바위', '연신내', '구산']:
                info(info, url, driver, station, id, 'D', '응암순환', line_number, destin)
            else:
                ulinfo = up_low_info.process(id, line_number, station)
                direction = input(f'방향을 선택해주세요.\n1. 상행({ulinfo[0]} 방면)\n2. 하행({ulinfo[1]} 방면)\n선택 : ')
                if direction == '1':
                    info(info, url, driver, station, id, 'U', '상행', line_number, destin)
                elif direction == '2':
                    info(info, url, driver, station, id, 'D', '하행', line_number, destin)
            a = input('Press any key to continue\n')

    elif sel == '2':
        while True:
            sel = input("호선을 선택해주세요.\n1. 수도권 전철 1호선\n2. 서울 지하철 2호선\n3. 수도권 전철 3호선\n4. 수도권 전철 4호선\n")
            searchStationInfo.process(sel)
            a = input('Press any key to continue\n')
            if sel == 'exit':
                break
