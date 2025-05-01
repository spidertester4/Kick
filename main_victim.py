import time
import requests

url = "https://kick.com/api/v2/messages/send/15720418"
headers = {
    "Authorization": "Bearer 214176003|8e5NWfg8A3R4XCIdCASqd8Hc0HyTTGCxrNAerKSA",
    "Content-Type": "application/json"
}
data = {"content":"[emote:39268:HYPERCLAPH]", "type":"message"}

for i in range(180):  # 3 hours = 180 minutes
    res = requests.post(url, json=data, headers=headers)
    print(f"[{i+1}/180] Status: {res.status_code}")
    time.sleep(60)
