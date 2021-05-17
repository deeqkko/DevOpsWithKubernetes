from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import uuid
import time
from datetime import datetime
import requests
import os

random_hash = str(uuid.uuid4())

def test_conn():
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    location = ("pong-app-http-service", 18084)
    result_of_check = a_socket.connect_ex(location)
    a_socket.close()
    return result_of_check

def print_uuid():
    page = requests.get("http://pong-app-http-service:18084").content
    pongcount = str(page.decode("utf-8"))
    timestamp = datetime.now()
    timestamp = timestamp.strftime('%Y.%m.%d %H:%m:%S')
    msg = os.getenv('MESSAGE')    
    output_uuid = msg + '<br>\n' + timestamp + ' ' + random_hash + '<br>\n' + pongcount
    return output_uuid    
        

class handler(BaseHTTPRequestHandler):
    def get_main(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = print_uuid()
        return message

    def get_health(self):
        conn = test_conn()
        if conn == 0:
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
        else:
            self.send_response(500)
            self.send_header('Content-type','text/html')
            self.end_headers()


    def do_GET(self):
        url_to_handler = {
            "/":self.get_main,
            "/healthz":self.get_health
            }
        if self.path.endswith("app"):
            response = url_to_handler["/"]()
            self.wfile.write(bytes(response, "utf8"))
        if self.path.endswith("/healthz"):
            response = url_to_handler["/healthz"]()


with HTTPServer(('', 8083), handler) as server:
    print("Listening 8083...")
    server.serve_forever()