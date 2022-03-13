
from http.server import HTTPServer, BaseHTTPRequestHandler


hostname = 'localhost'
port = 2030

class myserver(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/':
            self.path = '/service.html'
        try:
            open_file = open(self.path[1:]).read()
            self.send_response(200)
        except:
            open_file = "File can not be located"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(open_file, 'utf-8'))


pserver = HTTPServer((hostname, port), myserver)
pserver.serve_forever()

