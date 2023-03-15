import requests
import json
from requests.auth import HTTPDigestAuth 
print('Enter your IP address, example 192.168.0.90')
ip = input()
ip_address = ip
print ("Username for Axis product ")
axis_user = input()
axis_username = axis_user
print("Enter password of Axis product ")
axis_pass = input()
axis_pw = axis_pass

cam_user = axis_username
cam_pass = axis_pw
auth=HTTPDigestAuth(cam_user, cam_pass)

# before you can create a websocket connection we must request a token.  
urlsessionid= 'http://'+ip_address+'/axis-cgi/wssession.cgi'

response = requests.request("POST", urlsessionid, auth=auth)
sessionID_responseJsonDict = (response.text)
token = sessionID_responseJsonDict

