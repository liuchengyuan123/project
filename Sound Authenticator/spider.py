import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/71.0.3578.80 Safari/537.36'}
html = 'https://ibaotu.com/yinxiao/?chan=bd&label=video&plan=D2-bd&kwd=6705&\
            utm_source=%E7%99%BE%E5%BA%A6SEM&utm_medium=D2-bd&utm_campaign=%E9%9F%B3%E6%95%88-%E9%9F%B3%E6%95%88%E5%85%B6%E4%BB%96&\
            utm_term=%E5%88%9B%E6%84%8F&renqun_youhua=709935&bd_vid=9279238515515122058'
start = requests.get(html, headers = headers)
start.encoding = 'utf-8'
soup = BeautifulSoup(start.text, 'lxml')
all_a = soup.find('div', class_ = 'media-list media-audio').find_all('audio')
add = 'spider_file/'
for i, a in enumerate(all_a):
    source = a.find('source')
    print(source['src'])
    audio = requests.get('http:' + source['src'], headers = headers)
    print(audio.status_code)
    f = open(add + str(i) + '.mp3', 'ab')
    f.write(audio.content)
    print(add + str(i) + '.mp3', 'completed')
    f.close()
