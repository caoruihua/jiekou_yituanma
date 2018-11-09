import unittest
import requests
import json
import sys,time

sys.path.append("../..")  # 提升2级到项目根目录下
from config.config import *  # 从项目路径下导入
from lib.read_excel import *  # 从项目路径下导入
from lib.case_log import log_case_info  # 从项目路径下导入


class TestXiaobaiban(unittest.TestCase):
    u'''小白板'''
    @classmethod
    def setUpClass(cls):  # 整个测试类只执行一次
        cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"),
                                      "TestXiaobaiban")  # 读取TestUserReg工作簿的所有数据

    def test_01user_login_normal(self):
        u'''测试登录'''
        case_data = get_test_data(self.data_list, 'test_user_login_normal')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
        data1 = data.encode('UTF-8')
        expect_res = case_data.get('expect_res')  # 期望数据

        res = requests.post(url=url, data=json.loads(data1))  # 表单请求，数据转为字典格式
        log_case_info('test_user_login_normal', url, data, expect_res, res.text)
        self.assertEqual(res.text, expect_res)  # 断言

    def test_02xiaobaiban_coment(self):
        u'''小白板评论'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_coment')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据

        res = requests.post(url=url, data=data.encode(), headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言


    def test_03xiaobaiban_cainajianyi(self):
        u'''采纳建议'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_cainajianyi')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.get(url=url, headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_04xiaobaiban_quxiaocaina(self):
        u'''取消采纳建议'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_quxiaocaina')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url') # excel中的标题也必须是小写url
        data=case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.get(url=url, headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_05xiaobaiban_yidu(self):
        u'''取消采纳建议'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_yidu')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url') # excel中的标题也必须是小写url
        data=case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.get(url=url, headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_06xiaobaiban_weidu(self):
        u'''取消采纳建议'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_weidu')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url') # excel中的标题也必须是小写url
        data=case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.get(url=url, headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_07xiaobaiban_remind(self):
        u'''提醒阅读'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_remind')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url') # excel中的标题也必须是小写url
        data=case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.post(url=url, data=data.encode(), headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_08xiaobaiban_kudos(self):
        u'''点赞'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_kudos')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.get(url=url, headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_09xiaobaiban_unkudos(self):
        u'''取掉点赞'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_unkudos')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.get(url=url, headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_10xiaobaiban_collect(self):
        u'''小白板收藏'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_collect')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url') # excel中的标题也必须是小写url
        data=case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.post(url=url, data=data.encode(), headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_11xiaobaiban_collect_cancel(self):
        u'''小白板取消收藏'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_collect_cancel')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url') # excel中的标题也必须是小写url
        data=case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.get(url=url, headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言


    def test_12xiaobaiban_search(self):
        u'''小白板搜索'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_search')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url') # excel中的标题也必须是小写url
        data=case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.post(url=url,data=data.encode(),headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_13xiaobaiban_looktaolun(self):
        u'''查看讨论人数'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_looktaolun')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.get(url=url, headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言


    def test_15xiaobaiban_groupmember(self):
        u'''查看团队成员'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_groupmember')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.get(url=url, headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_17xiaobaiban_jielun(self):
        u'''形成结论'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_jielun')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.post(url=url,data=data.encode(), headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言


    def test_18xiaobaiban_search(self):
        u'''小白板筛选'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_shaixuan')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url') # excel中的标题也必须是小写url
        data=case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.post(url=url,data=data.encode(),headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_19xiaobaiban_comenlaste(self):
        u'''查看团队成员'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_comenlaste')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.get(url=url, headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_20xiaobaiban_mremind(self):
        u'''小白板提醒'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_mremind')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.post(url=url, data=data.encode(),headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_21xiaobaiban_CRS(self):
        u'''查看CRS'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_CRS')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.post(url=url, data=data.encode(),headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言


    def test_23xiaobaiban_log(self):
        u'''查看小白板日志'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_log')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.get(url=url, headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言


    def test_24xiaobaiban_tag(self):
        u'''小白板标签'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_tag')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.post(url=url, data=data.encode(),headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_25xiaobaiban_show_new_v2(self):
        u'''未读角标接口'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_show-new-v2')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.get(url=url,headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_26xiaobaiban_wechat(self):
        u'''小白板转微信'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_wechat')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.get(url=url,headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_26xiaobaiban_remindself(self):
        u'''小白板提醒自己'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_remindself')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.post(url=url,data=data.encode(),headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_27xiaobaiban_simple(self):
        u'''小白板提醒自己'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_simple')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.get(url=url,headers=hearder2)
        log_case_info('test_user_login_password_wrong', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_28xiaobaiban_shenpichajian(self):
        u'''小白板审批插件'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_templates')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.get(url=url, headers=hearder2)
        log_case_info('test_xiaobaiban_templates', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_29xiaobaiban_tongzhi(self):
        u'''小白板通知开启'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_templates')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.get(url=url, headers=hearder2)
        log_case_info('test_xiaobaiban_tongzhi', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_30xiaobaiban_badge(self):
        u'''重置侧滑栏'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_badge')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.get(url=url, headers=hearder2)
        log_case_info('test_xiaobaiban_badge', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_31xiaobaiban_C_D(self):
        u'''创建删除小白板'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_create_delete')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.post(url=url,data=data.encode(), headers=hearder2)
        time.sleep(2)
        id=res.json()["id"] #动态获取id
        res2=requests.get(url="https://gateway.workdesk.esenyun.com:9091/words/openapi/words/destroy/"+id+"?groupId=",headers=hearder2)
        log_case_info('test_xiaobaiban_badge', url, data, expect_res, res2.text)
        print(id)
        self.assertEqual(res2.status_code, expect_res)  # 断言

    def test_31xiaobaiban_deletePinglun(self):
        u'''创建删除小白板'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_create_common')  # 从数据列表中查找到该用例数据
        case_data1 = get_test_data(self.data_list, 'test_xiaobaiban_delete_common')
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  #创建数据接口
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据

        url1 = case_data1.get('url')  # 删除数据接口
        data1 = case_data1.get('data')
        expect_res1 = case_data.get('expect_res')  # 期望数据

        res = requests.post(url=url,data=data.encode(), headers=hearder2)
        time.sleep(2)
        id=res.json()["id"] #动态获取id
        res2=requests.get(url=url1+id+"?groupId=",headers=hearder2)
        log_case_info('test_deleteconment', url1, data1, expect_res1, res2.text)
        print(id)
        self.assertEqual(res.status_code, expect_res)  # 断言


    def test_32xiaobaiban_coment(self):
        u'''小白板评论上传图片'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_coment_picture')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据

        res = requests.post(url=url, data=data.encode(), headers=hearder2)
        log_case_info('ttest_xiaobaiban_coment_picture', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言

    def test_33xiaobaiban_tongzhi(self):
        u'''小白板标签相关'''
        case_data = get_test_data(self.data_list, 'test_xiaobaiban_markers')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            logging.error("用例数据不存在")

        url = case_data.get('url')  # excel中的标题也必须是小写url
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.post(url=url,data=data.encode(), headers=hearder2)
        log_case_info('test_xiaobaiban_markers', url, data, expect_res, res.text)
        self.assertEqual(res.status_code, expect_res)  # 断言







if __name__ == '__main__':
    unittest.main(verbosity=2)
