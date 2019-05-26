import requests
from bs4 import BeautifulSoup
import time

cookie_str = '_ga=GA1.3.301667312.1529715759; UM_distinctid=1684136598d290-02672aa019b919-b78173e-e1000-1684136598e61; ASP.NET_SessionId=mw1xby3t0ne1f0giz5rblmie'
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36', 'Referer': 'http://www.xk.shu.edu.cn/'}
url = 'http://xk.autoisp.shu.edu.cn/CourseSelectionStudent/CtrlViewOperationResult'
no = [('07275061', '1004'),
      ('07275084', '1001'),
      ('07275142', '1001'),
      ('07275145', '1002'),
      ('07276018', '1003'),
      ('0727A014', '1003'),
      ('16583109', '1090')]
data = {
    'IgnorClassMark': False,
    'IgnorCourseGroup': False,
    'IgnorCredit': False,
    'StudentNo': 17124056,
    'ListCourse[0].CID': '',
    'ListCourse[0].TNo': ''
}
for i, course in enumerate(no):
    cid, tid = course
    data['ListCourse[0].CID'] = cid
    data['ListCourse[0].TNo'] = tid
    html = requests.post(url, data=data, headers=headers, cookies=cookies)
    if html.status_code != 200:
        print('fail to connect')
        break
    while html.text.find('选课成功') == False:
        time.sleep(5)
        html = requests.post(url, data, headers=headers, cookies=cookies)
        print(str(i), ' failed')
    print(str(i), ' success')
'''
data = {
    'IgnorClassMark': False,
    'IgnorCourseGroup': False,
    'IgnorCredit': False,
    'StudentNo': 17124056,
    'ListCourse[0].CID': '',
    'ListCourse[0].TNo': ''
}
html = requests.post(url, headers=headers, cookies=cookies, data=data)
if html.text.find('选课成功'):
    print('ok')
else:
    print('fail')
'''
