"""
    파일을 다운받고 저장하는 함수

     [참고] 파이썬 정규식 표현 : https://wikidocs.net/4308
"""
from bs4 import BeautifulSoup
from urllib import parse
from urllib import request
import os, time, re  # re : 정규식

'''
    함수명 : download_file
    인자 : url(정보를 받아올 url)
    리턴값 : savepath(파일을 다운받아 저장할 경로)
    역할 : 파일을 다운받고 저장하는 함수

'''

def download_file(url):
    # 해당하는 url 정보를 자르는 역할
    # hostname과 path 를 사용하여 현재 폴더에 생성할 새 저장 경로를 만든다.
    p = parse.urlparse(url)
    # print('1-', p)
    # netloc( ) 함수를 사용하여 hostname 을, path( ) 함수를 사용하여 경로를 가져온다.
    savepath = './' + p.netloc + p.path
    # print('2', savepath)
    if re.search('/$', savepath):
        # 저장경로가 / 로 끝날 경우 index.html 을 덧붙임으로써,
        # 파일을 다운받을 경로가 완성되게끔 한다.
        savepath += 'index.html'
        print('3-', savepath)

    # 이미 파일을 다운 받았을 경우 함수 종료
    if os.path.exists(savepath): return savepath

    # 다운 받은 파일이 저장될 폴더가 없을 경우 생성한다.
    savedir = os.path.dirname(savepath)
    if not os.path.exists(savedir):
        os.makedirs(savedir)    #  makedirs로 하위폴더까지 생성

    try:
        request.urlretrieve(url, savepath)
        time.sleep(2)       # 파일 하나 다운 받고 2초 쉬기
        print('download - ', url)
        return savepath
    except:
        print('fail download :', url)
        return  None

if __name__ == '__main__':
    url = 'https://docs.python.org/3.6/library/'
    result = download_file(url)
    print(result)



