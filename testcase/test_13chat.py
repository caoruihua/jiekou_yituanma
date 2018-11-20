#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_13chat.py
# @Author: Feng
# @Date  : 2018/11/2
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


class Chat(unittest.TestCase):
    u"""IM相关"""

    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), "chat")  # 读取TestUserReg工作簿的所有数据
        cls.header7=Login.head()

    def test_01chat_create(self):
        u"""创建群聊"""
        case_data = get_test_data(self.data_list, 'test_chat_create')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8=self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_chat_create', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_02chat_Gaiming(self):
        u"""群组改名"""
        case_data = get_test_data(self.data_list, 'test_chat_GaiMing')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.put(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_chat_GaiMing', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_03chat_AddMember(self):
        u"""添加群组成员"""
        case_data = get_test_data(self.data_list, 'test_chat_AddMember')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.put(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_chat_AddMember', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_04chat_RmoveMember(self):
        u"""删除群组成员"""
        case_data = get_test_data(self.data_list, 'test_chat_RemoveMember')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.delete(url=url, headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_chat_RemoveMember', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_05chat_leave(self):
        u"""创建退出群聊"""
        case_data = get_test_data(self.data_list, 'test_chat_create')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查

        # 退出群组数据
        case_data1 = get_test_data(self.data_list, 'test_chat_leave')
        url1 = case_data1.get('url')
        data1 = case_data1.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res1 = case_data1.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7

        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        id = res.json()["id"]
        res1 = requests.get(url=url1 + id, data=data1.encode(), headers=header8)
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_chat_leave', url1, data1, expect_res1, json.dumps(res1.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res1.status_code, expect_res1)

    def test_06chat_ChangeOnwer(self):
        u"""转让群管理员"""
        case_data = get_test_data(self.data_list, 'test_chat_create')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查

        # 退出群组数据
        case_data1 = get_test_data(self.data_list, 'test_chat_ChangeOnwer')
        url1 = case_data1.get('url')
        expect_res1 = case_data1.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        data1 = case_data1.get('data')
        dict = json.loads(data1)
        header8 = self.header7

        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        id = res.json()["imGroupId"]
        dict['groupId'] = id
        res1 = requests.post(url=url1, data=json.dumps(dict), headers=header8)
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_chat_leave', url1, dict, expect_res1, json.dumps(res1.json(), ensure_ascii=False))
        #   响应断言（整体断言）
        self.assertEqual(res1.status_code, expect_res1)


if __name__ == '__main__':
    unittest.main(verbosity=2)  # 运行所有用例
