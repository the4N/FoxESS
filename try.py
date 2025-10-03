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

# 3. Build headers
headers = {
    "Content-Type": "application/json",
    "token": TOKEN,
    "timestamp": timestamp,
    "signature": signature,
    "lang": "en"
}

# 4. Request body (example: query pvPower and gridConsumption today)
# time range: last 6 hours (timestamps in ms)
end = int(time.time() * 1000)
begin = end - (6 * 60 * 60 * 1000)

payload = {
    "sn": DEVICE_SN,
    # "variables": ["pvPower", "gridConsumption"],
    # "begin": begin,
    # "end": end
}

# payload = {
#     "currentPage": 1,
#     "pageSize": 10
# }

# 5. Send POST request
url = BASE_URL + PATH
response = requests.post(url, headers=headers, json=payload)

print("Request URL:", url)
print("Timestamp:", timestamp)
print("Signature:", signature)
print("Status:", response.status_code)
print("Response:", response.json())
