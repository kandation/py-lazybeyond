import json
import os
from pprint import pprint

import requests, pickle
from bs4 import BeautifulSoup
from urllib.parse import quote
import urllib3
import re
from dotenv import load_dotenv

urllib3.disable_warnings()
load_dotenv()


class BeyondLazy:
    def __init__(self, username, password):
        self.__session = requests.Session()
        self.__user = ''
        self.__pwnd = ''
        self.__v_state = ''
        self.__v_gen = ''
        self.__v_valid = ''

        self.set_user(username)
        self.set_pwd(password)

    def get_user(self):
        return self.__user

    def set_user(self, username):
        self.__user = username

    def get_pwd(self):
        return self.__pwnd

    def set_pwd(self, password):
        self.__pwnd = password

    def get_v_state(self):
        return self.__v_state

    def set_v_state(self, value):
        self.__v_state = quote(value)

    def get_v_gen(self):
        return self.__v_gen

    def set_v_gen(self, value):
        self.__v_gen = quote(value)

    def get_v_valid(self):
        return self.__v_valid

    def set_v_valid(self, value):
        self.__v_valid = quote(value)

    def get_session(self):
        return self.__session

    def login(self):
        print('=== Login ===')
        v_login = self.__login_get()
        self.__get_aspx_validation(v_login)
        v_login_post = self.__login_post()

    def __login_get(self):
        url = "https://vcubelms.com/beyondtrainingplus/Login/Login.aspx?returnUrl=/beyondtrainingplus/Dashboard/TaskTab.aspx"
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'th,en-US;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41',
            'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }

        response = self.__session.request("GET", url, headers=headers, verify=False)
        return response.text or ""

    def __login_post(self):
        url = "https://vcubelms.com/beyondtrainingplus/Login/Login.aspx?returnUrl="

        payload = f'__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=' \
                  f'&__VIEWSTATE={self.get_v_state()}&__VIEWSTATEGENERATOR={self.get_v_gen()}' \
                  f'&__EVENTVALIDATION={self.get_v_valid()}&txtUserName={self.get_user()}&txtPassword={self.get_pwd()}' \
                  f'&btnLogin=Login&ddlLanguage=en-GB'
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'th,en-US;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'ASP.NET_SessionId=etorq54iruujfw4vcr3p32gy; G_ENABLED_IDPS=google; .AspNet.AccessCookie=IH9jesU1i1RFKoKosSGsEgfWYH%2brRTHQ9qReBjo%2fuJ9szm2ecWLEoaYL5ByKGNHmUdQpDrq4x%2b1m8JgUSblZ5g%3d%3d; .AspNet.AccessCookie=UfwIT6Mh8fcUpWH0CwTQ8iADF2nuUh4VlLiOB7%2fNE1yt2fQPHbD%2bFl7nslmoubmU%2bNmLDO6ssIHK2yKIebr9Zw%3d%3d; __AntiXsrfToken=093d319cd3ea42be94fc65b686ab01ed',
            'DNT': '1',
            'Origin': 'https://vcubelms.com',
            'Referer': 'https://vcubelms.com/beyondtrainingplus/Login/Login.aspx?returnUrl=/beyondtrainingplus/Dashboard/TaskTab.aspx',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41',
            'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }

        response = self.__session.request("POST", url, headers=headers, data=payload, verify=False)

        return response.text

    def __get_aspx_validation(self, text):
        bs = BeautifulSoup(text, "lxml")
        self.set_v_state(bs.find('input', {'name': '__VIEWSTATE'}).get('value'))
        self.set_v_gen(bs.find('input', {'name': '__VIEWSTATEGENERATOR'}).get('value'))
        self.set_v_valid(bs.find('input', {'name': '__EVENTVALIDATION'}).get('value'))

        return {'state': self.__v_state, 'gen': self.__v_gen, 'valid': self.__v_valid}


