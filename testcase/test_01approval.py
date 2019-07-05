# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_05GTP.py
# @Author: Feng
# @Date  : 2018/11/1
# @Desc  :


import json
import sys
import unittest

import requests
from jsonpath import jsonpath

from lib.case_log import log_case_info
from lib.db import *
from lib.read_excel import *
from lib.util import Login

sys.path.append('../..')


class TestApproval(unittest.TestCase):
    u"""审批相关"""

    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"),
                                      "approval")  # 读取TestUserReg工作簿的所有数据
        cls.header7 = Login.head()

    def test__01ApprovalList(self):
        u"""查看所有审批"""
        case_data = get_test_data(self.data_list, 'test__ApprovalList')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_user_approvalist', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test__02find_approval_by_id(self):
        u"""查看指定审批"""
        case_data = get_test_data(self.data_list, 'test__find_approval_by_id')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7

        res = requests.get(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_find_approval_by_id', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test__03find_approval_Chaosong(self):
        u"""查看指定审批"""
        case_data = get_test_data(self.data_list, 'test__find_approval_chaosongme')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test__find_approval_chaosongme', url, data, expect_res,
                      json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test__04find_approval_my_shenqing(self):
        u"""查看我申请的"""
        case_data = get_test_data(self.data_list, 'test__find_approval_my_shenqing')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_find_approval_my_shenqing', url, data, expect_res,
                      json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test__05find_approval_chaosongme(self):
        u"""查看抄送我的审批"""
        case_data = get_test_data(self.data_list, 'test__find_approval_chaosongme')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_approval_chaosongme', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test__06find_approval_my_shenpi(self):
        u"""查看我申请的"""
        case_data = get_test_data(self.data_list, 'test__find_approval_my_shenpi')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_find_approval_my_shenpi', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test__07approval_template(self):
        u"""查看我申请的"""
        case_data = get_test_data(self.data_list, 'test__approval_template')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_approval_template', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test__08approval_create(self):
        u"""查看我申请的"""
        case_data = get_test_data(self.data_list, 'test__approval_create')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_approval_create', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        apid = res.json()["id"]
        print('apid:' + apid)
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test__09approval_ok(self):
        u"""审批通过"""
        case_data = get_test_data(self.data_list, 'test__approval_create')
        case_data1 = get_test_data(self.data_list, 'test__approval_submmit_ok')

        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7

        res = requests.post(url=url, data=data.encode(), headers=header8).text  # 用data=data 传字符串也可以
        print(type(res))
        ree=json.loads(res)
        re, *_ = jsonpath(ree, '$.process.items.APPROVE[?(@.id)]') or (None)  #通过jsonpath匹配
        id = re['id']
        url1 = case_data1.get('url')
        data1 = case_data1.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res1 = case_data1.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        url2 = url1 + id + '/passed'
        print(url2)
        res1 = requests.put(url=url2, data=data.encode(), headers=header8)
        print(res1.status_code)
        log_case_info('test__approval_submmit_ok', url1, data1, expect_res1,res, ensure_ascii=False)
        self.assertEqual(res1.status_code, expect_res1)

    def test__10approval_over(self):
        u"""查看已完成的审批"""
        case_data = get_test_data(self.data_list, 'test__approval_over')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_approval_over', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        self.assertEqual(res.status_code, expect_res)

    def test__11approval_draft(self):
        u"""审批保存为草稿"""
        case_data = get_test_data(self.data_list, 'test__approval_draft')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.put(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test__approval_draft', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        self.assertEqual(res.status_code, expect_res)

    def test__12approval_savedraft(self):
        u"""审批保存为草稿"""
        case_data = get_test_data(self.data_list, 'test__approval_draft')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.put(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test__approval_draft', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        self.assertEqual(res.status_code, expect_res)

    def test__13approval_Draftlist(self):
        u"""审批草稿箱首页"""
        case_data = get_test_data(self.data_list, 'test__approval_draftlist')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test__approval_draftlist', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        self.assertEqual(res.status_code, expect_res)

    def test__14approval_chehui(self):
        u"""撤回审批"""
        case_data = get_test_data(self.data_list, 'test__approval_create')
        case_data1 = get_test_data(self.data_list, 'test__approval_chehui')

        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        header8 = self.header7

        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        time.sleep(1)
        id = res.json()["id"]
        print(type(id))
        url1 = case_data1.get('url')
        data1 = case_data1.get('data')  # 转为字典，需要取里面的name进行数据库检查
        url2 = url1 + id + "/cancel"
        expect_res1 = case_data1.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        res1 = requests.put(url=url2, data=data1.encode(), headers=header8)  # 用data=data 传字符串也可以
        log_case_info('test_approval_chehui', url1, data1, expect_res1, json.dumps(res.json(), ensure_ascii=False))
        self.assertEqual(res1.status_code, expect_res1)


if __name__ == '__main__':
    unittest.main(verbosity=2)  # 运行所有用例
