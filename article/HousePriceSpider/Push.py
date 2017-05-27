import requests


def pushMessage(msg):

	url = 'https://api.jpush.cn/v3/push'
	headers = {'Authorization': 'Basic NDJkZjdiY2MzZmRiN2Q2NDczODdlZmRhOjEwMTA2MTBjNzM3NmIyYTdhM2Y3ZjRlMw==','Content-Type':'application/json'}
	str1 = '{"platform":"all","audience":"all","notification" : {"ios" : {"alert" : "%s", "sound" : "sound.caf", "badge" : 1}},"options": {"apns_production": false}}'
	str1 =str1 % (msg)

	print str1
	rsp = requests.post(url,headers=headers,data=str1)
	if rsp.status_code:
		print 'push success'
		pass
	else :
		print 'push error'
		pass
	pass
