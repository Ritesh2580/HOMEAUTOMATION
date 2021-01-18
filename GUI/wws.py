from websocket import *
from ast import literal_eval
import json
def on_open(t):
 print("connection open")
 print(t)
def on_message(t,message):
 print(message)
 print(literal_eval(message))

def on_error(t):
 print("error",t)
def on_close():
 print("bye")

enableTrace(True)
ws=WebSocketApp("ws://localhost:3000?Ritesh",on_message = on_message,on_error = on_error,on_close = on_close)
ws.on_open = on_open
ws.run_forever()
