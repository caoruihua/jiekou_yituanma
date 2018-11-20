# -*-coding:utf-8-*-
import self as self

__author__ = 'Administrator'
import json
import sys

import requests

sys.path.append('../..')

from lib.db import *
from lib.read_excel import *
from lib.case_log import log_case_info


class Login():
    def head():
        hearer = {"User-Agent": "ESEN/1.3.11 (iPhone; iOS 12.1; Scale/2.00)",
                  "Authorization": "Basic bW9iaWxlX25hdGl2ZV9hcHA6NjF3NFUyenJjQjg4",
                  "accept": "*/*",
                  "accept-encoding": "gzip,deflate,br",
                  "content-type": "application/x-www-form-urlencoded",
                  'accept-language': 'zh-Hans-CN;q=1',
                  'channel': 'IOS',
                  'app-sys-info': 'IOS;12.1',
                  'version': '1.3.11', }
        data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), "uaa")
        case_data = get_test_data(data_list, 'test_uaa_login_Correct')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        res = requests.post(url=url, data=data.encode(), headers=hearer)  # 用data=data 传字符串也可以
        log_case_info('test_uaa_login_wrong', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        token = res.json()["access_token"]
        token1 = "Bearer" + " " + token
        header6 = hearer
        header6["Authorization"] = token1
        header6["content-type"] = "application/json"
        return header6


