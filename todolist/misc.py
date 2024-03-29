from .models import User
from hashlib import sha256

#Get user ip
def getIP(raw_http, raw_addr):
    if raw_http:
        ip = raw_http.split(',')[0]
    else:
        ip = raw_addr
    return sha256(ip.encode("utf-8")).hexdigest()
