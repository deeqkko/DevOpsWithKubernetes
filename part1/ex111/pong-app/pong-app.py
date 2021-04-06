from http.server import BaseHTTPRequestHandler, HTTPServer


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = 'Pong %s' % counter
        self.wfile.write(bytes(message, "utf8"))


with HTTPServer(('', 8084), handler) as server:
    counter = 1
    print("Listening 8084...")
    while True:
        server.handle_request()
        pongfile = open("./files/pongfile.txt", "w+")
        pongfile.write("Pongs: %s <br>\n" % counter)
        pongfile.close()
        counter += 1