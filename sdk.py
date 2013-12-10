#-*- encoding: utf-8 -*-
import hashlib,json,httplib
import urlparse
import urllib
import sys
from config import *

class UCLOUDException(Exception):
    def __str__(self):
        return "Error"

def _verfy_ac(private_key, params):
    items=params.items()
    items.sort()

    params_data = "";
    for key, value in items:
        params_data = params_data + str(key) + str(value)

    params_data = params_data+private_key

    '''use sha1 to encode keys'''
    hash_new = hashlib.sha1() 
    hash_new.update(params_data)
    hash_value = hash_new.hexdigest()
    return hash_value

class UConnection(object):
    def __init__(self, base_url):
        o = urlparse.urlsplit(base_url)
        if o.scheme == 'https':
            self.conn = httplib.HTTPSConnection(o.netloc); 
        else:
            self.conn = httplib.HTTPConnection(o.netloc); 

    def __del__(self):
        self.conn.close(); 


    def post(self, resouse, params):
        params = urllib.urlencode(params);
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        self.conn.request("POST", resouse, params, headers);     
        response = json.loads(self.conn.getresponse().read());
        return response;

    def get(self, resouse, params):
        if params:
            resouse = resouse + "?" + urllib.urlencode(params)
        self.conn.request("GET", resouse);     
        response = json.loads(self.conn.getresponse().read());
        return response;

    def delete(self, resouse, params):
        params = urllib.urlencode(params);
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        self.conn.request("DELETE", resouse, params, headers);     
        response = json.loads(self.conn.getresponse().read());
        return response;

    def delete(self, resouse, params):
        params = urllib.urlencode(params);
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        self.conn.request("PUT", resouse, params, headers);     
        response = json.loads(self.conn.getresponse().read());
        return response;

class UcloudApiClient(object):
    # 添加 设置 数据中心和  zone 参数 
    def __init__(self, base_url, public_key, private_key, region_id = 1, zone_id = 1):
        self.g_params = {};
        self.g_params['public_key'] = public_key;
        self.g_params['private_key'] = private_key;
        self.g_params['region_id'] = region_id;
        self.g_params['zone_id'] = zone_id;
        self.conn = UConnection(base_url);
    
    def get(self, url, **params):
        _params =  dict(self.g_params, **params);
        _params["access_token"] = _verfy_ac(_params['private_key'], _params);
        return self.conn.get(url,_params);

    def post(self, url, **params):
        _params =  dict(self.g_params, **params);
        _params["access_token"] = _verfy_ac(_params['private_key'], _params);
        return self.conn.post(url,_params);

    def delete(self, url, **params):
        _params =  dict(self.g_params, **params);
        _params["access_token"] = _verfy_ac(_params['private_key'], _params);
        return self.conn.delete(url,_params);

    def put(self, url, **params):
        _params =  dict(self.g_params, **params);
        _params["access_token"] = _verfy_ac(_params['private_key'], _params);
        return self.conn.delete(url,_params);

if __name__=='__main__':
    arg_length = len(sys.argv)
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    #response = ApiClient.get("/instances", offset=0, max_count=10);

    phone = ['13764073208'];
    response = ApiClient.post("/monitor/sendsms", phone=json.dumps(phone), content="test");
    print response;