class BeyondLazyApi:
    def __init__(self, session: requests.Session):
        self.session = session
        self.__raw_tasks = {}
        self.__tasks = []
        self.__curr_uri = ''

    def check_cookie(self):
        print(self.session.cookies)

    def get_tasks(self):
        url = "https://vcubelms.com/beyondtrainingplus/WebService/Dashboard/TaskTabService.asmx/GetTasks"

        payload = "{\"status\":1,\"index\":0,\"size\":10,\"orderBy\":\"RecentActivity_DESC\",\"activityTypes\":\"1,2,3,4,5,8\",\"courseTypes\":\"1,2,3\"}"
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'th,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'DNT': '1',
            'Origin': 'https://vcubelms.com',
            'Referer': 'https://vcubelms.com/beyondtrainingplus/Dashboard/TaskTab.aspx',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }

        response = self.session.request("POST", url, headers=headers, data=payload, verify=False)

        return response.json()

    def take_by_index(self, index):
        task = self.get_tasks()
        tasks = task.get('Result', {}).get('Tasks', [])
        tid = tasks[index].get('TaskId')
        uri = str(tasks[index].get('Url', '')).split('?p=')[-1]

        self.__curr_uri = uri

        print('ssxxxx', self.__curr_uri)

        return (tid, uri)

    '''https://vcubelms.com/beyondtrainingplus/Course/ViewCourse.aspx?p=PKYiwAadC8sQGNJR7tIBdE49jPG3Vk7pPIZyyjLMiZ%2bSzCg10tvQXmlZyT75qPQvFIAwul9FyVCIM05w4gAzHedSqAzu1hESizGh4kR9E8gztlzEqJFcaFrj4URAendUYCMuFqD%2fmwp7YkdW6whbJDxI85GDLh11%2fQps8JSn85UbcykunJ4ZNI5Lw7orHLLVgXQeX1ixnbAVgLA10NkukLzYhWQBxCXeoc5pCQ8uIoQpBKXQ349B1GVw8KkMP428HAKj2efpnYOS0tBPKU%2b8E9ATqFjXm78Smd5WO%2bRBQR4k1sTj%2f9S4oSInlVI3B7NukbUMGwqfo3iOt8L9oVTamgh6KK%2fUbFxyPTpERKYmZoQ9vjrXX3Ctf%2bIRAZwz4OM5qO08xkdSUsXvOHeGtIOZMQ%3d%3d'''

    def take(self, id, ref_course_id):
        url = "https://vcubelms.com/beyondtrainingplus/WebService/Course/CourseService.asmx/Take"
        # 8e76cd36-a2c3-ed11-9d88-00505601273f
        payload = f'{{\"resultId\":\"{id}\"}}'
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'th,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'DNT': '1',
            'Origin': 'https://vcubelms.com',
            'Referer': f'https://vcubelms.com/beyondtrainingplus/Course/ViewCourse.aspx?p={ref_course_id}',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }

        response = self.session.request("POST", url, headers=headers, data=payload, verify=False)

        return response.text

    def get_start(self):
        import requests

        url = f"https://vcubelms.com/beyondtrainingplus/Course/Start.aspx?p={self.__curr_uri}"
        print(url)

        payload = {}
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'th,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Referer': 'https://vcubelms.com/beyondtrainingplus/Dashboard/TaskTab.aspx',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41',
            'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }

        response = self.session.request("GET", url, headers=headers, data=payload, verify=False)

        print(response.text)
        print(response.headers)

    def get_result_id(self):
        if self.__curr_uri:
            raise Exception("Not select Course")

        url = f"https://vcubelms.com/beyondtrainingplus/Course/ViewCourse.aspx?p={self.__curr_uri}"

        payload = {}
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'th,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Referer': 'https://vcubelms.com/beyondtrainingplus/Dashboard/TaskTab.aspx',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41',
            'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }

        response = self.session.request("GET", url, headers=headers, data=payload, verify=False)

        print(response.text)
        print(response.url)
        print(response.history)

        return self.__find_result_id_form_start(response.text)

    def __find_result_id_form_start(self, text):
        pattern = r'ctrl\.ResultId = "(.*?)";'
        result = re.search(pattern, text)
        res = result.group(1) if result else ""
        self.__curr_res_id = res
        return res


class SessionManager:
    def __init__(self):
        self.__session = requests.Session()

    def __set_session(self, session: requests.Session = None):
        if session is not None:
            print('Get Sessions')
            self.__session = session

    def load(self):
        with open('session.pickle', 'rb') as f:
            self.__session.cookies.update(pickle.load(f))

    def save(self, session: requests.Session = None):
        self.__set_session(session)

        with open('my/cookie.json', 'w') as f:
            json.dump(self.__session.cookies.get_dict(), f)
        with open('my/session.pickle', 'wb') as f:
            pickle.dump(self.__session.cookies, f)

    def get_session(self):
        return self.__session


if __name__ == '__main__':
    TEST_FIRST_LOGIN = True

    env_user = os.getenv('BEYOND_USERNAME')
    env_pass = os.getenv('BEYOND_PASSWORD')
    print(f'Login by {env_user} {env_pass}')

    b = BeyondLazy(env_user, env_pass)
    if TEST_FIRST_LOGIN:
        b.login()

    b_session = b.get_session()
    session = SessionManager()

    if TEST_FIRST_LOGIN:
        session.save(b_session)

    session.load()
    r_session = session.get_session()

    bx = BeyondLazyApi(r_session)
    t = bx.check_cookie()
    print(t)

    pp = bx.get_tasks()
    pprint(pp)

    js = bx.take_by_index(0)
    pprint(js)

    bx.get_start()
    # bx.take()
    # bx.take()
