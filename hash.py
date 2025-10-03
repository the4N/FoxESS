import hashlib
import time
import requests

# Your API details
BASE_URL = "https://www.foxesscloud.com"  # official domain
PATH = "/op/v0/device/history/query"
# PATH = "/op/v0/device/list"
TOKEN = "3c7cdf6d-78c4-4ee9-9753-a56f5eadec6b"             # replace with your token
DEVICE_SN = "6077103056GT001"     # replace with your inverter SN

# 1. Current timestamp in milliseconds
timestamp = str(int(time.time() * 1000))

# 2. Compute signature (MD5)
signature_str = fr"{PATH}\r\n{TOKEN}\r\n{timestamp}"
signature = hashlib.md5(signature_str.encode("utf-8")).hexdigest()

print(signature)
print(timestamp)
