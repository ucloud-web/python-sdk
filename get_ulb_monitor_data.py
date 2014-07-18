#-*- encoding: utf-8 -*-
from sdk import UcloudApiClient 
from config import *
import sys

#实例化 API 句柄 指定获取数据的数据中心 {北京BGP :1001, 华东双线: 1 

ApiClient = UcloudApiClient(base_url, public_key, private_key, 1001)

#获取ULB 列表
#
# offset : 起始条数
# max_count : 最大获取条数

def get_ulb_list(offset, max_count):
    #调用短信API 
    response = ApiClient.get('/ulb/vserver', offset=offset, max_count=max_count);
    if response['ret_code'] == 0:
        return response['data'];
    return False 


#根据 uuid 和 监控指标 获取监控数据 
#uuid: ulb vserver_id 
#item_id: 指标ID , 
#start_time: 开始时间
#end_time: 结束时间

def get_monitor_data(uuid, item_id, start_time, end_time):
    response = ApiClient.get('/monitor/data', uuid=uuid, item_id=item_id, start_time=start_time, end_time=end_time);
    if response['ret_code'] == 0:
        return response['data'];
    return False 

if __name__=='__main__':
    arg_length = len(sys.argv)


    #获取 ulb 列表 起始条数, 最大条数 
    vserver_list = get_ulb_list(0, 100);

    print vserver_list
    #监控指标   104000 新建连接数/s 104001 入带宽(kbps) 104002 出带宽(kbps)  
    item_ids = [7003]

    for vserver in vserver_list:
        for public_ip in vserver['public_ips']:
            for item_id in item_ids:
                print get_monitor_data(public_ip["ip"], item_id, 1386604800, 1405668555);


    # if arg_length < 5 :
    #     print "./get_monitor_data.py ULB实例ID                            监控指标ID     开始时间   结束时间"
    #     print "./get_monitor_data.py 79003710-a719-47e7-ab30-b7524c5c2ffe 104000         1377187200 1377225583"
    #     sys.exit()

    # print get_monitor_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]);

