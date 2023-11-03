import time
import requests

from bs4 import BeautifulSoup
from getLocation import getLocation

class info():
    def run(self, url, driver, station, id, dir, dirkor, line_number, destin):
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
                        if trainNo[:3] == '#K2' and line_number == 'gj':
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
                            print('----------')
                            print(f'{trainNo} ({dest}) {gwangmyeongText}{rapidText}{semiRapidText}{commuterRapidText}{gyeonguiRapidText}{jungangRapidText} 열차')
                            if getLocation.getDeparture(driver, trainNo) == station:
                                print(f'약 {estTime} 후에 {trainState} 예정 (시각표 기준)')
                                print(f'{getLocation.getDeparture(driver, trainNo)}역 대기 중\n')
                                x += 1
                                count += 1
                            elif noDelayInfo:
                                print(f'약 {estTime} 후에 {trainState} 예정 (시각표 기준)')
                                getLocation.process(driver, trainNo)
                                x += 1
                            else:
                                print(f'약 {estTime} 후에 {trainState} 예정')
                            if trainNo != '' and not noDelayInfo:
                                getLocation.process(driver, trainNo)
                                x += 1
                                count += 1
                            print('\n')
                        else:
                            x += 1
                    except:
                        deptStation = getLocation.getDeparture(driver, trainNo)
                        if deptStation == '지하서울역':
                            deptStation = '서울'
                        if deptStation == '지하청량리':
                            deptStation = '청량리'
                        print(f'{deptStation}역 대기 중\n')
                        x += 1
                except:
                    x += 1
            except:
                if x == 1:
                    print("현재 운행 중인 열차가 없습니다.")
                elif count == 0 and destin != "no행":
                    print(f'현재 운행 중인 {destin} 열차가 없습니다.')
                break
