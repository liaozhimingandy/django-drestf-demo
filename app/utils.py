# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================
#   Copyright (C) 2022 liaozhimingandy@qq.com Ltd. All Rights Reserved.
#
#   @Author      : zhiming
#   @Project     : drestf_demo
#   @File Name   : utils.py
#   @Created Date: 2022-04-10 11:13
#      @Software : PyCharm
#         @e-Mail: liaozhimingandy@qq.com
#   @Description : utils工具
#
# ======================================================================


# start_drf.utils.py
def jwt_response_payload_handler(token, user=None, request=None):
    """
       自定义jwt认证成功返回数据
       """
    return {
        'token': token,
        'id': user.id,
        'username': user.username
    }