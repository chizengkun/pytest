import pyotp
import time
import base64

# "R3FOQP5MN5QQG4BY43HZNN7F4C7EBMRPFFJVJNQZGRWTZVLMMKCF4XN7GPYZH3O4"
# 'WJURNWAWWG2Y6RIT'
#key = base64.b32encode(b"this a test")
key = "WJURNWAWWG2Y6RIT"
#key = "R3FOQP5MN5QQG4BY43HZNN7F4C7EBMRPFFJVJNQZGRWTZVLMMKCF4XN7GPYZH3O4"
totp = pyotp.TOTP(key)
k = totp.now()
print("Current OTP:", k)


#print(base64.b32encode(b"chizengkun"))
#hotp = pyotp.HOTP(key)
# sec =  hotp.at(60)
#print(sec)
#time.sleep(2000)
#print(hotp.verify(sec, 60))
#hotp.at(1)
#print(hotp.at(30))
#print(hotp.at(60))
#print( pyotp.random_base32())

#print(totp.verify(k))

#time.sleep(30)
#print(totp.verify(k))



