#-*- encoding: utf-8 -*-
from sdk import UcloudApiClient 
from config import *
import sys
import json

#实例化 API 句柄
ApiClient = UcloudApiClient(base_url, public_key, private_key)
ApiClient = UcloudApiClient(base_url, public_key, private_key, 1)

def refresh_cdn():
    #调用cdn内容刷新API 
    response = ApiClient.post('/ucdn/refresh',
           url_list = 'http://ucloud.cn/images/test.jpg;http://ucloud.cn/images/test.jpg',
           cdn_domain='ucloud.cn',
           type = 1
    )
    print response

refresh_cdn();

#API 说明:
#1) 目录刷新：
#   1,请输入您要推送的完整目录URL，如 http://static.ucloud.cn/images/,各个目录URL之间以分号(";")隔开。一次最多30行。
#   2,目录必须以http://开头，具体目录名必须以正斜杠("/")结尾。
#   3,请注意区分URL中的字母的大小写，错误的大小写会导致刷新无效。
#   4,如果目录有上下级层次关于,本功能会自动同时推送下级子目录,不需要填写下级子目录。
#2) 文件刷新：
#   1,请输入您要刷新的完整URL，并且每个url要以http://开头。
#   2,如 http://static.ucloud.cn/images/test.jpg,各个URL之间以分号(";")隔开。
#   3,请注意区分URL中的字母的大小写，错误的大小写会导致刷新无效。
#
#POST字段说明：
#   cdn_domain //要刷新的域名
#   url_list   //该域名下的文件列表或目录列表
#   type       // url_list 的类型 1：目录列表，0：文件列表
#返回值字段说明：
#ret_code      //执行结果状态码 0：执行成功 
#data          //执行结果返回值 true ：成功   false：失败
#error_message //错误提示语
