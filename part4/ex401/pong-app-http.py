from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import psycopg2
import socket

class handler(BaseHTTPRequestHandler):
    dbhost = os.getenv('dbhost')
    dbname = os.getenv('dbname')
    dbuser = os.getenv('dbuser')
    password = os.getenv('POSTGRES_PASSWORD')

    def get_conn(self):
        conn = psycopg2.connect(host=self.dbhost,dbname=self.dbname,user=self.dbuser,password=self.password)
        return conn

    def read_pongcount(self):
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM pongcount")
        res = cur.fetchone()[1]
        conn.close()
        return res

    def update_pongcount(self, count):
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("UPDATE pongcount SET count = (%s) WHERE ID = (%s)", (count, '1'))
        conn.commit()
        conn.close()

    def test_conn(self):
        try:
            conn = self.get_conn()
            result_of_check = conn.closed
            conn.close()
        except:
            result_of_check = 1
        return result_of_check

    def get_main(self):
        if self.path.endswith('favicon.ico'):
            return
        counter = self.read_pongcount()
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = 'Pong %s' % counter
        self.update_pongcount(counter + 1)
        return message

    def get_health(self):
        conn = self.test_conn()
        if conn == 0:
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
        else:
            self.send_response(500)
            self.send_header('Content-type','text/html')
            self.end_headers()

    def do_GET(self):
        print(self.path)
        url_to_handler = {
            "/":self.get_main,
            "/healthz":self.get_health
        }
        if self.path.endswith('favicon.ico'):
            return
        if self.path.endswith("/"):
            response = url_to_handler["/"]()
            self.wfile.write(bytes(response, "utf8"))
        if self.path.endswith("/healthz"):
            response = url_to_handler["/healthz"]()


with HTTPServer(('', 8084), handler) as server:
    print("Listening 8084...")
    server.serve_forever()
        