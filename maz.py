import time
import requests
import random
import json

# --- Configuration ---
STREAMER_USERNAME = "maz87" # The streamer you want to check
COMMENT_URL = "https://kick.com/api/v2/messages/send/47452211" # This URL seems to be for a specific chatroom ID, ensure it's correct for your target

# Your Authorization header from the image
AUTHORIZATION_TOKEN = "Bearer 207575384|VM2TjP93pkyfOxxlZb9zeKt5eNRRHtj5qeooggnC"

# Headers for the live status check and commenting, including your provided Cookie
# Ensure this cookie is kept up-to-date for the script to function correctly
REQUEST_HEADERS = {
    "Host": "kick.com",
    "Cookie": "USER_LOCALE=en; _gcl_au=1.1.1081391823.1734369207; _ga_YS2DLSGQ53=GS1.1.1737296898.2.1.1737297421.55.0.1318495855; _ga=GA1.1.533835387.1734369208; __stripe_mid=d3954a6d-3017-41cf-b718-84bffc6b5ae63a58b0; _rdt_uuid=1734369398041.dc040a80-5acb-4272-9969-431cdfb8409a; __cf_bm=kb4cGCdT6sizLsPIfIU982hqfMaFFtf8OB0pEXil5UE-1737296896-1.0.1.1-_UQwapGUcUSARjmx69UelSNMgVFEJm75jlj5bV4D2UNZ90.zsJ3qyfv3a6jDHYkHk_1qimA_fg7wV7nmSu4JnQ; _cfuvid=MIwEopacUojfXRYTHuHm_78EJNshaF3ZT1_GiUMP1_w-1737296896151-0.0.1.1-604800000; _dd_s=logs=1&id=7fecd723-1d59-436d-9470-912f60486da1&created=1737296897634&expire=1737298376300&rum=0; KP_UIDz-ssn=02BVkHSp0k4DQK7hwBfBZpcDAzAgUiL68hyS6vuKg7XvJgpDfTxCSQ9dMZN8vEmwUgK60ULOr3DVtcExuLMuVTws1ncVoQCCbETUpTq9BDAz1YXiIcvPEVqIiBElwKc3Um9rg2eSEXufAcnsGqLng64I47scwIqBpWjtFkNOGz; KP_UIDz=02BVkHSp0k4DQK7hwBfBZpcDAzAgUiL68hyS6vuKg7XvJgpDfTxCSQ9dMZN8vEmwUgK60ULOr3DVtcExuLMuVTws1ncVoQCCbETUpTq9BDAz1YXiIcvPEVqIiBElwKc3Um9rg2eSEXufAcnsGqLng64I47scwIqBpWjtFkNOGz; cf_clearance=GOKznPZofq12TKmrcVTEmuGu_zswGjSdJnWIASCnYBM-1737296907-1.2.1.1-TE6lV5p2loLWUDPsNTiB0uhrcAAGfGI8xV4yaVmbZSf1DLdKeTIUi5LAhkn6mSnos5WnlOfwM7X4Lvar2orAar.Z69bMdvAuTsMEFH.3unTB0srp6bjiOS0RZNAKFlJefN_kpc6.3P2yDRd160oFhl96OxMB9IcDD_r4djrTjMs42dYKUuRmHfLtODRculfWQqoXvEBn0aPANV3t.PyUKoBsjaI9AQvhJV10dCZSbNIHYG2gOs3C8._6oiSpTNngj8SITYsj7jyHbKGTez2unPUCfBh_Xhajj96KguYz1Pc; __stripe_sid=05da7adb-2b06-4b72-b5af-f88dd4af5e2aa89da4; XSRF-TOKEN=eyJpdiI6IlkxbTZVUzBxMVNCeVEwVk83RmtMK2c9PSIsInZhbHVlIjoiWnA0R0MvaWhjcEczbGZERDJITG9HcUFZTkxsSzBqZCtPNm1XS2NFY0g1bDZHVHhma1gxMFhYS2hSZUMvUVdEQW9jd3VXNHJkZHo0bFhsNHpMaElialJXb2VWMWF1UWs2MzhmcmlhbUtYYmc1Vm5vR3pLdVFHcFg5NVBZUk5UR0EiLCJtYWMiOiIyY2E1ODlmNWI5MWJhYjEwOGExMTNlNzk0NDY1YjhiZjgyMjM1NDA3N2M4NWVmYjg1ZDA5NDZlMjY4NTIyZjFhIiwidGFnIjoiIn0%3D; kick_session=eyJpdiI6IjVlWEQvRkNrL0p1djIyZlgwa2NXRWc9PSIsInZhbHVlIjoiZ2ppRTFPdXh0WVR0R2FPbGxqZituVWZMSWFIbkV5bzBma2pKK2ZHcUw5Uk0zd3pSakU1L1AzR0dNcjlzUURoSFVsbTM0c0xLREpxQ0ladWwyZjJBaDUwQktjNFBZS1JhaTRZTjA3ZlMvZTFMdVhwUEdvNXJ5NzhuTWZ5NHFQRzIiLCJtYWMiOiIwODFkZjAzOWI1MzgwMjFkNDlkOGUwNDI2ZDU5ZjlhODdkZDg0N2VjMjQ2YWZjYmMyYzEwNjA4NWY4YjZkZTc2IiwidGFnIjoiIn0%3D; session_token=159067268%7CfmuV1h7P6VBLIw5W6WI4TthgcvXMso0R0ClHiaBY; qHEI8MSShAjh61xnQqKEmWnmfnSc3C6v0JMaTx2T=eyJpdiI6Iit5enI4TzF0UndqOGNkVzdvQTZlb3c9PSIsInZhbHVlIjoiTXhQREVaSnpUMjRQWjViRldkcVg0NWFtQm1RMGFoU3QxWWhzYjFZRDYrUnZaeExIVWxvK0dlOHlJQWJNR2hiRHpUUXhQaFJZamo5NGREWUlJamx5L0hKOFd5TmR5ZW1QandrN05oVHFLRWdnTUVNdkI5R29jVXFJZmZ2UEFadnRvM0xhU3p3czVIUG43aEpwaXRyTk9xaHIxc0NGN3NmWGYzNmdQd1BEeGRSRkF3bnA0dU9LQmtPSGIxNitHQUIyaGpBWGswampNN2sySVhwZTBZN0RndXhzQUdpVmk2MHp5ZjRHN0lYNUVvRE1Mc1YzMjR5enZ5WndGdTA3Qm83RU5nZG4zVW00aUVVcWRETHpQOVZEd2JVYjk4K0llNW1NVnp2ckZhVlVSUGU1aHZXeTdDV3pWcGlWb1BwL3BwZysrQkxFSHEwVFR1STBjaWhzdXBCMzJBeDZmbFRVVUo5cXE0N3doM0FFcTJUNWpUY1FwQzlXV3VjdmIyTVFBQ3d4S21wcmJMdFNzV1RhNTY4cW8yWVpUUGIvMDVXVVA3SXRqR3FzWXBKam84dERCYzZRMXRjVy90SW91S0hxdW1TQmNiZGFvZUFIRVNRWFplUVJpRk81amtMK2xkbjhIcWdMMUJFYk8ycEJKTS9aRTdVQ3Y3SCs3TUpoQmRQTVBWa0tEQ1hRK0tCbC85dDg4TXRhNVhSUHBESDFNLys0bFM3N1BnaFlmRnVOV3AyNDdqdUZqS3BDRitONmkvZWo0bVpiemdOd3pVd3BZNXZPb3djbjBpSThXTUZCVEFiTkxZd3dPS3R6WUlQN2V4Q3lONTJPWUpGKzdSYUlSNWJqWnN1TVhkSVlBSjR1RjRpbjNTLzlYZW16WkhoaVAxdGVTSHFvRGR3R0J5WXJxOWgxZ1F0T3FmV1BldUhkZEFNVXErd3oyeVY5ZjVBYjl4cmYwUWdwWHhSNGFKWXJkcXdwN1l0eUo2NW5Uc0ZacHZXQXpWVkJNaDl3Y1pMK0trOWxYMUIwN05lMFBrSUNoRmJyMklHSzZZaCtNckVSdnIzQXV3M0kzZnM2RDB3MUhQNG1lMVVWSFdFZjRsYW14aDVkMVRxcEFlRm5RcjVyQVNqZUR6QmhkcUZsM1N4dXp1VGQ5Ly90OU52UVlJTnZkZ3c9IiwibWFjIjoiMzE1ODdjYzIzMjkxODIyZWVmNGRhY2RhOGRmMjQ0NGMxYjAwMDQzNjFiOTEwZGZlMjE0ZTRlYjc2NmU0MTRlNSIsInRhZyI6IiJ9; volume=0; stream_quality_cookie=160",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": f"https://kick.com/{STREAMER_USERNAME}", # Dynamic referer
    "Authorization": AUTHORIZATION_TOKEN,
    "Cluster": "v2",
    "Origin": "https://kick.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=0",
    "Cache-Control": "max-age=0",
    "Te": "trailers"
}

