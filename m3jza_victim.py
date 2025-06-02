import time
import requests
import random

url = "https://kick.com/api/v2/messages/send/15720418"
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
    "!level",
    "اللهم صلى وسلم وبارك علي سيدنا محمد",
    "كفووووووووو",
    "اسطورة",
    "سبحان الله وبحمده سبحان الله العظيم",
    "اللهم صلى وسلم وبارك علي سيدنا محمد",
    "اللهم صلى وسلم وبارك علي سيدنا محمد",
    "سبحان الله وبحمده سبحان الله العظيم",
    "سبحان الله وبحمده سبحان الله العظيم",
]

# Calculate the number of iterations needed for 3 hours
# 3 hours = 180 minutes
# Each message is sent every 2 minutes (120 seconds)
# So, total iterations = 180 minutes / 2 minutes/iteration = 90 iterations
num_iterations = 90

# Loop to send messages
for i in range(num_iterations):
    # Randomly select an emote or command from the list
    random_emote = random.choice(emotes)

    # Prepare the data payload for the POST request
    data = {"content": random_emote, "type": "message"}

    # Send the POST request to the Kick.com API
    res = requests.post(url, json=data, headers=headers)

    # Print the status of the sent message
    print(f"[{i+1}/{num_iterations}] Sent: {random_emote} | Status: {res.status_code}")

    # Wait for 120 seconds (2 minutes) before the next iteration
    time.sleep(120)

print("Script finished after 3 hours.")
