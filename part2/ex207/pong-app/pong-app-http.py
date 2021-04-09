from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import psycopg2

dbhost = os.getenv('dbhost')
dbname = os.getenv('dbname')
dbuser = os.getenv('dbuser')
password = os.getenv('POSTGRES_PASSWORD')

def get_conn():
    conn = psycopg2.connect(host=dbhost,dbname=dbname,user=dbuser,password=password)
    return conn

def read_pongcount():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM pongcount")
    return cur.fetchone()[1]

def update_pongcount(count):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE pongcount SET count = (%s) WHERE ID = (%s)", (count, '1'))
    return conn.commit()



class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = 'Pong %s' % counter
        self.wfile.write(bytes(message, "utf8"))


with HTTPServer(('', 8084), handler) as server:
    print("Listening 8084...")
    while True:
        counter = read_pongcount()
        server.handle_request()
        update_pongcount(counter + 1)