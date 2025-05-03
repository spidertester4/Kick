import time
import requests

url = "https://kick.com/api/v2/messages/send/15720418"
headers = {
    "Authorization": "Bearer 207575384|VM2TjP93pkyfOxxlZb9zeKt5eNRRHtj5qeooggnC",
    "Content-Type": "application/json"
}
data = {"content":"[emote:39268:HYPERCLAPH]", "type":"message"}

for i in range(60):  # 3 hours = 180 minutes
    res = requests.post(url, json=data, headers=headers)
    print(f"[{i+1}/180] Status: {res.status_code}")
    time.sleep(60)
