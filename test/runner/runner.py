# coding=utf-8
import unittest
import os,time
from lib.utils import HTMLTestRunner
log_path = os.path.join(os.path.abspath(".."), "baogao")
print(log_path)
# 用例路径
case_path = os.path.join(os.path.abspath(".."), "case")
# 报告存放路径
report_path = os.path.join(os.getcwd(), log_path)
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test*.py",
                                                    top_level_dir=None)
    return discover

if __name__ == "__main__":
    #按照一定格式获取当前时间
    now = time.strftime("%Y%m%d_%H%M%S")
    #将当前时间加入到报告文件名称中
    # html报告文件路径
    report_abspath = os.path.join(log_path, now + u"测试报告" + "result.html")
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')
    # print(all_case())
    # # 调用add_case函数返回值
    runner.run(all_case())
    # fp.close()

