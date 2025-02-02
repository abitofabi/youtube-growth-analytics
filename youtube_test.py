import json
from googleapiclient.discovery import build

# Load API Key from config.json
with open('config.json') as f:
    config = json.load(f)
API_KEY = config["API_KEY"]

# YouTube API setup
YOUTUBE = build("youtube", "v3", developerKey=API_KEY)

# Fetch channel statistics (e.g., subscriber count)
def get_channel_stats(channel_id):
    request = YOUTUBE.channels().list(
        part="snippet,statistics",
        id=channel_id
    )
    response = request.execute()
    return response["items"][0]["statistics"]

# Test with a sample channel ID (replace with your own)
channel_id = "UC5hj4TGquFGqqUpvpH06xrA" #UC_x5XG1OV2P6uZZ5b6rT2KQ"  # Replace with your YouTube channel ID
stats = get_channel_stats(channel_id)
print(f"Subscribers: {stats['subscriberCount']}")
print(f"Views: {stats['viewCount']}")
print(f"Videos: {stats['videoCount']}")
