from http.server import BaseHTTPRequestHandler, HTTPServer
import uuid
import time
from datetime import datetime

random_hash = str(uuid.uuid4())

def print_uuid():
    pongfile = open("./files/pongfile.txt", "r")
    pongcount = pongfile.read()
    pongfile.close()
    timestamp = datetime.now()
    timestamp = timestamp.strftime('%Y.%m.%d %H:%m:%S')    
    output_uuid = timestamp + ' ' + random_hash + '<br>\n' + pongcount
    return output_uuid    
        

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        #message = "Hello, World!"
        message = print_uuid()
        self.wfile.write(bytes(message, "utf8"))

with HTTPServer(('', 8083), handler) as server:
    print("Listening 8083...")
    server.serve_forever()