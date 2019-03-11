import json
import sys
import unittest

import requests

from lib.util import Login

sys.path.append('../..')
from lib.db import *
from lib.read_excel import *
from lib.case_log import log_case_info


class TestTask(unittest.TestCase):
    u"""我的任务"""

    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"), "Task")  # 读取TestUserReg工作簿的所有数据
        cls.header7=Login.head()

    def test_01looktask(self):
        u"""进入我的任务"""
        case_data = get_test_data(self.data_list, 'test_looktask')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8=self.header7
        res = requests.get(url=url, headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_user_reg_normal', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_02todo(self):
        u"""进入我的待办"""
        case_data = get_test_data(self.data_list, 'test_todo')
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

    def test_03outdo(self):
        u"""进入我派发的"""
        case_data = get_test_data(self.data_list, 'test_outdo')
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

    def test_04toverify(self):
        u"""进入我的验证"""
        case_data = get_test_data(self.data_list, 'test_toverify')
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

    def test_05optin(self):
        u"""进入设置菜单"""
        case_data = get_test_data(self.data_list, 'test_gtd_option')
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

    def test_06createtask(self):
        u"""创建任务"""
        case_data = get_test_data(self.data_list, 'test_create_task')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_07words_task(self):
        u"""小白板转任务"""
        case_data = get_test_data(self.data_list, 'test_words_task')
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

    def test_08task_defaultverify(self):
        """默认验证人设置"""
        case_data = get_test_data(self.data_list, 'test_task_defaultverify')
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

    def test_09task_log(self):
        """查看task日志"""
        case_data = get_test_data(self.data_list, 'test_task_log')
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

    def test_10task_participators(self):
        """查看task参与人"""
        case_data = get_test_data(self.data_list, 'test_task_participators')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，
        header8 = self.header7
        res = requests.get(url=url, headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_user_reg_normal', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_11deletetask(self):
        u"""创建删除任务"""
        case_data = get_test_data(self.data_list, 'test_create_task')  # 创建任务的接口
        case_data1 = get_test_data(self.data_list, 'test_task_delete')  # 删除任务的接口
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')

        url1 = case_data1.get('url')

        expect_res1 = case_data1.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        taskid = res.json()["id"]
        res1 = requests.delete(url=url1 + taskid, headers=header8)
        log_case_info('test_user_deletetask', url, data, expect_res1, res1.text)
        self.assertEqual(res.status_code, expect_res1)  # 断言

    def test_11task_redo(self):
        """重新启动任务"""
        case_data = get_test_data(self.data_list, 'test_task_redo')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_task_redo', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_12task_cancel(self):
        """取消任务"""
        case_data = get_test_data(self.data_list, 'test_task_cancel')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_task_cancel', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_13task_ok(self):
        u"""任务审核通过"""
        case_data = get_test_data(self.data_list, 'test_create_task')  # 创建任务的接口
        case_data1 = get_test_data(self.data_list, 'test_task_ok')  # 删除任务的接口
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')

        url1 = case_data1.get('url')
        data1 = case_data1.get('data')

        expect_res1 = case_data1.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        taskid = res.json()["id"]
        res1 = requests.post(url=url1 + taskid + "/action", data=data1.encode(), headers=header8)
        log_case_info('test_user_ok', url, data, expect_res1, res1.text)
        self.assertEqual(res1.status_code, expect_res1)  # 断言

    def test_14task_reject(self):
        u"""任务审核不通过"""
        case_data = get_test_data(self.data_list, 'test_create_task')  # 创建任务的接口
        case_data1 = get_test_data(self.data_list, 'test_task_reject')  # 删除任务的接口
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')

        url1 = case_data1.get('url')
        data1 = case_data1.get('data')

        expect_res1 = case_data1.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        taskid = res.json()["id"]
        res1 = requests.post(url=url1 + taskid + "/action", data=data1.encode(), headers=header8)
        log_case_info('test_user_reject', url, data, expect_res1, res1.text)
        self.assertEqual(res1.status_code, expect_res1)  # 断言

    def test_15task_finish(self):
        u"""关闭任务"""
        case_data = get_test_data(self.data_list, 'test_create_task')  # 创建任务的接口
        case_data1 = get_test_data(self.data_list, 'test_task_finish')  # 删除任务的接口
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')

        url1 = case_data1.get('url')
        data1 = case_data1.get('data')

        expect_res1 = case_data1.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        taskid = res.json()["id"]
        res1 = requests.post(url=url1 + taskid + "/action", data=data1.encode(), headers=header8)
        log_case_info('test_user_reject', url, data, expect_res1, res1.text)
        self.assertEqual(res1.status_code, expect_res1)  # 断言

    def test_16task_tags(self):
        """给任务打标签"""
        case_data = get_test_data(self.data_list, 'test_task_tags')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.put(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_task_tags', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_16task_RuleByTime(self):
        """带我验证按创建时间排序"""
        case_data = get_test_data(self.data_list, 'test_task_rule_bytime')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_task_rule_bytime', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_17task_Dashboard(self):
        """查看GTD数据看板"""
        case_data = get_test_data(self.data_list, 'test_task_dashboard')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_task_dashboard', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_18task_Remind(self):
        """指定时间提醒设置"""
        case_data = get_test_data(self.data_list, 'test_task_remind')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_task_remind', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_19task_AutoRuler(self):
        u"""自动规则设置"""
        case_data = get_test_data(self.data_list, 'test_task_Zidongguize')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_task_Zidongguize', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_20task_Myjoin(self):
        u"""自动规则设置"""
        case_data = get_test_data(self.data_list, 'test_task_myjoin')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_task_myjoin', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_21task_Associatin(self):
        u"""编辑任务归属团队"""
        case_data = get_test_data(self.data_list, 'test_task_Association')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.put(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_task_Association', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)

    def test_21task_Homepage(self):
        u"""任务主页"""
        case_data = get_test_data(self.data_list, 'test_task_homepage')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')  # 转为字典，需要取里面的name进行数据库检查
        expect_res = case_data.get('expect_res')  # 转为字典，断言时直接断言两个字典是否相等
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)  # 用data=data 传字符串也可以
        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        log_case_info('test_task_homepage', url, data, expect_res, json.dumps(res.json(), ensure_ascii=False))
        # 响应断言（整体断言）
        self.assertEqual(res.status_code, expect_res)





if __name__ == '__main__':
    unittest.main(verbosity=2)  # 运行所有用例
