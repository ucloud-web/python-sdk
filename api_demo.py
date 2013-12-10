#!/usr/bin/python
#-*- encoding: utf-8 -*-
import base64
import sys
import pprint
import json

from config import *
from sdk import UcloudApiClient 

pp = pprint.PrettyPrinter(indent=4)

#{1:华东双线, 1001:北京BGP, 2001: 华南双线, 3001:亚太}

region_id = 1;

ApiClient = UcloudApiClient(base_url, public_key, private_key, 1)

if __name__=='__main__':

    #主机密码需要BASE64编码后传递，避免特殊字符被HTTP转义

    # passwd = base64.b64encode("testapi");

    # print "创建主机 ============================================================================="
    # # 创建主机
    # response = ApiClient.post('/instance/run', 
    #         cpu=2, 
    #         memory=2048,
    #         disk=20,
    #         image_id="c53aef95-72e1-49c3-a36c-1ca45362fba4",
    #         isp_id=0,
    #         band_width=0,
    #         pay_mode=1,
    #         hostname="testapi",
    #         password=passwd,
    #         public_secgroup=0,
    #         count=1,
    #         use_high_performance_disk=1
    #         )
    # if response['ret_code'] != 0:
    #     sys.exit(); 
    # #vmid = response['data']['item_id'];
    # 
    # print response

    # print "获取主机列表 ============================================================================="
    # # 获取主机列表
    # response = ApiClient.get('/instances', offset=0, max_count=100)

    # print response

    # if response['ret_code'] != 0:
    #     sys.exit(); 

    # print "遍历主机操作 ============================================================================="
    # # 遍历主机列表
    # for instance in response['data']:

    #     # #只有关机状态才能开机
    #     # if instance['vm_state'] == 510:
    #     #     #关机
    #     #     print "关机";
    #     #     response = ApiClient.post("/instance/shutdown", instance_id=instance['vmid']);
    #     #     print response

    #     # #只有关机状态才能开机
    #     # if instance['vm_state'] == 610:
    #     #     print "开机";
    #     #     response = ApiClient.post("/instance/start", instance_id=instance['vmid']);
    #     #     print response


    #     # #只有关机状态才能开机
    #     # if instance['vm_state'] == 510:
    #     #     print "重启";
    #     #     response = ApiClient.post("/instance/reboot", instance_id=instance['vmid']);
    #     #     print response


    #     #只有关机状态才能删除主机
    #     if instance['vm_state'] == 610:
    #         #删除 主机

    #         print "删除";
    #         response = ApiClient.delete("/instance", instance_id=instance['vmid']);
    #         print response


    # print "获取所有的负载均衡信息 ============================================================================="
    # response = ApiClient.get('/ulb/vserver', offset=0, max_count=10);
    # pp.pprint(response)


    # # print "通过vip_id获取单个获取一个Vserver 信息返回多端口设置================================================"
    #获取  ulb server id 获取 ulb 详细信息
    # response = ApiClient.get('/ulb/server', vserver_id="e02a76b6-a67c-46f3-9a1c-afde80fd0b9f");

    # 判断如果获取ULB 不成功或者没有包含多端口实例信息不进行下异步操作
    # if response['ret_code'] !=0 or len(response['data']) <= 0:
    #     sys.exit();

    # for vserver in response['data']:

    #     #注意修改添加 主机或者删除主机都需要全量 传递所有 的instances 已更新时传入为准
    #     response = ApiClient.put('/ulb/vserver',
    #             vserver_name = vserver['vserver_name'],
    #             vserver_type = vserver['vserver_type'],
    #             protocol = vserver['protocol'],
    #             frontend_port = vserver['frontend_port'],
    #             lb_method = vserver['lb_method'],
    #             persistence_type = vserver['persistence_type'],
    #             vserver_id = vserver['vserver_id'],
    #             instances = json.dumps(vserver['server_infos'])
    #     )

    #     pp.pprint(response)
