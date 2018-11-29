#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_22Setting.py
# @Author: Laocao
# @Date  : 2018-11-27

import json
import sys
import unittest

import requests

from lib.util import Login

sys.path.append('../..')

from lib.db import *
from lib.read_excel import *
from lib.case_log import log_case_info


class Setting(unittest.TestCase):
    u"""管理企业"""

    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"),
                                      "setting")  # 读取TestUserReg工作簿的所有数据
        cls.header7 = Login.head()

    def test_01_Setting_lizhi(self):
        u"""离职人员记录"""
        case_data = get_test_data(self.data_list, 'test_setting_lizhi')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_setting_lizhi', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_02_Setting_app(self):
        u"""app列表"""
        case_data = get_test_data(self.data_list, 'test_setting_app')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_setting_app', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_03_Setting_chat(self):
        u"""聊天水印开关"""
        case_data = get_test_data(self.data_list, 'test_setting_chat')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.put(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_setting_chat', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_04_Setting_words(self):
        u"""小白板水印开关"""
        case_data = get_test_data(self.data_list, 'test_setting_words')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.put(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_setting_words', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_05_Setting_task(self):
        u"""我的任务水印开关"""
        case_data = get_test_data(self.data_list, 'test_setting_task')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.put(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_setting_task', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_06_Setting_tag_CD(self):
        u"""创建删除标签"""
        case_data = get_test_data(self.data_list, 'test_setting_CreateTag')
        case_data1 = get_test_data(self.data_list, 'test_setting_DeleteTag')

        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        url1 = case_data1.get('url')
        data1 = case_data1.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res1 = case_data1.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        id = res.json()["id"]
        url2 = url1 + id
        res1 = requests.delete(url=url2, data=data1.encode(), headers=header8)  # 用data=data 传字符串也可以
        log_case_info('test_setting_DeleteTag', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res1.status_code, expect_res1)

    def test_07_Setting_Tags(self):
        u"""标签列表接口"""
        case_data = get_test_data(self.data_list, 'test_setting_Tags')

        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        log_case_info('test_setting_DeleteTag', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_08_Setting_Yaoqing(self):
        u"""仅管理员邀请新成员"""
        case_data = get_test_data(self.data_list, 'test_setting_yaoqing')

        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.put(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        log_case_info('test_setting_yaoqing', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_09_Setting_Remove(self):
        u"""仅管理员移除新成员"""
        case_data = get_test_data(self.data_list, 'test_setting_yichu')

        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.put(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        log_case_info('test_setting_yichu', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_10_Setting_Xiugai(self):
        u"""仅管理员可以修改团队名称"""
        case_data = get_test_data(self.data_list, 'test_setting_xiugai')

        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.put(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        log_case_info('test_setting_xiugai', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_11_Setting_RM(self):
        u"""移除管理员"""
        case_data = get_test_data(self.data_list, 'test_setting_Removeadmin')

        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        log_case_info('test_setting_Removeadmin', url, data, expect_res, res.text, ensure_ascii=False)
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_12_Setting_ADD(self):
        u"""添加管理员"""
        case_data = get_test_data(self.data_list, 'test_setting_Adddadmin')

        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        log_case_info('test_setting_Removeadmin', url, data, expect_res, res.text,ensure_ascii=False)
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)


if __name__ == '__main__':
    unittest.main(verbosity=2, retry=2)  # 运行所有用例
