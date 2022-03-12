import qrcode               #QR code library  
img = qrcode.make()
type(img)
img.save()


from http.server import HTTPServer, BaseHTTPRequestHandler


class myserver(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
