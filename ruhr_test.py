#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:ruhr_test
@time: 2021/02/08
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛ 
"""
import pytest
import requests
import yaml


class TestHttp():
    @pytest.mark.parametrize("data", yaml.safe_load(open("D:\WorkSpaces\PycharmProjects\Http1208/1.yaml")))
    def test_http(self, data):
        print(data)
        r = requests.post(f"http://47.100.179.197/ice-mars/temperature/list?imei={data}")
        assert r.json()["result"][0]["softVersion"] == 27
