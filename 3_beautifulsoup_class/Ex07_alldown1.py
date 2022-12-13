"""
    HTML 내부에 있는 링크를 추출하는 함수
        - a 링크 연결된 모든 파일을 가져오기
"""

from bs4 import BeautifulSoup
from urllib import parse, request
# from urllib import request
'''
    함수명 :enum_links
    인자 : html(해당 페이지), base(상대경로를 절대경로로 바꾸기 위한 url)
    리턴값 : result(링크들의 리스트)
    역할 : htrml내부에 있는 링크를 추출


'''
# HTML 내부에 있는 링크를 추출하는 함수
def enum_links(html,base):
    #-------------------------------------
    soup = BeautifulSoup(html, 'html.parser')
    # a 속성 값들 받아서 links에 넣기
    links = soup.select('a')
    # print(links)
    result = []
    for a in links:
        # 필요한 건 href 속성
        href = a.attrs['href']
        # print(href)
        # 해당 href가 상대 경로라서 urljoin이 필요함
        url = parse.urljoin(base, href)
        # print(url)
        result.append(url)
    return result


if __name__ == '__main__':
    url = 'https://docs.python.org/3.7/library/'
    response = request.urlopen(url)   # urllib.request.urlopen() : BeautifulSoup을 통해 html 파서할(데이타를 가져올) 대상
    # 응답한 파일을 넘겨주는 enum_links
    result = enum_links(response, url)
    print(result)