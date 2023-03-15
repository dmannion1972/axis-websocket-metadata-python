import websocket
import _thread
import json
# this file getsesssionid.py imports the token that is needed for authentication
from getsesssionid import *


url= "ws://192.168.20.195/vapix/ws-data-stream?wssession="+token+"&sources=events"

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    def run(*args):
      ws.send(json.dumps({
  "apiVersion": "1.0",
  "method": "events:configure",
  "params": {
    "eventFilterList":[
      {
        "topicFilter":""
      }
    ]
  }
}))
    _thread.start_new_thread(run, ())
if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url, 
                              on_open = on_open,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
