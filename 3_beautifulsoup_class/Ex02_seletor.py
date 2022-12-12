"""
    BeautifulSoup 모듈에서
    - HTML의 구조(=트리구조)에서 요소를 검색할 때 : find() / find_all()
    - CSS 선택자 검색할 때 : select() /  select_one()
    ※ select()으로 하면 list 형태로 출력
      select_one() 으로 하면 한개씩 나옴
"""

from bs4 import BeautifulSoup

html = """
    <html><body>
        <div id='course'>
            <h1>빅데이터 과정</h1>
        </div>
        <div id='subjects'> 
            <ul class='subs'>
                <li>머신러닝</li>
                <li>데이터 처리</li>
                <li>데이타 분석</li>
            </ul>
        </div>
    </body></html>
"""
soup = BeautifulSoup(html, 'html.parser')

# (1) id로 찾기
h = soup.select_one('#course > h1')
print(h)
print(h.text)
# (2) class로 찾기
li = soup.select('ul.subs > li')
print(li)
for i in li:
    print(i)
    print(i.text)