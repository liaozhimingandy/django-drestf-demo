# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================
#   Copyright (C) 2022 liaozhimingandy@qq.com Ltd. All Rights Reserved.
#
#   @Author      : zhiming
#   @Project     : drestf_demo
#   @File Name   : serializers.py
#   @Created Date: 2022-04-09 22:36
#      @Software : PyCharm
#         @e-Mail: liaozhimingandy@qq.com
#   @Description : 序列化器文件
#
# ======================================================================


from rest_framework import serializers
from .models import User


class UserModelSerializer(serializers.ModelSerializer):
    # 需要进行数据转换的字段

    # 当前转换的模型类相关声明
    class Meta:
        model = User
        fields = "__all__"   # 所有字段

    # 验证数据的方法[反序列化: 接受客户端的数据]

    # 操作数据库的代码[反序列化: 保存数据的代码(添加和更新)]