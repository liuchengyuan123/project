import requests
from bs4 import BeautifulSoup


class stu:
    def __init__(self):
        self.lcy = requests.session()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
        self.base()

    def base(self):
        url = 'http://cj.shu.edu.cn/'
        self.lcy = requests.session()
        ret = self.lcy.get(url, headers=self.headers)
        soup = BeautifulSoup(ret.text, 'lxml')
        all_in = soup.find_all('input')
        data = {}
        for i, input in enumerate(all_in):
            data[input['name']] = input['value']
        url = 'https://sso.shu.edu.cn/idp/profile/SAML2/POST/SSO'
        ret = self.lcy.post(url, headers=self.headers, data=data)
        url = 'https://sso.shu.edu.cn/idp/Authn/UserPassword'
        data = {
            'j_username': '',
            'j_password': ''
        }
        ret = self.lcy.post(url, headers=self.headers, data=data)
        soup = BeautifulSoup(ret.text, 'lxml')
        all_input = soup.find_all('input')
        data = {}
        for i, input in enumerate(all_input):
            if i >= 2:
                break
            data[input['name']] = input['value']
        url = 'http://oauth.shu.edu.cn/oauth/Shibboleth.sso/SAML2/POST'
        ret = self.lcy.post(url, data=data, headers=self.headers)
        # waiting to check

    def query(self):
        url = 'http://cj.shu.edu.cn/StudentPortal/ScoreQuery'
        ret = self.lcy.get(url, headers=self.headers)

    def judge(self):
        url = 'http://cj.shu.edu.cn/StudentPortal/Evaluate'
        ret = self.lcy.get(url, headers=self.headers)
        soup = BeautifulSoup(ret.text, 'lxml')
        table = soup.find(class_='tbllist')
        all_tr = table.find_all('tr')
        data = {}
        for i, tr in enumerate(all_tr):
            if i is 0:
                continue
            all_td = tr.find_all('td')
            # print(all_td[0].find('input'))
            for input in all_td[0].find_all('input'):
                # print(input['name'], input['value'])
                try:
                    data[input['name']] = input['value']
                except KeyError:
                    continue
            for i in range(4, all_td.__len__()):
                data[all_td[i].find('select')['name']] = 25
        '''
        for key, value in data.items():
            print(key, value)
        '''
        url = 'http://cj.shu.edu.cn/StudentPortal/EvaluateSave'
        ret = self.lcy.post(url, headers=self.headers, data=data)
        if ret.status_code == 200:
            print('教学评估已完成')

if __name__ == '__main__':
    task = stu()
