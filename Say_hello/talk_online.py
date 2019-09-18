from requests import *
from bs4 import BeautifulSoup
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}

def weather():
    url = 'http://www.weather.com.cn/weather1d/101020100.shtml'
    lcy = session()
    ret = lcy.get(url, headers=headers)
    ret.encoding = ret.apparent_encoding
    soup = BeautifulSoup(ret.text, 'lxml')
    tar = soup.find_all('li')
    '''
    print(type(tar))
    for i, t in enumerate(tar):
        print(i, t.text) 
    '''
    t1 = tar[28]
    t2 = tar[29]
    res = []
    for word in t1.text.split():
        print(word)
        res.append(word)
    return res

def joke():
    rnd_ret = random.randint(1, 7)
    f = open('jokeset.txt', 'r', encoding='utf8')
    sty = ''
    for id, line in enumerate(f.read().split()):
        # print(line)
        if id + 1 == rnd_ret:
            print(line)
            sty = line
            break
    f.close()
    return sty

def grade():
    url = 'http://cj.shu.edu.cn/'
    lcy = session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
    ret = lcy.get(url, headers=headers)
    soup = BeautifulSoup(ret.text, 'lxml')
    all_in = soup.find_all('input')
    data = {}
    for i, input in enumerate(all_in):
        data[input['name']] = input['value']
    url = 'https://sso.shu.edu.cn/idp/profile/SAML2/POST/SSO'
    ret = lcy.post(url, headers=headers, data=data)
    url = 'https://sso.shu.edu.cn/idp/Authn/UserPassword'
    data = {
        'j_username': '17124056',
        'j_password': ''
    }
    ret = lcy.post(url, headers=headers, data=data)
    soup = BeautifulSoup(ret.text, 'lxml')
    all_input = soup.find_all('input')
    data = {}
    for i, input in enumerate(all_input):
        if i >= 2:
            break
        data[input['name']] = input['value']
    url = 'http://oauth.shu.edu.cn/oauth/Shibboleth.sso/SAML2/POST'
    ret = lcy.post(url, data=data, headers=headers)
    url = 'http://cj.shu.edu.cn/StudentPortal/ScoreQuery'
    ret = lcy.get(url, headers=headers)
    url = 'http://cj.shu.edu.cn/StudentPortal/CtrlScoreQuery'
    data = {'academicTermID': '20181'}
    ret = lcy.get(url, headers=headers, data=data)
    soup = BeautifulSoup(ret.text, 'lxml')
    all_td = soup.find_all('td')
    ub = []
    tmp = ''
    for i, td in enumerate(all_td):
        if i + 1 <= 72:
            print(td.text, end=' ')
            tmp += td.text + ' '
            if (i + 1) % 6 == 0:
                print()
                ub.append(tmp)
                tmp = ''
    print(all_td[72].text)
    ub.append(all_td[72].text)
    return ub

'''
if __name__ == '__main__':
    grade()
'''
