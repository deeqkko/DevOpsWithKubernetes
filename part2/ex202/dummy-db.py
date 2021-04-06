from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type','application/json')
        self.end_headers()

        message = '''{
            "task":[
                "Wipe your behind",
                "Flush the toilet"
            ]
        }'''
        self.wfile.write(bytes(message,"utf-8"))

with HTTPServer(('', 8085), handler) as server:
    print("Listening 8085...")
    server.serve_forever()