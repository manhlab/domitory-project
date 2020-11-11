import hashlib
import datetime
def time_format(time_str):
    y, m, d = str(time_str).split("-")
    return datetime.date(int(y), int(m), int(d))

def hash_format(pasw):
    return hashlib.sha224(pasw.encode("utf-8")).hexdigest()

# if int(hashchr, 16) & int(hashcode, 16):
# print("success access programe!!!\n")