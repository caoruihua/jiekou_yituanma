#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_14CRS.py
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


class CRS(unittest.TestCase):
    u"""客户管理"""

    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), "CRS")  # 读取TestUserReg工作簿的所有数据
        cls.header7=Login.head()

    def test_01CRS_Customer(self):
        u"""客户列表"""
        case_data = get_test_data(self.data_list, 'test_CRS_Customer')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8=self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_CRS_Customer', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_02CRS_Customer_Datail(self):
        u"""客户详情"""
        case_data = get_test_data(self.data_list, 'test_CRS_CustomerDatail')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_CRS_CustomerDatail', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_03CRS_Customer_Feedback(self):
        u"""客户反馈"""
        case_data = get_test_data(self.data_list, 'test_CRS_CustomerFeedback')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_CRS_Customerfeedback', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_04CRS_Customer_create(self):
        u"""创建客户失败"""
        case_data = get_test_data(self.data_list, 'test_CRS_Customer_Create')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_CRS_Customer_Create', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_05CRS_Customer_Area(self):
        u"""客户所在地域"""
        case_data = get_test_data(self.data_list, 'test_CRS_Customer_Area')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_CRS_Customer_Area', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_06CRS_Customer_level(self):
        u"""客户登记"""
        case_data = get_test_data(self.data_list, 'test_CRS_levellist')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_CRS_levellist', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_07CRS_SourceList(self):
        u"""客户获取渠道"""
        case_data = get_test_data(self.data_list, 'test_CRS_sourcelist')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_CRS_sourcelist', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_08CRS_TradeList(self):
        u"""客户领域"""
        case_data = get_test_data(self.data_list, 'test_CRS_tradelist')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_CRS_tradelist', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_09CRS_contact(self):
        u"""CRS-联系人"""
        case_data = get_test_data(self.data_list, 'test_CRS_contact')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_CRS_contact', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_10CRS_Contact_C_D(self):
        u"""创建删除联系人信息"""
        case_data = get_test_data(self.data_list, 'test_CRS_contact_Create')
        case_data1 = get_test_data(self.data_list, 'test_CRS_contact_detele')
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
        id = res.json()["id"]  # 获取创建的id
        res1 = requests.delete(url=url1 + id, data=data1.encode(), headers=header8)
        log_case_info('test_CRS_contact_create', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))

        log_case_info('test_CRS_contact_detele', url1 + id, data1, expect_res1, res1.text)
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)
        self.assertEqual(res1.status_code, expect_res1)

    def test_11CRS_market(self):
        u"""查看市场信息"""
        case_data = get_test_data(self.data_list, 'test_CRS_market')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_CRS_market', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_12CRS_market_create(self):
        u"""CRS-创建市场信息"""
        case_data = get_test_data(self.data_list, 'test_CRS_market_create')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_CRS_market_create', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_13CRS_SPM_shangji(self):
        u"""销售商机"""
        case_data = get_test_data(self.data_list, 'test_CRS_spm_shangji')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_CRS_spms_hangji', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_14CRS_SPM_xiansuo(self):
        u"""查看销售线索"""
        case_data = get_test_data(self.data_list, 'test_CRS_spm_xiansuo')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_CRS_spm_xiansuo', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_15CRS_customr_teammber(self):
        u"""查看负责客户的任务"""
        case_data = get_test_data(self.data_list, 'test_CRS_customer_teammember')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_CRS_customer_teammber', url, data, expect_res, json.dumps(res.json()), ensure_ascii=False)
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_16CRS_customr_tasklist(self):
        u"""查看负责客户的任务"""
        case_data = get_test_data(self.data_list, 'test_CRS_customer_tasklist')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_CRS_customer_tasklist', url, data, expect_res, json.dumps(res.json()), ensure_ascii=False)
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_17CRS_customr_record(self):
        u"""添加客户服务记录"""
        case_data = get_test_data(self.data_list, 'test_CRS_customer_record')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_CRS_customer_record', url, data, expect_res, json.dumps(res.json()), ensure_ascii=False)
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_18CRS_relitu(self):
        u"""热力图"""
        case_data = get_test_data(self.data_list, 'test_CRS_relitu')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_CRS_relitu', url, data, expect_res, json.dumps(res.json()), ensure_ascii=False)
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_19CRS_Cus_level(self):
        u"""基础设置-客户默认等级设置"""
        case_data = get_test_data(self.data_list, 'test_CRS_cus_level')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_CRS_cus_level', url, data, expect_res, json.dumps(res.json()), ensure_ascii=False)
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_21CRS_Cus_level_list(self):
        u"""基础设置-客户等级列表"""
        case_data = get_test_data(self.data_list, 'test_CRS_cus_level_list')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_CRS_cus_level_list', url, data, expect_res, json.dumps(res.json()), ensure_ascii=False)
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_22CRS_Cus_Master_permission(self):
        u"""基础设置-管理员权限设置"""
        case_data = get_test_data(self.data_list, 'test_CRS_cus_master_permission')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_CRS_cus_master_permission', url, data, expect_res, json.dumps(res.json()),
                      ensure_ascii=False)
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_23CRS_Cus_Mycus(self):
        u"""我的所有客户列表"""
        case_data = get_test_data(self.data_list, 'test_CRS_cus_my_cus')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_CRS_cus_my_cus', url, data, expect_res, json.dumps(res.json()), ensure_ascii=False)
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_24CRS_Source_C_D(self):
        u"""创建删除客户来源信息"""
        case_data = get_test_data(self.data_list, 'test_CRS_source_create')
        case_data1 = get_test_data(self.data_list, 'test_CRS_source_delete')
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
        id = res.json()["id"]  # 获取创建的id
        res1 = requests.delete(url=url1 + id, data=data1.encode(), headers=header8)
        log_case_info('test_CRS_source_create', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))

        log_case_info('test_CRS_source_delete', url1 + id, data1, expect_res1, res1.text)
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)
        self.assertEqual(res1.status_code, expect_res1)

    def test_25CRS_Cus_C_D(self):
        u"""创建删除客户信息"""
        case_data = get_test_data(self.data_list, 'test_CRS_cus_create')
        case_data1 = get_test_data(self.data_list, 'test_CRS_cus_delete')
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
        id = res.json()["id"]  # 获取创建的id
        res1 = requests.delete(url=url1 + id, data=data1.encode(), headers=header8)
        log_case_info('test_CRS_cus_create', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))

        log_case_info('test_CRS_cus_delete', url1 + id, data1, expect_res1, res1.text)
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)
        self.assertEqual(res1.status_code, expect_res1)


if __name__ == '__main__':
    unittest.main(verbosity=2)  # 运行所有用例
