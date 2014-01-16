#!/usr/bin/python
#-*- encoding: utf-8 -*-
from sdk import UcloudApiClient 
from config import *
import sys 
import json


ApiClient = UcloudApiClient(base_url, public_key, private_key, 1, 1)


#获取当前用户主机列表
response = ApiClient.get('/instances',
   offset = 0,
   max_count = 100
)

if response['ret_code'] == 0:
   print response


#获取EIP列表
response = ApiClient.get('/uip/list')
if response['ret_code'] == 0:
   print response


#绑定EIP到主机
response = ApiClient.post('/uip/associate',
   vm_id = "$VM_INSTANCE_UUID",
   eip_id = "$EIP_UUID"
)
if response['ret_code'] == 0:
   print response


#从主机解绑EIP
response = ApiClient.post('/uip/disassociate',
   vm_id = "$VM_INSTANCE_UUID",
   eip_id = "$EIP_UUID"
)
if response['ret_code'] == 0:
   print response
