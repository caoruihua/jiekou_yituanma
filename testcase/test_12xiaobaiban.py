import json
import sys
import unittest

import requests

from lib.util import Login

sys.path.append("../..")  # 提升2级到项目根目录下
from config.config import *  # 从项目路径下导入
from lib.read_excel import *  # 从项目路径下导入
from lib.case_log import log_case_info  # 从项目路径下导入


class TestXiaobaiban(unittest.TestCase):
    u"""小白板"""

    @classmethod
    def setUpClass(cls):  # 整个测试类只执行一次
        cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"),
                                      "TestXiaobaiban")  # 读取TestUserReg工作簿的所有数据
        cls.header7 = Login.head()

    def test_02xiaobaiban_coment(self):
        u"""小白板评论"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_coment')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7

        res = requests.post(url=url, data=data.encode(), headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_03xiaobaiban_cainajianyi(self):
        u"""采纳建议"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_cainajianyi')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_04xiaobaiban_quxiaocaina(self):
        u"""取消采纳建议"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_quxiaocaina')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_05xiaobaiban_yidu(self):
        u"""小白板已读"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_yidu')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_06xiaobaiban_weidu(self):
        u"""小白板未读"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_weidu')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_07xiaobaiban_remind(self):
        u"""提醒阅读"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_remind')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_08xiaobaiban_kudos(self):
        u"""点赞"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_kudos')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_09xiaobaiban_unkudos(self):
        u"""取掉点赞"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_unkudos')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_10xiaobaiban_collect(self):
        u"""小白板收藏"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_collect')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_11xiaobaiban_collect_cancel(self):
        u"""小白板取消收藏"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_collect_cancel')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_12xiaobaiban_search(self):
        u"""小白板搜索"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_search')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_13xiaobaiban_looktaolun(self):
        u"""查看讨论人数"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_looktaolun')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_15xiaobaiban_groupmember(self):
        u"""查看团队成员"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_groupmember')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_17xiaobaiban_jielun(self):
        u"""形成结论"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_jielun')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_18xiaobaiban_search(self):
        u"""小白板筛选"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_shaixuan')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_19xiaobaiban_comenlaste(self):
        u"""查看团队成员"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_comenlaste')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_20xiaobaiban_mremind(self):
        u"""小白板提醒"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_mremind')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_21xiaobaiban_CRS(self):
        u"""查看CRS"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_CRS')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_23xiaobaiban_log(self):
        u"""查看小白板日志"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_log')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_24xiaobaiban_tag(self):
        u"""小白板标签"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_tag')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_25xiaobaiban_show_new_v2(self):
        u"""未读角标接口"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_show-new-v2')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_26xiaobaiban_wechat(self):
        u"""小白板转微信"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_wechat')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_26xiaobaiban_remindself(self):
        u"""小白板提醒自己"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_remindself')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_27xiaobaiban_simple(self):
        u"""小白板提醒自己"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_simple')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, headers=header8)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_28xiaobaiban_shenpichajian(self):
        u"""小白板审批插件"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_templates')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, headers=header8)
        log_case_info('test_xiaobaiban_templates', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_29xiaobaiban_tongzhi(self):
        u"""小白板通知开启"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_templates')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, headers=header8)
        log_case_info('test_xiaobaiban_tongzhi', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_30xiaobaiban_badge(self):
        u"""重置侧滑栏"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_badge')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, headers=header8)
        log_case_info('test_xiaobaiban_badge', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_31xiaobaiban_C_D(self):
        u"""创建删除带各种标签的小白板"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_create_delete')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        time.sleep(2)
        id = res.json()["id"]  # 动态获取id
        res2 = requests.get(
            url="https://gateway.workdesk.esenyun.com:9091/words/openapi/words/destroy/" + id + "?groupId=",
            headers=header8)
        log_case_info('test_xiaobaiban_badge', url, data, expect_res, res2.text)
        print(id)
        self.assertEqual(res2.status_code, expect_res)  # 断言

    def test_32xiaobaiban_deletePinglun(self):
        u"""创建删除评论"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_create_common')  # 从数据列表中查找到该用例数据
        case_data1 = get_test_data(self.data_list, 'test_xiaobaiban_delete_common')
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # 创建数据接口
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据

        url1 = case_data1.get('url')  # 删除数据接口
        data1 = case_data1.get('data')
        expect_res1 = case_data.get('expect_res')  # 期望数据
        header8 = self.header7

        res = requests.post(url=url, data=data.encode(), headers=header8)
        time.sleep(2)
        id = res.json()["id"]  # 动态获取id
        res2 = requests.get(url=url1 + id + "?groupId=", headers=header8)
        log_case_info('test_deleteconment', url1, data1, expect_res1, res2.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_33xiaobaiban_coment(self):
        u"""小白板评论上传图片"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_coment_picture')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7

        res = requests.post(url=url, data=data.encode(), headers=header8)
        log_case_info('ttest_xiaobaiban_coment_picture', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_34xiaobaiban_tongzhi(self):
        u"""小白板标签相关"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_markers')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        log_case_info('test_xiaobaiban_markers', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_35xiaobaiban_Dashboard_Increase(self):
        u"""小白板日增量报告"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_increase')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)
        log_case_info('test_xiaobaiban_increase', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_36xiaobaiban_Dashboard_Mycreate(self):
        u"""七天内我发布的小白板"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_mycreate')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)
        log_case_info('test_xiaobaiban_mycreate', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_37xiaobaiban_Dashboard_Myreply(self):
        u"""我回复的小白板数据"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_myreply')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)
        log_case_info('test_xiaobaiban_myreplay', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_38xiaobaiban_Dashboard_Mycollect(self):
        u"""我收藏的小白板数据"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_mycollect')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)
        log_case_info('test_xiaobaiban_mycollect', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_39xiaobaiban_Dashboard_Myjoin(self):
        u"""我参与的小白板数据"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_myjoin')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)
        log_case_info('test_xiaobaiban_myjoin', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_40xiaobaiban_Dashboard_at_my(self):
        u"""@我的小白板数据"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_at_my')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)
        log_case_info('test_xiaobaiban_at_my', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_41xiaobaiban_combline(self):
        u"""新建小白板标签选择页面"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_combline')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        log_case_info('test_xiaobaiban_combline', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_42xiaobaiban_Update(self):
        u"""小白板更新"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_update')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        log_case_info('test_xiaobaiban_update', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_43xiaobaiban_Caogao(self):
        u"""小白板草稿箱"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_caogao')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        log_case_info('test_xiaobaiban_caogao', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_44xiaobaiban_JielunCaogao(self):
        u"""结论草稿箱"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_jieluncaogao')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        log_case_info('test_xiaobaiban_jieluncaogao', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_45xiaobaiban_TagJiemian(self):
        u"""新标签选择界面接口"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_jieluncaogao')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        log_case_info('test_xiaobaiban_jieluncaogao', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_46xiaobaiban_TagJiemian(self):
        u"""新标签选择界面接口"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_BiaoqiannNew')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        log_case_info('test_xiaobaiban_BiaoqiannNew', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_47xiaobaiban_MemberNumber(self):
        u"""参与小白板成员人数"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_member_number')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        log_case_info('test_xiaobaiban_member_number', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_48xiaobaiban_WidgetTemplate(self):
        u"""插件模板接口"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_widget_template')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)
        log_case_info('test_xiaobaiban_widget_template', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_49xiaobaiban_Widgets(self):
        u"""获取插件状况接口"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_widgets')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)
        log_case_info('test_xiaobaiban_widgets', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_50xiaobaiban_Widgets(self):
        u"""插件列表接口"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_associte')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.get(url=url, data=data.encode(), headers=header8)
        log_case_info('test_xiaobaiban_associte', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_51xiaobaiban_filter(self):
        u"""小白板标签搜索接口"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_filter_search')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        log_case_info('test_xiaobaiban_filter_search', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_52xiaobaiban_cehua(self):
        u"""小白板侧滑筛选接口"""
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_cehua_search')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        header8 = self.header7
        res = requests.post(url=url, data=data.encode(), headers=header8)
        log_case_info('test_xiaobaiban_cehua_search', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言




if __name__ == '__main__':
    unittest.main(verbosity=2)
