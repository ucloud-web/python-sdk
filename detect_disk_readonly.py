#!/usr/bin/python
#-*- encoding: utf-8 -*-
import json
import string 

from monitor_lib import get_ip_address, f_detect_disk_readonly
from sendsms import sendsms

#调用短信API，可以是多个手机号码['13888888888', '13999999999']
phone = ['13888888888', '13999999999']

def main():
    ip = get_ip_address()
    disklist = f_detect_disk_readonly()

    for disk in disklist:
        # 如果某块磁盘频繁发生只读请联系技术支持!
        message =  "%s %s文件系统只读" % (ip, disk)
        print sendsms(string.join(phone, "|"), message)


if __name__ == "__main__":
    main()
