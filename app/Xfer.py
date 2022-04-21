# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================
#   Copyright (C) 2022 liaozhimingandy@qq.com Ltd. All Rights Reserved.
#
#   @Author      : zhiming
#   @Project     : django-drestf-demo
#   @File Name   : Xfer.py
#   @Created Date: 2022-04-14 22:52
#      @Software : PyCharm
#         @e-Mail: liaozhimingandy@qq.com
#   @Description :
#
# ======================================================================

import sys
import os
from ftplib import FTP

_XFER_FILE = 'FILE'
_XFER_DIR = 'DIR'


class Xfer(object):
    """
      @note: 上传本地文件或文件夹到ftp服务器
    """

    def __init__(self, ip, uname, pwd, port=21, timeout=60):
        self.timeout = timeout
        self.port = port
        self.pwd = pwd
        self.uname = uname
        self.ip = ip
        self.ftp = None

    def __del__(self):
        pass

    def initEnv(self):
        if self.ftp is None:
            self.ftp = FTP()
            print(f'### connect ftp server: {self.ip} ...')
            try:
                self.ftp.connect(self.ip, self.port, self.timeout)
            except (ConnectionRefusedError, ) as e:
                print(f"{self.ip} 积极拒绝连接...")
                exit(1)
            self.ftp.login(self.uname, self.pwd)
            self.ftp.encoding = 'utf8'
            self.ftp.getwelcome()


    def clearEnv(self):
        if self.ftp:
            self.ftp.close()
            print(f'### disconnect ftp server: {self.ip}!')
            self.ftp = None

    def uploadDir(self, localdir='./', remotedir='data'):
        if not os.path.isdir(localdir):
            return
        try:
            self.ftp.cwd(remotedir)
        except:
            self.ftp.mkd(remotedir)
            self.ftp.cwd(remotedir)
        for file in os.listdir(localdir):
            src = os.path.join(localdir, file)
            if os.path.isfile(src):
                self.uploadFile(src, file)
            elif os.path.isdir(src):
                try:
                    self.ftp.mkd(file)
                except:
                    sys.stderr.write('the dir is exists %s' % file)
                self.uploadDir(src, file)
        self.ftp.cwd('..')

    def uploadFile(self, localpath, remotepath='./'):
        if not os.path.isfile(localpath):
            return
        print(f'+++ upload: {localpath} to {self.ip}:{remotepath}')
        self.ftp.storbinary('STOR ' + remotepath, open(localpath, 'rb'))

    def __filetype(self, src):
        if os.path.isfile(src):
            index = src.rfind('\\')
            if index == -1:
                index = src.rfind('/')
            return _XFER_FILE, src[index + 1:]
        elif os.path.isdir(src):
            return _XFER_DIR, ''

    def upload(self, src, dest):
        filetype, filename = self.__filetype(src)

        self.initEnv()
        if filetype == _XFER_DIR:
            self.srcDir = src
            self.uploadDir(self.srcDir, remotedir=dest)
        elif filetype == _XFER_FILE:
            self.uploadFile(src, filename)
        self.clearEnv()


if __name__ == '__main__':
    # 使用方法 python D:\PyCharm\django-drestf-demo\drestf_proj\app\Xfer.py D:\dicom\KHdata\Image\蔡桂香_20211229008F 蔡桂香_20211229008F 127.0.0.1 ftpuser 123456
    # 判断参数的个数,至少5个
    if(len(sys.argv) < 6):
        print("参数个数不能少于5个!")
        exit(2)
    else:
        src_dir = sys.argv[1]
        dest_dir = sys.argv[2]

    # src_dir = r"D:\dicom\KHdata\Image\蔡桂香_20211229008F"
    # srcFile = r'D:\dicom\KHdata\Image\蔡桂香_20211229008F\sar.c'
    # xfer = Xfer('127.0.0.1', 'ftpuser', '123456')
    xfer = Xfer(sys.argv[3], sys.argv[4], sys.argv[5])
    xfer.upload(src_dir, dest_dir)
    # xfer.upload(srcFile)

