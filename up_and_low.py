# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

class up_low_info():
    def __init__(self, id, line_number):
        self.id = id
        self.line_number = line_number

    def process(self, line_number):
        up_and_low = []
        if line_number == '1':
            up_and_low.append('소요산, 양주, 광운대, 청량리')
            up_and_low.append('인천, 천안, 서동탄, 신창')
        elif line_number == 'gj':
            up_and_low.append('문산, 용산')
            up_and_low.append('청량리, 덕소, 팔당, 용문, 지평')
        elif line_number == 'sub':
            up_and_low.append('청량리 / 왕십리 / 오이도(수인선 구간 한정)')
            up_and_low.append('죽전 / 고색 / 오이도(분당선 구간 한정) / 인천')
        elif line_number == 'kc':
            up_and_low.append('청량리 / 상봉 / 광운대')
            up_and_low.append('평내호평 / 마석 / 춘천')
        elif line_number == 'sh':
            up_and_low.append('소사')
            up_and_low.append('원시')
        elif line_number == 'gk':
            up_and_low.append('판교')
            up_and_low.append('여주')
        elif line_number == 'dh':
            up_and_low.append('부전')
            up_and_low.append('태화강')
        elif self == 'tdResultSeoulMetro2':
            up_and_low.append('내선순환 / 신설동(성수지선) / 신도림(신정지선)')
            up_and_low.append('외선순환 / 성수(성수지선) / 까치산(신정지선)')
        elif self == 'tdResultSeoulMetro3':
            up_and_low.append('대화 / 구파발')
            up_and_low.append('수서 / 오금')
        elif self == 'tdResultSeoulMetro4':
            up_and_low.append('진접 / 당고개')
            up_and_low.append('사당 / 오이도')
        elif self == 'tdResultSMRT5':
            up_and_low.append('방화')
            up_and_low.append('상일동 / 하남검단산 / 마천')
        elif self == 'tdResultSMRT6':
            up_and_low.append('응암')
            up_and_low.append('봉화산 / 신내')
        elif self == 'tdResultSMRT7':
            up_and_low.append('장암 / 도봉산')
            up_and_low.append('온수 / 석남')
        elif self == 'tdResultSMRT8':
            up_and_low.append('암사')
            up_and_low.append('모란')
        elif self == 'tdResultMetro9':
            up_and_low.append('중앙보훈병원')
            up_and_low.append('개화')
        elif self == 'tdResultDX':
            up_and_low.append('신사')
            up_and_low.append('광교')
        elif self == 'tdResultUI':
            up_and_low.append('신설동')
            up_and_low.append('북한산우이')
        elif self == 'tdResultSL':
            up_and_low.append('샛강')
            up_and_low.append('관악산')
        elif self == 'tdResultGMP':
            up_and_low.append('구래 / 양촌')
            up_and_low.append('김포공항')
        elif self == 'tdResultULRT':
            up_and_low.append('발곡')
            up_and_low.append('탑석 / 차량기지임시승강장')
        elif self == 'tdResultEVER':
            up_and_low.append('기흥')
            up_and_low.append('전대(에버랜드)')
        elif self == 'tdResultIncheonMetro1':
            up_and_low.append('계양')
            up_and_low.append('송도달빛축제공원')
        elif self == 'tdResultIncheonMetro2':
            up_and_low.append('검단오류')
            up_and_low.append('운연')
        return up_and_low
