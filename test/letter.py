import unittest
import requests
import json
import sys
import os
sys.path.append('../..')

from config.config import *
from lib.db import *
from lib.read_excel import *
from lib.case_log import log_case_info



class TestTask(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), "letter")  # 读取TestUserReg工作簿的所有数据

    def test_01letter_someone(self):
        u'''查看自己的感谢信状态'''
        case_data = get_test_data(self.data_list, 'test_user_letter_someone')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        res = requests.get(url=url,headers=hearder2)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_user_letter_someone', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)


    def test_02letter_oneday(self):
        u'''查看某一天感谢信动态'''
        case_data = get_test_data(self.data_list, 'test_user_letter_oneday')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        res = requests.get(url=url,headers=hearder2)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_user_letter_oneday', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)



    def test_03letter_history(self):
        u'''查看历史感谢信记录'''
        case_data = get_test_data(self.data_list, 'test_user_letter_history')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url') # excel中的标题也必须是小写url
        data=case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.get(url=url,  headers=hearder2)
        log_case_info('test_user_letter_history', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_04letter_month(self):
        u'''感谢信月度排行榜'''
        case_data = get_test_data(self.data_list, 'test_user_letter_month')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.get(url=url, headers=hearder2)
        log_case_info('test_user_letter_month', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_05letter_quarter(self):
        u'''查看感谢信季度排行榜'''
        case_data = get_test_data(self.data_list, 'test_user_letter_quarter')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.get(url=url, headers=hearder2)
        log_case_info('test_user_letter_quarter', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_05letter_year(self):
        u'''查看感谢信年度排行榜'''
        case_data = get_test_data(self.data_list, 'test_user_letter_year')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.get(url=url, headers=hearder2)
        log_case_info('test_user_letter_year', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言


    def test_05letter_save(self):
        u'''查看感谢信年度排行榜'''
        case_data = get_test_data(self.data_list, 'test_user_letter_save')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.post(url=url, data=data.encode(), headers=hearder2)
        log_case_info('test_user_letter_save', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言




if __name__ == '__main__':
    unittest.main(verbosity=2)  # 运行所有用例
