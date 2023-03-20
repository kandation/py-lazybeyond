import json

with open('data/0101.json', encoding='utf8', mode='r') as fo:
    data = json.dumps(fo.read())

class LazyLearnResource:
    def __init__(self):
        pass

    def get_result(self):
        import requests

        url = "https://vcubelms.com/beyondtrainingplus/WebService/Course/CourseVideoService.asmx/GetResult"

        payload = "{\"resultItemId\":\"cd2da212-a2bf-4b95-8903-c409b648bcb9\"}"
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'th,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'Cookie': 'ASP.NET_SessionId=wf1ahfw5sj1jogfz3sxy0dec; G_ENABLED_IDPS=google; __AntiXsrfToken=ea170191fe40417b9c307fbcf404e912; .AspNet.ApplicationCookie=9d6dmoPg6iX9J-Cq6THUMRh6P8lhiaCELO5Fp8AlOoLe90C0eYpbPBXvlRdU6ZXiWiTQGyVmWPeTPtayb8Xgln8k7sTbq-SCkC6Fy9EIvFdFFpqxnmrDYgDtkJkzKjY6kX7q03vzOAymNZwKzEprYt4WcSWpC4_1oUlyu5lz--jGhvoMiDwzJODdTinL4mIntASLnFiERtWy1ep-DnFecGl4E3Bf2fwg2qbNnpnRhlONF5Wz2bp3qSaNZj5M0sfM2xSRLN1_QuzMTLBkSSTHdwYJFwnZub8DrVwy3PGl-EVFDzlA9Hd6CN31Kbqf64kBpbngUmiUy016RvDYVw9fk-tjk8enevogib3eXhivhh-D48vPeJUrOHWQoj1mEnIijfXQ9x3lfJ_tI9LypKx7nM52C2iD7wRsKP2PSl6s9GxsLcjOr4K-KoC4CjtuJEg-5NiUXEkmsuMlidQ_Awb-moIEVi03bHQEa7ZDKIP_UbzfSU-zRzIyVtVzL3NL_fKMhN63Cwg5tsXk3FrWefqlNZinXk4CQvE8DMmma7LX2Qd_83o3rBPwCPLgFx0uFIUDaIgx6O8vx1jCisiDxGB-kTNYwqWaoguQGsZqlcUQBGoPOw4BG_8b3fyT8xoUfg9Y3ybCtkhgeShx6KcabhjJ4t3lmwHdxBYboKbryrbBr4ywMWHLhu9Go8yZkeQRRi-AJBiDbw',
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

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def set_dur(self):
        import requests

        url = "https://vcubelms.com/beyondtrainingplus/WebService/Course/CourseVideoService.asmx/SetVideoDurationSec"

        payload = "{\"resultItemId\":\"cd2da212-a2bf-4b95-8903-c409b648bcb9\",\"durationIntervalSec\":100}"
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'th,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'Cookie': 'ASP.NET_SessionId=wf1ahfw5sj1jogfz3sxy0dec; G_ENABLED_IDPS=google; __AntiXsrfToken=ea170191fe40417b9c307fbcf404e912; .AspNet.ApplicationCookie=9d6dmoPg6iX9J-Cq6THUMRh6P8lhiaCELO5Fp8AlOoLe90C0eYpbPBXvlRdU6ZXiWiTQGyVmWPeTPtayb8Xgln8k7sTbq-SCkC6Fy9EIvFdFFpqxnmrDYgDtkJkzKjY6kX7q03vzOAymNZwKzEprYt4WcSWpC4_1oUlyu5lz--jGhvoMiDwzJODdTinL4mIntASLnFiERtWy1ep-DnFecGl4E3Bf2fwg2qbNnpnRhlONF5Wz2bp3qSaNZj5M0sfM2xSRLN1_QuzMTLBkSSTHdwYJFwnZub8DrVwy3PGl-EVFDzlA9Hd6CN31Kbqf64kBpbngUmiUy016RvDYVw9fk-tjk8enevogib3eXhivhh-D48vPeJUrOHWQoj1mEnIijfXQ9x3lfJ_tI9LypKx7nM52C2iD7wRsKP2PSl6s9GxsLcjOr4K-KoC4CjtuJEg-5NiUXEkmsuMlidQ_Awb-moIEVi03bHQEa7ZDKIP_UbzfSU-zRzIyVtVzL3NL_fKMhN63Cwg5tsXk3FrWefqlNZinXk4CQvE8DMmma7LX2Qd_83o3rBPwCPLgFx0uFIUDaIgx6O8vx1jCisiDxGB-kTNYwqWaoguQGsZqlcUQBGoPOw4BG_8b3fyT8xoUfg9Y3ybCtkhgeShx6KcabhjJ4t3lmwHdxBYboKbryrbBr4ywMWHLhu9Go8yZkeQRRi-AJBiDbw',
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

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