LIVE_STATUS_URL = "https://kick.com/api/v1/user/livestreams"

# Emotes/comments to send
emotes = [
    "[emote:37244:modCheck]",
    "[emote:39402:FlowIdle]",
    "[emote:37242:catblob0an]",
    "[emote:39258:coffinpls]",
    "[emote:39268:HYPERCLAPh]",
    "!points",
    "!lxp",
    "!level"
]

def check_live_status(username):
    """
    Checks if a given Kick streamer is currently live.
    Returns True if live, False otherwise.
    """
    try:
        response = requests.get(LIVE_STATUS_URL, headers=REQUEST_HEADERS)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        livestreams_data = response.json()

        for stream in livestreams_data:
            if stream.get("channel", {}).get("slug") == username and stream.get("is_live") == True:
                return True
        return False
    except requests.exceptions.RequestException as e:
        print(f"Error checking live status: {e}")
        return False

def send_comment(comment, url, headers):
    """
    Sends a comment to the specified Kick chatroom.
    """
    data = {
        "content": comment,
        "type": "message"
    }
    try:
        res = requests.post(url, json=data, headers=headers)
        res.raise_for_status() # Raise an exception for bad status codes
        return res
    except requests.exceptions.RequestException as e:
        print(f"Error sending comment: {e}")
        return None

# --- Main script logic (continuous) ---
is_streamer_live = False # Flag to track live status
comment_counter = 0 # To keep track of comments sent in a session

while True:
    current_live_status = check_live_status(STREAMER_USERNAME)

    if current_live_status:
        if not is_streamer_live:
            print(f"\n{STREAMER_USERNAME} is now LIVE! Starting auto-commenter.")
            is_streamer_live = True
            comment_counter = 0 # Reset counter when streamer goes live

        # Streamer is live, send comments
        comment_counter += 1
        random_emote = random.choice(emotes)
        res = send_comment(random_emote, COMMENT_URL, REQUEST_HEADERS)

        if res:
            print(f"[{comment_counter}] Sent: {random_emote} | Status: {res.status_code}")
        else:
            print(f"[{comment_counter}] Failed to send: {random_emote}")

        time.sleep(150) # Comment every 2.5 minutes while live

    else:
        if is_streamer_live:
            print(f"\n{STREAMER_USERNAME} went OFFLINE. Stopping comments.")
            is_streamer_live = False
        else:
            print(f"{STREAMER_USERNAME} is currently OFFLINE. Checking again in 5 minutes...")

        time.sleep(300) # Check every 5 minutes if not live
