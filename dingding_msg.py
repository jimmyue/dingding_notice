#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Created on 2022年6月16日
@author: yuejing
'''
import requests
import time
import hmac
import hashlib
import base64
import urllib.parse

#https://open.dingtalk.com/document/robots/custom-robot-access
def send_msg(secret,Webhook,data):
	#获取timestamp和sign
	timestamp = str(round(time.time() * 1000))
	secret_enc = secret.encode('utf-8')
	string_to_sign = '{}\n{}'.format(timestamp, secret)
	string_to_sign_enc = string_to_sign.encode('utf-8')
	hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
	sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
	#发送请求
	headers={"Content-Type":"application/json;charset=utf-8"}
	url=Webhook+'&timestamp='+timestamp+'&sign='+sign
	r=requests.post(url,json=data,headers=headers)
	print(r.text)

if __name__ == "__main__":
	#修改标签
	secret = 'SEC72a6aae6b199a6ee17912866bc347b5923aff5fab1364d7a05b60568f7465f6d'
	#修改Webhook地址
	Webhook='https://oapi.dingtalk.com/robot/send?access_token=5bbd6405593bdebe6413ea1feeea2bee74207765cd470af43f6d61b35adae76d'
	#修改消息数据
	data={"msgtype": "text",
		  "text": {"content":"静夜思-李白\n床前明月光，疑是地上霜。\n举头望明月，低头思故乡。"},
		  "at":{"atMobiles":["185XXXXXXXX"],"isAtAll"False}
		  }
	send_msg(secret,Webhook,data)



