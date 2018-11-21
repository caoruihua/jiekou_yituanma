#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_06out.py
# @Author: Fang
# @Date  : 2018/10/31
# @Desc  :

import json
import sys
import unittest

import requests

from lib.util import Login

sys.path.append('../..')

from lib.db import *
from lib.read_excel import *
from lib.case_log import log_case_info


class Qingjia(unittest.TestCase):
    u"""我的外出"""

    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), "out")  # 读取TestUserReg工作簿的所有数据
        cls.header7 = Login.head()

    def test_01_outrecord(self):
        u"""外出请假记录"""
        case_data = get_test_data(self.data_list, 'test_user_hr_waichu')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_user_reg_normal', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_02_hr_worktime(self):
        u"""查看工作时间"""
        case_data = get_test_data(self.data_list, 'test_user_hr_worktime')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_user_hr_worktime', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_03_hr_outnow(self):
        u"""当前人员外出状态"""
        case_data = get_test_data(self.data_list, 'test_user_hr_Out_now')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_user_hr_Outnow', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_04_hr_outnow(self):
        u"""当日申请汇总"""
        case_data = get_test_data(self.data_list, 'test_user_hr_Out_today')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_user_hr_Outtoday', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_05_hr_Outingreport(self):
        u"""外出-我的报表"""
        case_data = get_test_data(self.data_list, 'test_user_hr_Outingreport')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_user_hr_Outingreport', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_06_hr_OutCreate_Cancle(self):
        u"""创建取消外出"""
        case_data = get_test_data(self.data_list, 'test_user_hr_Out_Create')
        case_data1 = get_test_data(self.data_list, 'test_user_hr_Out_Cancel')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        url1 = case_data1.get('url')
        data1 = case_data1.get('data')
        expect_res1 = case_data1.get('expect_res')
        header8 = self.header7
        header8['accept'] = 'application/json, text/plain, */*'
        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        id = res.json()["id"]
        res1 = requests.get(url=url1 + id, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以

        log_case_info('test_user_hr_Out_Cancel', url1, data1, expect_res1, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res1.status_code, expect_res1)


if __name__ == '__main__':
    unittest.main(verbosity=2)  # 运行所有用例
