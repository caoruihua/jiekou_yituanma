import logging
import os
import time

# 项目路径
header={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/70.0.3538.77 Safari/537.36",
            "Authorization": "Bearer b649f862-d5f5-4cde-93a4-876c61af12c5",
            "accept": "application/json,text/plain,*/*",
            "accept-encoding": "gzip,deflate,br",
            "content-type": 'application/json',
            'accept - language': 'zh - CN, zh;q = 0.9'

            }
hearder2={  "User-Agent": "ESEN/1.3.11 (iPhone; iOS 12.1; Scale/2.00)",
            "Authorization": "Bearer 78e4c50f-3d41-4f4c-b105-95a754af0e65",
            "accept": "*/*",
            "accept-encoding": "gzip,deflate,br",
            "content-type": 'application/json',
            'accept-language': 'zh-Hans-CN;q=1',
            'channel':'IOS',
            'app-sys-info':'IOS;12.1',
            'version':'1.3.11',



}
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级的上一级目录（增加一级）

data_path = os.path.join(prj_path, 'data')  # 数据目录
test_path = os.path.join(prj_path, 'testcase')   # 用例目录
now = time.strftime('%y-%m-%d_%H_%M', time.localtime(time.time()))

log_file = os.path.join(prj_path, "log", now+'log.log')  # 更改路径到log目录下
report_file = os.path.join(prj_path, 'report', 'report.html')  # 更改路径到report目录下

# log配置
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')  # 追加模式


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
