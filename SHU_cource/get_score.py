import requests
from bs4 import BeautifulSoup
import time

url = 'http://cj.shu.edu.cn/'
lcy = requests.session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
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
    'j_username': '',
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
data = {'academicTermID': ''}
ret = lcy.get(url, headers=headers, data=data)
print(ret.text)
