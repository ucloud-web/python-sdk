#-*- encoding: utf-8 -*-
from sdk import UcloudApiClient 
from config import *
import sys
import json

#实例化 API 句柄
ApiClient = UcloudApiClient(base_url, public_key, private_key)

def sendsms(phone, message):
    #调用短信API 
    phone = phone.split("|")
    response = ApiClient.post('/monitor/sendsms', json.dumps(phone), message)
    if response['ret_code'] == 0:
        return True
    return False 

if __name__=='__main__':
    arg_length = len(sys.argv)
    if arg_length == 1 or arg_length == 2 :
        print "./sendsms.py 1377777777777|137888888888 测试短信"
        sys.exit()

    sendsms(sys.argv[1], sys.argv[2]);

