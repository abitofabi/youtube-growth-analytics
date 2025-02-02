import json
import sqlite3
from googleapiclient.discovery import build
from datetime import datetime

# Load API Key from config.json
with open('config.json') as f:
    config = json.load(f)
API_KEY = config["API_KEY"]

# YouTube API setup
YOUTUBE = build("youtube", "v3", developerKey=API_KEY)

# SQLite Database Setup
conn = sqlite3.connect("youtube_data.db")  # Creates database if not exists
cursor = conn.cursor()

# Create Table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS youtube_stats (
    date TEXT,
    subscribers INTEGER,
    views INTEGER,
    videos INTEGER
)
""")
conn.commit()

# Function to Fetch YouTube Channel Stats
def get_channel_stats(channel_id):
    request = YOUTUBE.channels().list(
        part="statistics",
        id=channel_id
    )
    response = request.execute()
    stats = response["items"][0]["statistics"]
    return {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "subscribers": int(stats["subscriberCount"]),
        "views": int(stats["viewCount"]),
        "videos": int(stats["videoCount"])
    }

# Function to Store Data in Database
def save_data(data):
    cursor.execute("INSERT INTO youtube_stats VALUES (?, ?, ?, ?)", 
                   (data["date"], data["subscribers"], data["views"], data["videos"]))
    conn.commit()

# Run
channel_id = "UC5hj4TGquFGqqUpvpH06xrA"  # Replace with your channel ID
stats = get_channel_stats(channel_id)
save_data(stats)
print(f"Data saved: {stats}")

# Close Database Connection
conn.close()
