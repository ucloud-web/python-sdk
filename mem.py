#!/usr/bin/python
#-*- encoding: utf-8 -*-
import json
import string

from monitor_lib import f_meminfo, get_ip_address
from sendsms import sendsms

#调用短信API，可以是多个手机号码['13888888888', '13999999999']
phone = ['13888888888']
#告警得限额，0.1指的是内存使用率大于10%则会告警
watermark = 0.1


def main():
    ip = get_ip_address()
    meminfo = f_meminfo()
    
    # proc.meminfo.memfree 1373986088 4005464
    # proc.meminfo.buffers 1373986088 381416
    # proc.meminfo.cached 1373986088 9843132
    # proc.meminfo.memtotal 1373986088 16268732

    memtotal = float(meminfo.get("proc.meminfo.memtotal"));
    memused = memtotal - float(int(meminfo.get('proc.meminfo.memfree')) + int(meminfo.get('proc.meminfo.buffers')) + int(meminfo.get('proc.meminfo.cached')));

    utilization = (memused  / memtotal) 

    if(utilization > watermark ):
        message =  "%s 内存使用率超过 %.2f%%" % (ip, utilization * 100)
        sendsms(string.join(phone, "|") , message)

if __name__ == "__main__":
    main()
