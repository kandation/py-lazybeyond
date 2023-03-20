import json
import random
from time import sleep
import urllib3
from colored import fg, bg, attr

urllib3.disable_warnings()


def show(*text):
    print(f'{bg(1)}', text)


class LazyLearnResource:
    def __init__(self, item_id):
        self.item_id = item_id
        self.__duration_need = 100
        self.__duration_maxa = 0
        self.__duration_curr = 0
        self.__duration_skip = 10
        self.__item_data = {}
        self.__select_data_x = {}
        self.__view_gateway = None

        self.__lazy_cookie = {
            'Cookie':'ASP.NET_SessionId=wf1ahfw5sj1jogfz3sxy0dec; G_ENABLED_IDPS=google; __AntiXsrfToken=ea170191fe40417b9c307fbcf404e912; .AspNet.ApplicationCookie=H8P6P1rkDBiTv3ZEgzgOXV-GHO9gGvcBD9H0gkFVoWYNk-Q8cAdAMgCfO2wNhA3gfmZyDBgz12fvlqDuDJKRE3Nj5OjKb3AHg4CCfHly_Y3FKcC1fiyvJF66WHDM89BKzrvHWXFHutQ1QC8T8Fb36L_YE4fQ0GDDCc-1IP3x2k4AqQ_lBc20RNrlQ1dki5MWsorEapgrv9N1rzznPN2jIwFhzl00PxZbNr9bQOsADGCN8MvrVqgPiGscnDoREYlPZV4gBj3avgfEPZrYHFn3qLNe5qb0H3uD8jW7G2sW2XwYNTB1KlwdiF-3Sr0AXqn8M-J8ME1otaE5kZhTRco9jfGfqbLRETpWpfLC2cUTmNIL6niHIa9PR_8KJMQ52lr6BGn8ONFtpFOBfv1tXouaEQZT23gP7eCdRb7vIvxzHp1cGYz7jQkUO0rly011lOWi5zjm4EFhXQEu6AJAcgDzS448YA2YBaFu49AeF-wmmfL8GN4S67YETgpsCWonF7N7N3pe7ClMwPe84o1wwmPC4VjuxIat8O75rZtWQ2dtsKxdATJRJuiIOyYCGO4YlKoCyB3q3k535RaaHSlQ4oc1y6ewdRnbDg5Ro9qpdPNj8AzW1kvgWuRlSM9nS9_FIyQ58_vJXcw5Cyw_llotVHIWpnXIl91_vsqI86U-fcHhe7Ru4U-KUmUtNGEaDs5ZQzDg2jeOBA'
        }

    def cal_duration(self):
        _data = self.__item_data.get('Result', {})

        print('DATAAAAAAAAAAAA', _data)
        item_completed = _data.get('IsCompleted')
        item_duration = _data.get('CompleteDurationSec')
        item_played = _data.get('PlayDurationSec')
        item_iteration = random.randrange(5, 10)
        if item_completed:
            pass

        durr = item_duration - item_played
        time_skip = durr // self.__duration_need
        time_skip += 1  # For reminder

        if durr < 0:
            time_skip = 0

        self.__duration_skip = time_skip
        res = {'need': self.__duration_need, 'skip': time_skip, 'item_completed': item_completed,
               'item_duration': item_duration, 'item_played': item_played}
        print(res)
        return res

    def check_result(self):
        _data = self.__select_data_x
        print('THISIS DATAAAAAA_', _data)
        is_close = 'ViewGateway' in _data
        if is_close:
            print('Item content not already: Send Acknowledge')
            self.__get_view_gateway(_data)

        return is_close

    def __get_view_gateway(self, data):
        import requests

        url = f"https://vcubelms.com/beyondtrainingplus/Course/{data}"
        print(url)

        payload = {}
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'th,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Referer': f'https://vcubelms.com/beyondtrainingplus/Course/{data}',
            'Sec-Fetch-Dest': 'iframe',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41',
            'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }
        headers.update(self.__lazy_cookie)

        response = requests.request("GET", url, headers=headers, data=payload, verify=False)
        print(f'View Gateway Activate: [status_code={response.status_code}]')
        print(response.url)
        for i, h in enumerate(response.history):
            print(f'h_{str(i).zfill(2)}', h.url)

    def get_result(self):
        import requests

        url = "https://vcubelms.com/beyondtrainingplus/WebService/Course/CourseVideoService.asmx/GetResult"

        payload = f'{{"resultItemId":"{self.item_id}"}}'
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'th,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'DNT': '1',
            'Origin': 'https://vcubelms.com',
            'Referer': 'https://vcubelms.com/beyondtrainingplus/Course/ViewVideo.aspx?p=Hk5N2cJm1EAUjJFF9p%2fVkBVFpzf9WnZzVFButJ%2fSOq8Z6wBYTxkyrurv4nsjQ9xtqg%2bPpb7TuFXo%2b%2ftFYfiN7g%3d%3d',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }
        headers.update(self.__lazy_cookie)

        response = requests.request("POST", url, headers=headers, data=payload, verify=False)

        try:
            self.__item_data = response.json()
        except:
            print(headers)
            print(response.text)
            print(headers)
            raise Exception('Login Fails')

        print(self.__item_data)

    def set_dur(self):
        import requests

        url = "https://vcubelms.com/beyondtrainingplus/WebService/Course/CourseVideoService.asmx/SetVideoDurationSec"

        payload = f'{{"resultItemId":"{self.item_id}","durationIntervalSec":{self.__duration_need}}}'
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'th,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'DNT': '1',
            'Origin': 'https://vcubelms.com',
            'Referer': 'https://vcubelms.com/beyondtrainingplus/Course/ViewVideo.aspx?p=Hk5N2cJm1EAUjJFF9p%2fVkBVFpzf9WnZzVFButJ%2fSOq8Z6wBYTxkyrurv4nsjQ9xtqg%2bPpb7TuFXo%2b%2ftFYfiN7g%3d%3d',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }
        headers.update(self.__lazy_cookie)

        response = requests.request("POST", url, headers=headers, data=payload, verify=False)

        print(response.text)

    def select(self):
        import requests

        url = "https://vcubelms.com/beyondtrainingplus/WebService/Course/CourseService.asmx/Select"

        payload = f'{{"resultItemId":"{self.item_id}"}}'
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'th,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'DNT': '1',
            'Origin': 'https://vcubelms.com',
            'Referer': 'https://vcubelms.com/beyondtrainingplus/Course/ViewCourse.aspx?p=PKYiwAadC8sQGNJR7tIBdE49jPG3Vk7pPIZyyjLMiZ%2bSzCg10tvQXmlZyT75qPQvFIAwul9FyVCIM05w4gAzHedSqAzu1hESizGh4kR9E8gztlzEqJFcaFrj4URAendUYCMuFqD%2fmwp7YkdW6whbJDxI85GDLh11%2fQps8JSn85UbcykunJ4ZNI5Lw7orHLLVgXQeX1ixnbAVgLA10NkukLzYhWQBxCXeoc5pCQ8uIoQpBKXQ349B1GVw8KkMP428HAKj2efpnYOS0tBPKU%2b8E9ATqFjXm78Smd5WO%2bRBQR4k1sTj%2f9S4oSInlVI3B7NukbUMGwqfo3iOt8L9oVTamgh6KK%2fUbFxyPTpERKYmZoQ9vjrXX3Ctf%2bIRAZwz4OM5qO08xkdSUsXvOHeGtIOZMQ%3d%3d',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }
        headers.update(self.__lazy_cookie)

        response = requests.request("POST", url, headers=headers, data=payload, verify=False, allow_redirects=False)
        print(response.url)

        self.__select_data_x = response.json().get('Result')
        print(self.__select_data_x)


if __name__ == '__main__':
    with open('data/0201.json', encoding='utf8', mode='r') as fo:
        data = json.loads(fo.read())

    for d in data:
        print(d)
        item_id = d.get('ResultItemId')
        item_type = d.get('Type')

        learn = LazyLearnResource(item_id)

        show('-----------Select--------------')
        learn.select()
        print('-------CHeck------')
        learn.check_result()

        if item_type == 4:
            show('------RESULT--------')
            learn.get_result()
            show('--------DUR-------')
            cal = learn.cal_duration()
            skip_times = cal.get('skip')
            show(f'>> Skip {skip_times}')
            for ir in range(skip_times):
                learn.set_dur()

        slz_time = random.randrange(0, 2) + random.random()
        print('Sleep', slz_time)
        sleep(slz_time)
        print('-' * 50)
