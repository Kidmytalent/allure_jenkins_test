# -*- coding: utf-8 -*-
# @Author： Kid
# @FileName: test_allure1.py

# 执行命令： pytest test_allure1.py --alluredir=./result/1    当前页面生成1个目录文件夹
# 执行完生成4个 json文件，每个文件里面 描述了测试用例的详细信息-----通过的还是失败的，记录了 运行时间，开始时间，结束时间 等等详细内容
# 执行第二条命令： allure serve ./result/1    --- 生成了一个allure_report 并通过默认浏览器自动打开了
# Ctrl + C 终止展示， 刷新就看不到了该报告 --- 实时在线的report
# 执行第三条命令： allure_report>allure generate ./result/1 -o ./report/1 --clean
# 第四条命令： allure open -h 127.0.0.1 -p 8885 ./report/1    ----通过指定本地127.0.0.1启动一个服务，指定一个端口8885去打开它

import pytest


def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')