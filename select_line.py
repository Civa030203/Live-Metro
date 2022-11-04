# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

class select_line():
    def __init__(self, driver):
        self.driver = driver
        self.line = 0

    def process(self):
        self.line = input('정보를 조회할 역은 무슨 노선인가요?\n참고 : 서울 지하철 5 ~ 8호선 간 환승역의 경우(예 : 공덕역) 계속 오류가 발생한다면, 다른 노선(공덕역의 경우 5호선 오류 발생 시 6호선으로)으로 변경 후 재검색해보세요.\n1. 수도권 전철 1호선\n2. 서울 지하철 2호선\n3. 수도권 전철 3호선\n4. 수도권 전철 4호선\n5. 수도권 전철 5호선\n6. 서울 지하철 6호선\n7. 서울 지하철 7호선\n8. 서울 지하철 8호선\n9. 서울 지하철 9호선\ngj. 수도권 전철 경의중앙선\nsub. 수도권 전철 수인분당선\nkc. 수도권 전철 경춘선\nsh. 수도권 전철 서해선\ngk. 수도권 전철 경강선\ndh. 동해선 광역철도\nsb. 수도권 전철 신분당선\nui. 서울 경전철 우이신설선\nsl. 서울 경전철 신림선\ngl. 김포 골드라인\nul. 의정부 경전철\nev. 용인 에버라인\nicn1. 인천 지하철 1호선\nicn2. 인천 지하철 2호선\narex. 공항철도\n선택 : ')
        if self.line in ['1', 'gj', 'sub', 'kc', 'sh', 'gk', 'dh']:
            lines = self.find_element(By.CSS_SELECTOR, "#cmbDir > option:nth-child(3)")
            lines.click()
            line_identifier = 'tdResultMetroAllStop'
        elif self.line == '2':
            lines = self.find_element(By.CSS_SELECTOR, "#cmbDir > option:nth-child(4)")
            lines.click()
            line_identifier = 'tdResultSeoulMetro2'
        elif self.line == '3':
            lines = self.find_element(By.CSS_SELECTOR, "#cmbDir > option:nth-child(5)")
            lines.click()
            line_identifier = 'tdResultSeoulMetro3'
        elif self.line == '4':
            lines = self.find_element(By.CSS_SELECTOR, "#cmbDir > option:nth-child(6)")
            lines.click()
            line_identifier = 'tdResultSeoulMetro4'
        elif self.line in ['5', '6', '7', '8']:
            lines = self.find_element(By.CSS_SELECTOR, "#cmbDir > option:nth-child(7)")
            lines.click()
            if self.line == '5':
                line_identifier = 'tdResultSMRT5'
            elif self.line == '6':
                line_identifier = 'tdResultSMRT6'
            elif self.line == '7':
                line_identifier = 'tdResultSMRT7'
            elif self.line == '8':
                line_identifier = 'tdResultSMRT8'
        elif self.line == '9':
            lines = self.find_element(By.CSS_SELECTOR, "#cmbDir > option:nth-child(8)")
            lines.click()
            line_identifier = 'tdResultMetro9'
        elif self.line == 'sb':
            lines = self.find_element(By.CSS_SELECTOR, "#cmbDir > option:nth-child(9)")
            lines.click()
            line_identifier = 'tdResultDX'
        elif self.line == 'ui':
            lines = self.find_element(By.CSS_SELECTOR, "#cmbDir > option:nth-child(10)")
            lines.click()
            line_identifier = 'tdResultUI'
        elif self.line == 'sl':
            lines = self.find_element(By.CSS_SELECTOR, "#cmbDir > option:nth-child(11)")
            lines.click()
            line_identifier = 'tdResultSL'
        elif self.line == 'gl':
            lines = self.find_element(By.CSS_SELECTOR, "#cmbDir > option:nth-child(12)")
            lines.click()
            line_identifier = 'tdResultGMP'
        elif self.line == 'ul':
            lines = self.find_element(By.CSS_SELECTOR, "#cmbDir > option:nth-child(13)")
            lines.click()
            line_identifier = 'tdResultULRT'
        elif self.line == 'ev':
            lines = self.find_element(By.CSS_SELECTOR, "#cmbDir > option:nth-child(14)")
            lines.click()
            line_identifier = 'tdResultEVER'
        elif self.line in ['icn1', 'icn2']:
            lines = self.find_element(By.CSS_SELECTOR, "#cmbDir > option:nth-child(15)")
            lines.click()
            if self.line == 'icn1':
                line_identifier = 'tdResultIncheonMetro1'
            elif self.line == 'icn2':
                line_identifier = 'tdResultIncheonMetro2'
        elif self.line == 'arex':
            lines = self.find_element(By.CSS_SELECTOR, "#cmbDir > option:nth-child(2)")
            lines.click()
        return line_identifier, self.line
