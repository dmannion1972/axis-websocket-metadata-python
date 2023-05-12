import requests
from requests.auth import HTTPDigestAuth 
from getpass import getpass

ip_address = input("Enter your IP address: ")
cam_user = input("Enter username: ")
cam_pass = getpass("Enter password: ")
auth = HTTPDigestAuth(cam_user, cam_pass)

urlsessionid= f'http://{ip_address}/axis-cgi/wssession.cgi'

response = requests.request("POST", urlsessionid, auth=auth)
sessionID_responseJsonDict = (response.text)
print(sessionID_responseJsonDict)
token = sessionID_responseJsonDict

