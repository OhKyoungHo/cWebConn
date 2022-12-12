from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <ul>
                <li><a href='http://www.naver.com'>네이브</a></li>
                <li><a href='http://www.daum.net'>다아음</a></li>
            </ul>
        </body>
    </html>
"""

''' 리스트(li)목록의 내용과 해당 경로를 추출하기
    속성추출 : attrs['속성명']

    [출력결과]
    네이브 : http://www.naver.com
    다아음 : http://www.daum.net
'''

# 데이터 파서하기
soup = BeautifulSoup(html, 'html.parser')
# a tag 찾아서 변수 지정
alist = soup.find_all('a')
# list 형태이기 때문에 반복문으로 출력
for i in alist:
    name = i.text
    link = i.attrs['href']
    print(name, ':', link)
