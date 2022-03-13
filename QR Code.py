
from python_server import pserver

import qrcode
img = qrcode.make(pserver)
type(img)
img.save()
