from pyvirtualdisplay import Display
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class get_destin():
    def run(station, line_number, destin):
        if line_number == "1":
            if destin in ["연천행", "소요산행", "동두천행", "양주행", "의정부행", "청량리행", "동묘앞", "서울행", "용산행", "영등포행"]: # 상행 전용 행선
                return '1'
            elif destin in ["부평행", "동인천행", "인천행", "광명행", "서동탄행", "신창행"]: # 하행 전용 행선
                return '2'
            else:
                if destin == "광운대행":
                    if station in ["소요산", "동두천", "보산", "동두천중앙", "지행", "덕정", "덕계", "양주", "녹양", "가능", "의정부", "회룡", "망월사", "도봉산", "도봉", "방학", "창동", "녹천", "월계"]:
                        return '2'
                    else:
                        return '1'
                if destin == "서울역행":
                    if station in ["소요산", "동두천", "보산", "동두천중앙", "지행", "덕정", "덕계", "양주", "녹양", "가능", "의정부", "회룡", "망월사", "도봉산", "도봉", "방학", "창동", "녹천", "월계", "광운대", "석계", "신이문", "외대앞", "회기", "청량리", "제기동", "신설동", "동묘앞", "동대문", "종로5가", "종로3가", "종각", "시청"]:
                        return '2'
                    else:
                        return '1'
                if destin == "구로행":
                    if station in ["소요산", "동두천", "보산", "동두천중앙", "지행", "덕정", "덕계", "양주", "녹양", "가능", "의정부", "회룡", "망월사", "도봉산", "도봉", "방학", "창동", "녹천", "월계", "광운대", "석계", "신이문", "외대앞", "회기", "청량리", "제기동", "신설동", "동묘앞", "동대문", "종로5가", "종로3가", "종각", "시청", "서울역", "서울", "남영", "용산", "노량진", "대방", "신길", "영등포", "신도림"]:
                        return '2'
                    else:
                        return '1'
                if destin == "병점행":
                    if station in ["신창", "온양온천", "배방", "탕정", "아산", "쌍용", "봉명", "천안", "두정", "직산", "성환", "평택", "평택지제", "서정리", "송탄", "진위", "오산", "오산대", "세마"]:
                        return '1'
                    else:
                        return '2'
                if destin == "천안행":
                    if station in ["신창", "온양온천", "배방", "탕정", "아산", "쌍용", "봉명"]:
                        return '1'
                    else:
                        return '2'
        if line_number == "3":
            if destin in ["대화행", "독립문행", "압구정행"]:
                return '1'
            elif destin in ["오금행", "수서행", "도곡행", "약수행", "삼송행"]:
                return '2'
            else:
                if destin == "구파발행":
                    if station in ["대화", "주엽", "정발산", "백석", "마두", "대곡", "화정", "원당", "원흥"]:
                        return '2'
                    else:
                        return '1'
        if line_number == "4":
            if destin in ["진접행", "노원행", "한성대입구행"]:
                return '1'
            elif destin in ["서울역행", "남태령행", "산본행", "오이도행"]:
                return '2'
            else:
                if destin == ["당고개행", "불암산행"]:
                    if station in ["진접", "오남", "별내별가람"]:
                        return '2'
                    else:
                        return '1'
                if destin == "사당행":
                    if station in ["남태령", "선바위", "경마공원", "대공원", "과천", "정부과천청사", "인덕원", "평촌", "범계", "금정", "산본", "수리산", "대야미", "반월", "상록수", "한대앞", "중앙", "고잔", "초지", "안산", "신길온천", "정왕", "오이도"]:
                        return '1'
                    else:
                        return '2'
                if destin == "금정행":
                    if station in ["산본", "수리산", "대야미", "반월", "상록수", "한대앞", "중앙", "고잔", "초지", "안산", "신길온천", "정왕", "오이도"]:
                        return '1'
                    else:
                        return '2'
                if destin == "안산행":
                    if station in ["신길온천", "정왕", "오이도"]:
                        return '1'
                    else:
                        return '2'
        else:
            return None
