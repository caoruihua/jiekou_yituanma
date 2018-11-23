import os, time, unittest
import HTMLTestRunner_cn
import pytest

report_path = os.path.dirname(os.path.abspath('.')) + '/jiekou2/report/'
now = time.strftime('%y-%m-%d_%H_%M', time.localtime(time.time()))  # 获取当前信息并且以前面的格式输出
title = u'NexT+接口测试报告'  # 标题
report_repash = report_path + now + 'NexT+回归测试报告.html'  # 这里只要是组成一个测试报告路径
print(report_repash)


# 导入用例
def case_all():
    case_pash = os.path.dirname(os.path.abspath('.')) + '/jiekou2/testcase'
    discover = unittest.defaultTestLoader.discover(case_pash,
                                                   pattern='test_*.py')  # 添加用例，在case_path的路径下，所有以ceshi开头的文件都当做用例文件执行
    return discover


if __name__ == '__main__':
    fp = open(report_repash, "wb")  # 保存报告文件
    print(fp)
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                              title=title + '：', verbosity=2, retry=3)
    runner.run(case_all())  # 执行用例
    fp.close()
