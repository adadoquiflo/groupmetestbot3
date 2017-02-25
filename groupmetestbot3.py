import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler

def some_function():
    print "some_function got called"

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        some_function()

        self.send_response(200)

httpd = SocketServer.TCPServer(("", 8080), MyHandler)
httpd.serve_forever()
