import time
import requests
import random

url = "https://kick.com/api/v2/messages/send/16409618"
headers = {
    "Authorization": "Bearer 207575384|VM2TjP93pkyfOxxlZb9zeKt5eNRRHtj5qeooggnC",
    "Content-Type": "application/json"
}

emotes = [
    "[emote:37244:modCheck]",
    "[emote:39402:Flowie]",
    "[emote:37242:catblobDan]",
    "[emote:39258:coffinPls]",
    "[emote:39268:HYPERCLAPH]",
    "!points",
    "!xp"
]

for i in range(180):  # 3 hours = 180 minutes
    random_emote = random.choice(emotes)
    data = {"content": random_emote, "type": "message"}
    res = requests.post(url, json=data, headers=headers)
    print(f"[{i+1}/180] Sent: {random_emote} | Status: {res.status_code}")
    time.sleep(120)
