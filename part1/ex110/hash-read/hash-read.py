from http.server import BaseHTTPRequestHandler, HTTPServer

def read_hashfile():
    hashfile = open("./files/hashfile.txt", "r")
    contents = hashfile.read()
    return contents

        

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        #message = "Hello, World!"
        message = read_hashfile()
        self.wfile.write(bytes(message, "utf8"))

with HTTPServer(('', 8083), handler) as server:
    print("Listening 8083...")
    server.serve_forever()