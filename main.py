import os
from pprint import pprint
import random
from time import sleep

from beyondLazyLearn import LazyLearnResource
from beyondLean import CredencialType, BeyondLazy, SessionManager, BeyondLazyApi
from dotenv import load_dotenv

from utils import show

load_dotenv()
if __name__ == '__main__':
    """
    > Login 
    > Take Some Course
    > Learn first chapter and do pre-test
    > Run script GGEZ
    """

    # Recommended: Use Cookie browser [see manual at convert_browser_cookies]
    credential_type = CredencialType.USE_BROWSER_COOKIE

    print('Login type:: ', credential_type)

    env_user = os.getenv('BEYOND_USERNAME')
    env_pass = os.getenv('BEYOND_PASSWORD')
    print(f'Login by {env_user} {env_pass}')

    b = BeyondLazy(env_user, env_pass)
    if credential_type == CredencialType.USE_LOGIN:
        b.login()

    b_session = b.get_session()
    session = SessionManager()

    if credential_type == CredencialType.USE_LOGIN:
        session.save(b_session)

    session.load()
    r_session = session.get_session()

    bx = BeyondLazyApi(r_session)
    t = bx.check_cookie()
    print(t)

    pp = bx.get_tasks()
    pprint(pp)

    '''
    > GetTask [getUrl, TaskId]
    > Start(uri)
    > ViewCourse(uri): [resultId]
    '''
    task_id, result_uri = bx.get_task_by_index(0)
    print(f'TaskId {task_id} , URI  {result_uri}')

    bx.get_start()

    result_id = bx.get_view_course()
    rex = bx.take(result_id, result_uri)
    sections = rex.get('Result', {}).get('Sections', {})

    show('====Section====')
    pprint(sections)

    selected_sec = sections[1] or {}
    sel_items = selected_sec.get('ResultItems')

    show('===== Selected Items ====')
    pprint(sel_items)

    show('==== Learn ====')


    for d in sel_items:
        print(d)
        item_id = d.get('ResultItemId')
        item_type = d.get('Type')

        learn = LazyLearnResource(item_id, r_session)
        learn.set_duration_need(10)

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
                learn.send_fake_learn_duration()

        slz_time = random.randrange(0, 2) + random.random()
        print('Sleep', slz_time)
        sleep(slz_time)
        print('-' * 50)
