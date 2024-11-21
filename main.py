# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-
# 코드가 너무 더럽다아아아,,,

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from IPython.display import clear_output
from pyvirtualdisplay import Display

from webdriver_manager.chrome import ChromeDriverManager
from select_line import select_line
from up_and_low import up_low_info
from getLocation import getLocation
from get_destin import get_destin
from initProcess import *
from info import *

import requests
import time
import os
import traceback
import logging

def clearScreen():
    try:
        clear_output()
        os.system('clear')
    except:
        os.system('cls')

def searchStationName():
    sta = input('역 이름을 입력해주세요. "exit" 입력 시 프로그램이 종료됩니다.\n')
    if sta in ['서울', '서울역'] and line_number in ['1', '4']:
        station = '지하서울역'
    elif sta == '청량리' and line_number == '1':
        station = '지하청량리'
    elif sta == '수원' and line_number == 'sub':
        station = '지하수원'
    elif sta == '인천' and line_number == 'sub':
        station = '지하인천'
    elif sta == '총신대입구':
        station = '이수'
    elif sta == '서울역' and line_number in ['gj', 'arex']:
        station = "서울"
    elif sta == '당고개':
        station = '불암산'
    else:
        station = sta
    return station

class main:
    while True:
        sel = input('1. 실시간 지하철 도착 정보 조회\nexit. 프로그램 종료\n선택 : ')
        if sel == '1':
            while True: # 반복문 돌려서 프로그램 실행
                clearScreen()
                print("정보 제공 사이트에 연결 중입니다... 잠시만 기다려 주세요.")
                driver = initProcess.start_options()
                clearScreen()
                id, line_number = select_line.process(driver)
                if id == 'exit':
                    clearScreen()
                    break
                clearScreen()
                station = searchStationName()
                if station == 'exit':
                    break
                initProcess.find_start(driver, station)
                find = driver.find_element(By.CSS_SELECTOR, '#btnSubmit')
                find.click()

                if line_number not in ["2", "8", "9", "gk", "dh", "ui", "sl", "ul", "ev"]:
                    destin = input('찾으시는 행선지가 있으신가요? 없으실 경우 빈 칸으로 두고 엔터를 눌러주세요.\n입력 : ')
                    if destin == station:
                        destin = '당역종착'
                    elif destin == '':
                        destin = 'no행'
                    else:
                        destin = destin + '행'
                else:
                    destin = 'no행'
                dirt = get_destin.run(station, line_number, destin)

                if id == 'tdResultSMRT6' and station in ['역촌', '불광', '독바위', '연신내', '구산']: # 응암순환 구간 예외처리
                    info.run(info, driver, station, id, 'D', '응암순환', line_number, 'no행')
                else:
                    ulinfo = up_low_info.process(id, line_number, station)
                    if dirt == None:
                        direction = input(f'방향을 선택해주세요.\n1. 상행({ulinfo[0]} 방면)\n2. 하행({ulinfo[1]} 방면)\n선택 : ')
                    else:
                        direction = dirt
                    if direction == '1':
                        info.run(info, driver, station, id, 'U', '상행', line_number, destin)
                    elif direction == '2':
                        info.run(info, driver, station, id, 'D', '하행', line_number, destin)

                a = input('Press enter key to continue\n')


        elif sel == 'exit':
            break

        else:
            try:
                clear_output()
                os.system('clear')
            except:
                os.system('cls')
            print("잘못된 입력입니다! 다시 입력해 주세요.")
