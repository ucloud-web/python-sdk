#!/usr/bin/python
#-*- encoding: utf-8 -*-
import json
import string 

from monitor_lib import f_meminfo, get_ip_address, f_diskinfo
from sendsms import sendsms

#调用短信API，可以是多个手机号码['13888888888', '13999999999']
phone = ['13888888888']
#告警得限额，0.1指的是内存使用率大于10%则会告警
watermark = 0.1


def main():
    ip = get_ip_address()
    diskinfo = f_diskinfo()
    
    # df.1kblocks.total 1373990040 20641404 mount=/ fstype=ext4
    # df.1kblocks.used 1373990040 10632160 mount=/ fstype=ext4
    # df.1kblocks.free 1373990040 8960720 mount=/ fstype=ext4

    for key in diskinfo:

        diskused = float(diskinfo[key].get("df.1kblocks.used"))
        disktotal = float(diskinfo[key].get("df.1kblocks.total"))
        utilization = (diskused / disktotal) 
        if(utilization > watermark ):
            message =  "%s 文件系统 [%s] 磁盘使用率超过 %.2f%%" % (ip, key, utilization * 100)
            print sendsms(string.join(phone, "|"), message)

if __name__ == "__main__":
    main()
