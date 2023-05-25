import http.server
import socketserver
from datetime import datetime

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", 1234), handler) as httpd:
   index = open('index.html', 'a')
   dt_obj = datetime.now()
   index.write(dt_obj.strftime("%A %d-%b-%Y %H:%M:%S"))
   index.close()
   httpd.serve_forever()