#urllib 라이브러리
'''
     - URL를 다루는 모듈을 모아 놓은 패키지
      - Http나 Ftp를 사용하여 데이터를 다운로드 할 때 사용하는 라이브러리

      - request 모듈 : 웹 요청을 보내고 받는 기능을 하는 모듈
        >> urlretrieve() 함수를 이용하여 이미지를 다운로드 받아 파일로 저장한다.

'''

# 내장모듈 이용
from urllib import request

url ='http://www.google.com'
site = request.urlopen(url)

page = site.read()
print(page)
print('-'*50)
print(site.status)

headers = site.getheaders()
print(headers)      # 리스트 구조안에  튜플로 잡힘

for header in headers:
    print(header[0],'>>',header[1])