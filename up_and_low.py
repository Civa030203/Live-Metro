# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

class up_low_info():
    def __init__(self, id, line_number):
        self.id = id
        self.line_number = line_number

    def process(self, line_number, station):
        up_and_low = []
        if line_number == '1':
            if station in ['연천', '전곡', '청산']:
                up_and_low.append('연천')
                up_and_low.append('인천 / 광운대')
            elif station in ['소요산', '동두천', '보산', '동두천중앙', '지행', '덕정', '덕계']: # 경원선 소요산 ~ 덕계 구간
                up_and_low.append('연천 / 동두천(소요산)')
                up_and_low.append('인천 / 광운대')
            elif station in ['양주', '녹양', '가능', '의정부', '회룡', '망월사', '도봉산', '도봉', '방학', '창동', '녹천', '월계']: # 경원선 양주 ~ 월계 구간
                up_and_low.append('연천 / 동두천(소요산) / 의정부(양주)')
                up_and_low.append('인천 / 광운대')
            elif station in ['광운대', '석계', '신이문', '외대앞', '회기']: # 경원선 광운대 ~ 회기 구간
                up_and_low.append('연천 / 동두천(소요산) / 의정부(양주) / 광운대')
                up_and_low.append('인천 / 서동탄 / 천안(신창)')
            elif station in ['지하청량리', '제기동', '신설동', '동묘앞', '동대문', '종로5가', '종로3가', '종각', '시청', '지하서울역', '남영']: # 서울 지하철 1호선 + 남영역
                up_and_low.append('연천 / 동두천(소요산) / 의정부(양주) / 청량리(광운대)')
                up_and_low.append('인천 / 서동탄 / 천안(신창)')
            elif station in ['용산', '노량진', '대방', '신길', '영등포', '신도림', '구로']: # 경부선 용산 + 구로 구간
                up_and_low.append('연천 / 동두천(소요산) / 의정부(양주) / 청량리(광운대) / 용산(급행)')
                up_and_low.append('인천(동인천급행) / 서동탄(병점) / 천안(신창)')
            elif station in ['구일', '오류동', '온수', '소사', '중동', '부개', '백운', '간석', '도화', '도원']: # 경인선 급행 미정차역 구간
                up_and_low.append('연천 / 동두천(소요산) / 의정부(양주)')
                up_and_low.append('인천')
            elif station in ['개봉', '역곡', '부천', '송내', '부평', '동암', '주안', '제물포']: # 경인선 급행 정차역 구간
                up_and_low.append('연천 / 동두천(소요산) / 의정부(양주) / 용산(급행)')
                up_and_low.append('인천(동인천급행)')
            elif station in ['동인천', '인천']: # 경인선 급행 없는 구간
                up_and_low.append('연천 / 동두천(소요산) / 의정부(양주) / 용산(급행)')
                up_and_low.append('인천')
            elif station in ['가산디지털단지', '금정', '의왕']: # 경부선 가산디지털단지 ~ 병점 급행 정차역 구간
                up_and_low.append('청량리(광운대)')
                up_and_low.append('서동탄(병점) / 천안(신창)')
            elif station in ['금천구청', '안양', '군포', '성균관대', '수원']: # 경부선 금천구청 ~ 수원 초록급행 정차역
                up_and_low.append('청량리(광운대) / 서울역(급행)')
                up_and_low.append('서동탄(병점) / 천안(신창)')
            elif station == '병점':
                up_and_low.append('청량리(광운대) / 서울역(급행)')
                up_and_low.append('서동탄 / 천안(신창)')
            elif station == '서동탄':
                up_and_low.append('청량리(광운대)')
                up_and_low.append('서동탄')
            elif station in ['오산', '서정리', '평택', '성환', '두정', '천안']: # 경부선 세마 ~ 천안 초록급행 정차역
                up_and_low.append('청량리(광운대) / 서울역(급행)')
                up_and_low.append('천안(신창)')
            elif station in ['세마', '오산대', '진위', '송탄', '평택지제', '직산']: # 경부선 세마 ~ 천안 급행 통과역
                up_and_low.append('청량리(광운대)')
                up_and_low.append('천안(신창)')
            elif station == '광명': # 경부고속선 광명역
                up_and_low.append('영등포')
                up_and_low.append('광명')
            else: # 장항선 봉명 ~ 신창 구간
                up_and_low.append('청량리(광운대)')
                up_and_low.append('신창')

        elif line_number == 'gj':
            if station == '도라산': # 경의선 도라산 셔틀 구간
                up_and_low.append('도라산')
                up_and_low.append('임진강')
            elif station in ['임진강', '운천']: # 경의선 임진강 ~ 운천 별도 운행계통 구간
                up_and_low.append('임진강 / 도라산')
                up_and_low.append('문산')
            elif station == '문산': # 경의선 문산역
                up_and_low.append('임진강 / 문산')
                up_and_low.append('용문(지평) / 덕소(팔당) / 청량리(용산) / 서울역')
            elif station in ['파주', '월롱', '금촌', '금릉', '운정', '야당', '탄현', '일산', '풍산', '백마', '곡산']: # 경의선 파주 ~ 곡산 구간
                up_and_low.append('문산')
                up_and_low.append('용문(지평) / 덕소(팔당) / 청량리(용산) / 서울역')
            elif station in ['대곡', '능곡', '행신', '강매', '화전', '수색', '디지털미디어시티', '가좌']: # 경의선 대곡 ~ 가좌 구간
                up_and_low.append('문산 / 대곡')
                up_and_low.append('용문(지평) / 덕소(팔당) / 청량리(용산) / 서울역')
            elif station in ['신촌', '서울']: # 경의선 신촌 ~ 서울 구간
                up_and_low.append('문산 / 대곡')
                up_and_low.append('서울역')
            elif station in ['홍대입구', '서강대', '공덕', '효창공원앞']: # 용산/효창선 구간
                up_and_low.append('문산')
                up_and_low.append('용문(지평) / 덕소(팔당) / 청량리(용산)')
            elif station == '용산':
                up_and_low.append('문산 / 용산')
                up_and_low.append('용문(지평) / 덕소(팔당) / 청량리(용산)')
            elif station in ['이촌', '서빙고', '한남', '옥수', '응봉', '왕십리', '청량리']: # 경원선 이촌 ~ 청량리 구간
                up_and_low.append('문산 / 용산')
                up_and_low.append('용문(지평) / 덕소(팔당) / 청량리')
            elif station in ['회기', '중랑', '상봉', '망우', '양원', '구리', '도농', '양정', '덕소']: # 중앙선 회기 ~ 덕소 구간
                up_and_low.append('문산 / 용산(청량리)')
                up_and_low.append('용문(지평) / 덕소(팔당)')
            elif station in ['도심', '팔당']: # 중앙선 도심, 팔당역
                up_and_low.append('문산 / 용산(청량리)')
                up_and_low.append('용문(지평) / 팔당')
            elif station in ['운길산', '신원', '양수', '국수', '아신', '오빈', '양평', '원덕', '용문']: # 중앙선 운길산 ~ 용문 구간
                up_and_low.append('문산 / 용산(청량리)')
                up_and_low.append('용문(지평)')
            elif station == '지평': # 중앙선 지평역
                up_and_low.append('문산 / 용산(청량리)')
                up_and_low.append('지평')

        elif line_number == 'sub':
            if station == '청량리': # 경원선 청량리역
                up_and_low.append('청량리')
                up_and_low.append('죽전 / 고색 / 인천')
            elif station in ['왕십리', '서울숲', '압구정로데오', '강남구청', '선정릉', '선릉', '한티', '도곡', '구룡', '개포동', '대모산입구', '수서', '복정', '가천대', '태평', '모란', '야탑', '이매', '서현', '수내', '정자', '미금', '오리', '죽전']: # 분당선 왕십리 ~ 죽전 구간
                up_and_low.append('왕십리(청량리)')
                up_and_low.append('죽전 / 고색 / 인천')
            elif station == '죽전': # 분당선 죽전역
                up_and_low.append('왕십리(청량리) / 죽전')
                up_and_low.append('죽전 / 고색 / 인천')
            elif station in ['보정', '구성', '신갈', '기흥', '상갈', '청명', '영통', '망포', '매탄권선', '수원시청', '매교', '지하수원', '고색']: # 분당선 보정 ~ 고색 구간
                up_and_low.append('왕십리(청량리) / 죽전')
                up_and_low.append('고색 / 인천')
            elif station in ['오목천', '어천', '야목', '사리', '한대앞', '중앙', '고잔', '초지', '안산', '신길온천', '정왕']: # 수인선 오목천 ~ 사리 구간 및 안산선 공용 구간
                up_and_low.append('왕십리(청량리) / 죽전')
                up_and_low.append('인천')
            else: # 수인선 오이도 ~ 인천 구간
                up_and_low.append('왕십리(청량리) / 죽전 / 오이도')
                up_and_low.append('인천')

        elif line_number == 'kc':
            if station in ['청량리', '회기', '중랑']: # 중앙선 공용구간
                up_and_low.append('청량리')
                up_and_low.append('춘천(평내호평)')
            elif station in ['상봉', '망우', '신내', '갈매', '별내', '퇴계원', '사릉', '금곡', '평내호평']:
                up_and_low.append('상봉(청량리 / 광운대)')
                up_and_low.append('춘천(평내호평)')
            elif station == '광운대':
                up_and_low.append('광운대')
                up_and_low.append('춘천')
            else:
                up_and_low.append('상봉(청량리 / 광운대)')
                up_and_low.append('춘천')

        elif line_number == 'sh':
            if station in ['곡산', '백마', '풍산', '일산']: # 경의선 공용구간
                up_and_low.append('일산')
                up_and_low.append('원시')
            else:
                up_and_low.append('대곡(일산)')
                up_and_low.append('원시')

        elif line_number == 'gk':
            up_and_low.append('판교')
            up_and_low.append('여주')
        elif line_number == 'dh':
            up_and_low.append('부전')
            up_and_low.append('태화강')

        elif self == 'tdResultSeoulMetro2':
            if station in ['용답', '신답', '용두', '신설동']:
                up_and_low.append('신설동')
                up_and_low.append('성수')
            elif station in ['도림천', '양천구청', '신정네거리', '까치산']:
                up_and_low.append('신도림')
                up_and_low.append('까치산')
            elif station == '시청':
                up_and_low.append('내선순환(을지로)')
                up_and_low.append('외선순환(신촌)')
            elif station in ['을지로입구', '을지로3가', '을지로4가']:
                up_and_low.append('내선순환(왕십리)')
                up_and_low.append('외선순환(시청)')
            elif station in ['동대문역사문화공원', '신당', '상왕십리']:
                up_and_low.append('내선순환(왕십리)')
                up_and_low.append('외선순환(을지로)')
            elif station == '왕십리':
                up_and_low.append('내선순환(성수)')
                up_and_low.append('외선순환(을지로)')
            elif station in ['한양대', '뚝섬']:
                up_and_low.append('내선순환(성수)')
                up_and_low.append('외선순환(왕십리)')
            elif station == '성수':
                up_and_low.append('내선순환(잠실) / 신설동')
                up_and_low.append('외선순환(왕십리) / 성수')
            elif station in ['건대입구', '구의', '강변', '잠실나루']:
                up_and_low.append('내선순환(잠실)')
                up_and_low.append('외선순환(성수)')
            elif station == '잠실':
                up_and_low.append('내선순환(강남)')
                up_and_low.append('외선순환(성수)')
            elif station in ['잠실새내', '종합운동장', '삼성', '선릉', '역삼']:
                up_and_low.append('내선순환(강남)')
                up_and_low.append('외선순환(잠실)')
            elif station == '강남':
                up_and_low.append('내선순환(사당)')
                up_and_low.append('외선순환(잠실)')
            elif station in ['교대', '서초', '방배']:
                up_and_low.append('내선순환(사당)')
                up_and_low.append('외선순환(강남)')
            elif station == '사당':
                up_and_low.append('내선순환(신도림)')
                up_and_low.append('외선순환(강남)')
            elif station in ['낙성대', '서울대입구', '봉천', '신림', '신대방', '구로디지털단지', '대림']:
                up_and_low.append('내선순환(신도림)')
                up_and_low.append('외선순환(사당)')
            elif station == '신도림':
                up_and_low.append('내선순환(신촌) / 신도림')
                up_and_low.append('외선순환(사당) / 까치산')
            elif station in ['문래', '영등포구청', '당산', '합정', '홍대입구']:
                up_and_low.append('내선순환(신촌)')
                up_and_low.append('외선순환(신도림)')
            elif station == '신촌':
                up_and_low.append('내선순환(을지로)')
                up_and_low.append('외선순환(신도림)')
            elif station in ['이대', '아현', '충정로']:
                up_and_low.append('내선순환(을지로)')
                up_and_low.append('외선순환(신촌)')

        elif self == 'tdResultSeoulMetro3':
            if station in ['대화', '주엽', '정발산', '마두', '백석', '대곡', '화정', '원당', '원흥', '삼송']: # 일산선 구간
                up_and_low.append('대화')
                up_and_low.append('삼송 / 오금(수서)')
            elif station == '지축': # 일산선 / 서울 지하철 3호선 지축역
                up_and_low.append('대화')
                up_and_low.append('오금(수서)')
            elif station in ['가락시장', '경찰병원', '오금']: # 서울 지하철 3호선 오금연장 구간
                up_and_low.append('대화 / 구파발')
                up_and_low.append('오금')
            else: # 서울 지하철 3호선
                up_and_low.append('대화 / 구파발')
                up_and_low.append('오금(수서)')

        elif self == 'tdResultSeoulMetro4':
            if station in ['진접', '오남', '별내별가람']: # 진접선 구간
                up_and_low.append('진접')
                up_and_low.append('사당')
            elif station in ['당고개', '상계', '노원', '창동', '쌍문', '수유', '미아', '미아사거리', '길음', '성신여대입구', '한성대입구', '혜화', '동대문', '동대문역사문화공원', '충무로', '명동', '회현', '지하서울역', '숙대입구', '삼각지', '신용산', '이촌', '동작', '이수', '사당']: # 서울 지하철 4호선 전구간(남태령 제외)
                up_and_low.append('당고개(진접)')
                up_and_low.append('사당 / 오이도')
            else: # 서울 지하철 4호선 남태령역, 과천선, 안산선 구간
                up_and_low.append('당고개')
                up_and_low.append('오이도')

        elif self == 'tdResultSMRT5':
            if station in ['둔촌동', '올림픽공원', '방이', '오금', '개롱', '거여', '마천']: # 마천지선 구간
                up_and_low.append('방화')
                up_and_low.append('마천')
            elif station in ['길동', '굽은다리', '명일', '고덕', '상일동']: # 서울 지하철 5호선 길동 ~ 상일동 구간
                up_and_low.append('방화')
                up_and_low.append('하남검단산(상일동)')
            elif station in ['강일', '미사', '하남풍산', '하남시청', '하남검단산']: # 하남선 구간
                up_and_low.append('방화')
                up_and_low.append('하남검단산')
            else: # 서울 지하철 5호선 구간
                up_and_low.append('방화')
                up_and_low.append('하남검단산(상일동) / 마천')

        elif self == 'tdResultSMRT6':
            up_and_low.append('응암')
            up_and_low.append('봉화산(신내)')

        elif self == 'tdResultSMRT7':
            if station in ['까치울', '부천종합운동장', '춘의', '신중동', '부천시청', '상동', '삼산체육관', '굴포천', '부평구청', '산곡', '석남']:
                up_and_low.append('도봉산(장암)')
                up_and_low.append('석남')
            else:
                up_and_low.append('도봉산(장암)')
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
        elif self == 'tdResultAREXCommuter':
            up_and_low.append('서울')
            up_and_low.append('검암 / 인천국제공항')
        return up_and_low
