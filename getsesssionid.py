
import requests
import json
from requests.auth import HTTPDigestAuth 
cam_user = 'root'
cam_pass = 'adp2013'
auth=HTTPDigestAuth(cam_user, cam_pass)

urlsessionid= 'http://192.168.20.195/axis-cgi/wssession.cgi'

response = requests.request("POST", urlsessionid, auth=auth)
sessionID_responseJsonDict = (response.text)
token = sessionID_responseJsonDict

