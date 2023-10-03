import requests
from requests.auth import HTTPDigestAuth 
import websocket
import threading  # Using threading instead of _thread for better control
import json

# List of IP addresses adjust as needed
ip_addresses = [f"192.168.20.{i}" for i in range(35, 41)]

def get_token_for_ip(ip_address, username, password):
    auth = HTTPDigestAuth(username, password)
    urlsessionid = f'http://{ip_address}/axis-cgi/wssession.cgi'
    
    try:
        response = requests.post(urlsessionid, auth=auth)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Failed to get session ID for IP: {ip_address}. Error: {e}")
        return None

def get_all_tokens(username, password):
    ip_tokens = []

    for ip in ip_addresses:
        token = get_token_for_ip(ip, username, password)
        if token:
            ip_tokens.append((ip, token))

    return ip_tokens

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    def run():
        ws.send(json.dumps({
            "apiVersion": "1.0",
            "method": "events:configure",
            "params": {
                "eventFilterList": [
                    {
                        # Uncomment and adjust these if required
                        "topicFilter": "tnsaxis:CameraApplicationPlatform/ObjectAnalytics/Device1Scenario1"
                    },
                    {
                         "topicFilter": "tnsaxis:CameraApplicationPlatform/ObjectAnalytics/Device1ScenarioANY"
                    }
                ]
            }
        }))
    threading.Thread(target=run).start()

def create_ws(ip_address, token):
    url = f"ws://{ip_address}/vapix/ws-data-stream?wssession={token}&sources=events"
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url, 
                                on_open=on_open,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()

if __name__ == "__main__":
    # Provide your camera's username and password here:
    cam_user = "root"
    cam_pass = "pass"
    
    ip_addresses_tokens = get_all_tokens(cam_user, cam_pass)

    for ip, token in ip_addresses_tokens:
        threading.Thread(target=create_ws, args=(ip, token)).start()
