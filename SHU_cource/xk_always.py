import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}

class client:

    def __init__(self):
        self.lcy = requests.session()
        self.calc()

    def calc(self):
        url = 'http://xk.autoisp.shu.edu.cn/'
        ret = self.lcy.get(url, headers=headers)
        url = 'https://oauth.shu.edu.cn/oauth/authorize?response_type=code&client_id=yRQLJfUsx326fSeKNUCtooKw&redirect_uri=http%3a%2f%2fxk.autoisp.shu.edu.cn%2fpassport%2freturn'
        ret = self.lcy.get(url, headers=headers)
        data = {}
        soup = BeautifulSoup(ret.text, 'lxml')
        input = soup.find_all('input')
        for i in input:
            data[i['name']] = i['value']
        url = 'https://sso.shu.edu.cn/idp/profile/SAML2/POST/SSO'
        ret = self.lcy.post(url, data=data, headers=headers)
        url = 'https://sso.shu.edu.cn/idp/Authn/UserPassword'
        data_user = {
            'j_username': '',    # 学号
            'j_password': ''     # 密码
        }
        ret = self.lcy.post(url, data=data_user, headers=headers)
        data = {}
        soup = BeautifulSoup(ret.text, 'lxml')
        input = soup.find_all('input')
        for e, i in enumerate(input):
            if e > 1:
                break
            data[i['name']] = i['value']
        url = 'http://oauth.shu.edu.cn/oauth/Shibboleth.sso/SAML2/POST'
        ret = self.lcy.post(url, headers=headers, data=data)
        url = 'http://xk.autoisp.shu.edu.cn/CourseSelectionStudent/FastInput'
        ret = self.lcy.get(url, headers=headers)
        if ret.text.find('选课时间未到') != -1:
            print('不可以选课')

    def course(self, CouNo, TeaNo):
        url = 'http://xk.autoisp.shu.edu.cn/CourseSelectionStudent/CtrlViewOperationResult'
        referer = 'http://xk.autoisp.shu.edu.cn/CourseSelectionStudent/FastInput'
        data = {
            'IgnorClassMark': False,
            'IgnorCourseGroup': False,
            'IgnorCredit': False,
            'StudentNo': '',    # 学号
            'ListCourse[0].CID': CouNo,
            'ListCourse[0].TNo': TeaNo,
            'ListCourse[0].NeedBook': False
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        }
        ret = self.lcy.post(url, headers=headers, data=data)
        # print(ret.text)
        return ret

if __name__ == '__main__':
    '''
    neww = client()
    ret = neww.course('1234', '1234')
    print(ret.text)
    '''
    lcyy = []
    for i in range(40):
        lcyy.append(client())
        print(str(i) + ' login succeed!')
    T = 0
    while True:
        st = time.time()
        try:
            ret = lcyy[T % 40].course('', '')    # 课程编号 教师号
            print(str(T) + ' :Thread ' + str(T % 40 + 1) + '  :' + str(time.time()-st))
            # print(ret.text)
            soup = BeautifulSoup(ret.text, 'lxml')
            all_td = soup.find_all('td')
            print(all_td[10].text.strip())
            if ret.text.find('选课成功') != -1:
                print('Succeed!')
                break
        except Exception as e:
            print(e)
            print('trying to reconnect...')
            lcyy[T % 40] = client()
        T += 1
        
