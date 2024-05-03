from Crypto.Cipher import AES
import os
import hashlib

script_path = os.path.dirname(os.path.realpath(__file__))
sha1 = hashlib.sha1()
key = bytes('WhySoSerious^@@^','utf-8')

fid = open(script_path + '/firmware.bin', 'rb')
original_data = fid.read()
fid.close()

IV = bytes(os.urandom(16))
cipher = AES.new(key, AES.MODE_CBC, IV=IV)
if len(original_data) % len(IV) != 0:
    original_data = original_data + bytes([0xFF]*(16 - len(original_data)%16))
encrypted_text = cipher.encrypt(original_data)
encrypted_text = IV + encrypted_text
sha1.update(encrypted_text)
HASH = format(sha1.hexdigest())
encrypted_text = HASH.encode() + encrypted_text

fid = open(script_path + '/efirmware', 'wb')
fid.write(encrypted_text)
fid.close()
