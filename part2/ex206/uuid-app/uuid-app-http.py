from http.server import BaseHTTPRequestHandler, HTTPServer
import uuid
import time
from datetime import datetime
import requests
import os

random_hash = str(uuid.uuid4())

def print_uuid():
    page = requests.get("http://pong-app-http-service:18084").content
    pongcount = str(page.decode("utf-8"))
    timestamp = datetime.now()
    timestamp = timestamp.strftime('%Y.%m.%d %H:%m:%S')
    msg = os.getenv('MESSAGE')    
    output_uuid = msg + '<br>\n' + timestamp + ' ' + random_hash + '<br>\n' + pongcount
    return output_uuid    
        

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = print_uuid()
        self.wfile.write(bytes(message, "utf8"))

with HTTPServer(('', 8083), handler) as server:
    print("Listening 8083...")
    server.serve_forever()