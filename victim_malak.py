import time
import requests
import random

url = "https://kick.com/api/v2/messages/send/16409618"
headers = {
    "Authorization": "Bearer 214176003|8e5NWfg8A3R4XCIdCASqd8Hc0HyTTGCxrNAerKSA",
    "Content-Type": "application/json"
}

emotes = [
    "[emote:37244:modCheck]",
    "[emote:39402:Flowie]",
    "[emote:37242:catblobDan]",
    "[emote:39258:coffinPls]",
    "[emote:39268:HYPERCLAPH]",
    "!points",
    "!xp",
    "!level",
    "سبحان الله وبحمده سبحان الله العظيم",
    "اللهم صلى وسلم وبارك علي سيدنا محمد",
    "اللهم صلى وسلم وبارك علي سيدنا محمد",
    "سبحان الله وبحمده سبحان الله العظيم",
    "سبحان الله وبحمده سبحان الله العظيم",
    "لا اله الا الله وحده لا شريك له له الملك وله الحمد وهو علي كل شئ قدير"
]

for i in range(180):  
    random_emote = random.choice(emotes)
    data = {"content": random_emote, "type": "message"}
    res = requests.post(url, json=data, headers=headers)
    print(f"[{i+1}/180] Sent: {random_emote} | Status: {res.status_code}")
    time.sleep(60)
