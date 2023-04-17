import os
from IPython.display import clear_output

class searchStationInfo():
    def __init__(sel):
        self.sel = sel

    def process(sel):
        try:
            clear_output()
            os.system('clear')
        except:
            os.system('cls')
        line1_stns = ["소요산", "동두천", "보산", "동두천중앙", "지행", "덕정", "덕계", "양주", "녹양", "가능", "의정부", "회룡", "망월사", "도봉산", "도봉", "방학", "창동", "녹천", "월계", "광운대", "석계", "신이문", "외대앞", "회기", "청량리", "제기동", "신설동", "동묘앞", "동대문", "종로5가", "종로3가", "종각", "시청", "서울역", "남영", "용산", "노량진", "대방", "신길", "영등포", "신도림", "구로", "구일", "개봉", "오류동", "온수", "역곡", "소사", "부천", "중동", "송내", "부개", "부평", "백운", "동암", "간석", "주안", "도화", "제물포", "도원", "동인천", "인천", "가산디지털단지", "독산", "금천구청", "광명", "석수", "관악", "안양", "명학", "금정", "군포", "당정", "의왕", "성균관대", "화서", "수원", "세류", "병점", "서동탄", "세마", "오산대", "오산", "진위", "송탄", "서정리" , "평택지제", "평택", "성환", "직산", "두정", "천안", "봉명", "쌍용", "아산", "탕정", "배방", "풍기", "온양온천", "신창"]
        line2_stns = ["", "시청", "을지로입구", "을지로3가", "을지로4가", "동대문역사문화공원", "신당", "상왕십리", "왕십리", "한양대", "뚝섬", "성수", "건대입구", "구의" ,"강변", "잠실나루", "잠실", "잠실새내", "종합운동장", "삼성", "선릉", "역삼", "강남", "교대", "서초", "방배", "사당", "낙성대", "서울대입구", "봉천", "신림", "신대방", "구로디지털단지", "대림", "신도림", "문래", "영등포구청", "당산", "합정", "홍대입구", "신촌", "이대", "아현", "충정로", "용답", "신답", "용두", "신설동", "도림천", "양천구청", "신정네거리", "까치산"]
        line3_stns = ["", "", "", "", "", "", "", "", "", "대화", "주엽", "정발산", "마두", "백석", "대곡", "화정", "원당", "원흥", "삼송", "지축", "구파발", "연신내", "불광", "녹번", "홍제", "무악재", "독립문", "경복궁", "안국", "종로3가", "을지로3가", "충무로", "동대입구", "약수", "금호", "옥수", "압구정", "신사", "잠원", "고속터미널", "교대", "남부터미널", "양재", "매봉", "도곡", "대치", "학여울", "대청", "일원", "수서", "가락시장", "경찰병원", "오금"]
        line4_stns = ["", "", "", "", "", "진접", "오남", "풍양", "별내별가람", "당고개", "상계", "노원", "창동", "쌍문", "수유", "미아", "미아사거리", "길음", "성신여대입구", "한성대입구", "혜화", "동대문", "동대문역사문화공원", "충무로", "명동", "회현", "서울역", "숙대입구", "삼각지", "신용산", "이촌", "동작", "이수", "사당", "남태령", "선바위", "경마공원", "대공원", "과천", "정부과천청사", "과천지식산업단지", "인덕원", "평촌", "범계", "금정", "산본", "수리산", "대야미", "반월", "상록수", "한대앞", "중앙", "고잔", "초지", "안산", "신길온천", "정왕", "오이도"]

        if sel == '1':
            from line1 import stn as stations
            stn_list = line1_stns
        elif sel == '2':
            from line2 import stn as stations
            stn_list = line2_stns
        elif sel == '3':
            from line3 import stn as stations
            stn_list = line3_stns
        elif sel == '4':
            from line4 import stn as stations
            stn_list = line4_stns

        stn_sel = input('역명을 입력해주세요. 부기역명 없이 한글 역명 정확히 적어주세요 : ')
        stn_num = 0
        for stn in stn_list:
            if stn_list[stn_num] == stn_sel:
                break
            stn_num += 1

        station = stations.stns[int(stn_num)]
        print(f"{station['KRName']}역의 정보")
        print(f"{station['KRName']}".center(27))
        print(f"({station['Num']})".center(30))

        if station['Terminal'] == 'Yes':
            if station['nextStop'] == None or station['preStop'] == None:
                pass
            elif station['nextStop'] != None or station['preStop'] != None:
                print("(일부 열차 시종착)".center(25))
        elif station['Terminal'] == 'lastTrain':
            print("(막차 한정 시종착)".center(25))
        elif station['Terminal'] == 'emergency':
            print("(비상시 시종착 가능)".center(20))

        print(f"<={station['nextToward']} 방면".rjust(5), end = '')
        print(f"{station['preToward']} 방면=>".rjust(20), end = '')
        # print(f"<={station['nextToward']} 방면          {station['preToward']} 방면=>".center(25))

        print("")

        if station['nextStop'] == None:
            print("시종착".rjust(5), end = '')
            print(f"{station['preStop']}".rjust(20))
        elif station['preStop'] == None:
            print(f"{station['nextStop']}".rjust(5), end = '')
            print("시종착".rjust(20))
        else:
            print(f"{station['nextStop']}               {station['preStop']}".center(25))

        print(f"{station['nextDistance']}                  {station['preDistance']}".center(35))
        if station['Transfer'] != 'No':
            print(f"{station['Transfer']}과 환승이 가능합니다.")

        print(f"내리는 문은 {station['Doors']}입니다.")
