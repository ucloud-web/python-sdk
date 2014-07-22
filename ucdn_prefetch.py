#-*- encoding: utf-8 -*-
from sdk import UcloudApiClient 
from config import *
import sys
import json

#实例化 API 句柄
ApiClient = UcloudApiClient(base_url, public_key, private_key)

def prefetch():
    #调用内容预取API 
    response = ApiClient.post('/ucdn/prefetch',
           url_list = 'http://ucloud.cn/images/test.jpg',
           cdn_domain='ucloud.cn'
    )
    print response

prefetch();

#API 说明:
#1) 文件预取：
#   1,填写要预取的域名和预取的文件的完整url，并且每个url要以http://开头，如 http://ucloud.cn/images/test.jpg。
#   2,各个URL之间以分号(";")隔开，一次最多10个文件。
#   3,请注意区分URL中的字母的大小写，错误的大小写会导致预取无效。
#
#POST字段说明：
#   cdn_domain //要预取的域名
#   url_list   //提交的预取文件url列表

#返回值字段说明：
#ret_code      //执行结果状态码 0：执行成功 
#data          //执行结果返回值 true ：成功   false：失败
#error_message //错误提示语

