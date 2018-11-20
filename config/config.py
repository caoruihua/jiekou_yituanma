# -*- coding: utf-8 -*-
import logging
import os
import time

# header配置
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/70.0.3538.77 Safari/537.36",
    "Authorization": "Bearer 72f60ef2-277f-48bf-9404-cbdd5e6a7fea",
    "accept": "application/json,text/plain,*/*",
    "accept-encoding": "gzip,deflate,br",
    "content-type": 'application/json',
    'accept - language': 'zh - CN, zh;q = 0.9'

}

hearder2 = {"User-Agent": "ESEN/1.3.11 (iPhone; iOS 12.1; Scale/2.00)",
            "Authorization": "Bearer 72f60ef2-277f-48bf-9404-cbdd5e6a7fea",
            "accept": "*/*",
            "accept-encoding": "gzip,deflate,br",
            "content-type": 'application/json',
            'accept-language': 'zh-Hans-CN;q=1',
            'channel': 'IOS',
            'app-sys-info': 'IOS;12.1',
            'version': '1.3.11',
            }

hearder3 = {"User-Agent": "ESEN/1.3.11 (iPhone; iOS 12.1; Scale/2.00)",
            "Authorization": "Bearer 72f60ef2-277f-48bf-9404-cbdd5e6a7fea",
            "accept": "*/*",
            "accept-encoding": "gzip,deflate,br",
            "content-type": 'application/x-www-form-urlencoded',
            'accept-language': 'zh-Hans-CN;q=1',
            'channel': 'IOS',
            'app-sys-info': 'IOS;12.1',
            'version': '1.3.11',

            }

# 小程序买专用header
hearder4 = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                  "Mobile/16C5043b MicroMessenger/6.7.3(0x16070321) NetType/4G Language/zh_CN",
    "Authorization": "Bearer 72f60ef2-277f-48bf-9404-cbdd5e6a7fea",
    "accept": "*/*",
    "accept-encoding": "gzip,deflate,br",
    "content-type": 'application/json',
    'accept-language': 'zh-cn',
    'x-wxa-appid': 'wx3bc009c34c8a1040',
    'referer': 'https://servicewechat.com/wx3bc009c34c8a1040/19/page-frame.html',

}

#登录专用
hearder5 = {"User-Agent": "ESEN/1.3.11 (iPhone; iOS 12.1; Scale/2.00)",
            "Authorization": "Basic bW9iaWxlX25hdGl2ZV9hcHA6NjF3NFUyenJjQjg4",
            "accept": "*/*",
            "accept-encoding": "gzip,deflate,br",
            "content-type": "application/x-www-form-urlencoded",
            'accept-language': 'zh-Hans-CN;q=1',
            'channel': 'IOS',
            'app-sys-info': 'IOS;12.1',
            'version': '1.3.11',

            }


# 日志路径配置
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级的上一级目录（增加一级）

data_path = os.path.join(prj_path, 'data')  # 数据目录
test_path = os.path.join(prj_path, 'testcase')  # 用例目录
now = time.strftime('%y-%m-%d_%H_%M', time.localtime(time.time()))

log_file = os.path.join(prj_path, "log", now + 'log.log')  # 更改路径到log目录下
report_file = os.path.join(prj_path, 'report', 'report.html')  # 更改路径到report目录

# log配置
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a',
                    )  # 追加模式

# 数据库配置
db_host = '115.28.108.130'
db_port = 3306
db_user = 'testcase'
db_passwd = '123456'
db = 'api_test'

# 邮件配置
smtp_server = 'smtp.sina.com'
smtp_user = 'test_results@sina.com'
smtp_password = 'hanzhichao123'

sender = smtp_user  # 发件人
receiver = '2375247815@qq.com'  # 收件人
subject = '接口测试报告'  # 邮件主题
