
import qrcode

img = qrcode.make("http://localhost:8080/service.html")

img.save("pserverQR.jpg")
