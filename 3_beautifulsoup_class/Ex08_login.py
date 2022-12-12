"""
    일단 http://www.hanbit.co.kr 회원가입

    [예] 한빛출판네트워크 ( 단순 페이지 ) : 이 예문은 위키북스 출판사 교재 예문임
                                    <파이썬을 이용한 머신러닝, 딥러닝 실전개발 예문>
    로그인페이지 : http://www.hanbit.co.kr/member/login.html
    마이페이지 : http://www.hanbit.co.kr/myhanbit/myhanbit.html

    1. 로그인 페이지에서 개발자모드에서 로그인 form 태그를 분석
        입력태그의 name='m_id' / name='m_passwd' 확인

    2. 로그인 후에 마이페이지에서 마일리지와 한빛이코인 부분
        마일리지 (.mileage_section1 > dd > span ) / 한빛이코인 (.mileage_section2 > dd > span )

    3. 로그인과정에 어떤 통신이 오가는지 분석
        Network > Preserve log 체크 > Doc 탭을 선택하고 다시 처음부터 로그인을 하면 서버와 통신을 오고간다
        이 때 Name 중 login_proc.php를 선택하고 Headers 부분을 확인한다
        
        Gereral : Request Mathod : POST
        Form Data : m_id와 m_passwd 값 확인
"""

import requests
from bs4 import BeautifulSoup

req = requests.session() #세션을 사용하기 위한 준비 ( 실제 세션은 아니지만, 로그인이 필요한지 여부를 세션으로 파악하기 때문 )

login_info = {
    "m_id" : "ketty1061",
    "m_passwd" : "!rudgh1061"
}
# 세션을 사용하여 url 에 로그인 정보를 넘기고 그 결과를 출력해본다.
# requests 라이브러리의 raise_for_status( ) 함수는 오류가 발생하면 예외를 발생시킨다.

url_login = 'https://www.hanbit.co.kr/member/login_proc.php'
res = req.post(url_login, login_info)

url_mypage = 'https://www.hanbit.co.kr/myhanbit/myhanbit.html'
mypage = req.get(url_mypage)

soup = BeautifulSoup(mypage.text, 'html.parser')

mileage = soup.select_one('.mileage_section1 span')
coin = soup.select_one('.mileage_section2 span')

print('마일리지:{}점\n이코인:{}원'.format(mileage.text, coin.text))
