"""
http://www.seoul.go.kr > 청사안내 > 자치구
https://www.seoul.go.kr/seoul/autonomy.do

BeautifulSoup  : 파서를 이용해서 html 의 요소를 추출하게 해주는 모듈
        - 단점은 개행문자를 고려해야 한다
Tag : 태그
NavigableString : 원래는 tag 사이의 문자열

#  xpath를 사용하면 개행문자를 고려하지 않아도 된단다
#  https://developer.mozilla.org/ko/docs/XPath
"""

from urllib import request
from bs4 import BeautifulSoup

html = 'http://www.seoul.go.kr/seoul/autonomy.do'
site = request.urlopen(html)
site1=site.read()

soup = BeautifulSoup(site1,"html.parser")

# 아래 리스트에 각 구청의 상세 정보를 저장하고 출력하기
구청이름 = []
구청주소 = []
구청전화번호 = []
구청홈페이지 = []
name = soup.select('#content strong')
for x in name:
    구청이름.append(x.text)
addr = soup.select('li:nth-child(1)')
for x in addr:
    구청주소.append(x.text)
tel = soup.select('li:nth-child(2)')
for x in tel:
    구청전화번호.append(x.text)
home = soup.select('li:nth-child(3)')
for x in home:
    구청홈페이지.append(x.text)

for i,x in enumerate(구청이름):
    print('구청이름 : ', x)
    print('구청주소 : ', 구청주소[i])
    print('구청전화번호 : ', 구청전화번호[i])
    print('구청홈페이지 : ', 구청홈페이지[i])
    print('')



'''
1. 추출한 결과를 위 리스트에 저장한다.'''
# for i in soup:
#     name = [name.text for name in soup.select('.tabcont strong')]
#     # print(name)
#     addr = [addr.text for addr in soup.select('.tabcont li:nth-child(1)')]
#     # print(addr)
#     tel = [tel.text for tel in soup.select('.tabcont li:nth-child(2)')]
#     # print(tel)
#     page = [page.text for page in soup.select('.tabcont li a')]
#     # print(page)
#     for name, addr, tel, page in zip(name, addr, tel, page):
#         print('구청이름 :', name)
#         print('구청주소 :', addr)
#         print('구청전화번호 :', tel)
#         print('구청홈페이지 :', page)
#         print('-'*10)


'''2. 리스트 출력 결과 예시- 아래처럼 각 구청의 정보를 추출
      ex)
      구청이름 : 강동구
      구청주소 : (우) 04558 / 서울시 중구 창경궁로 17 (예관동)
      구청전화번호 : TEL. 02-3396-4114
      구청홈페이지 : http://www.junggu.seoul.kr
'''
# for i in soup:
#     name = soup.select('.tabcont strong')
#     addr = soup.select('.tabcont li:nth-child(1)')
#     tel = soup.select('.tabcont li:nth-child(2)')
#     page = soup.select('.tabcont li a')
#     for name, addr, tel, page in zip(name, addr, tel, page):
#         print('구청이름 :', name.text)
#         print('구청주소 :', addr.text)
#         print('구청전화번호 :', tel.text)
#         print('구청홈페이지 :', page.text)
#         print('-'*10)
