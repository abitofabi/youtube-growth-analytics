import json
import sqlite3
import matplotlib.pyplot as plt
from googleapiclient.discovery import build
from datetime import datetime

# Load API Key from config.json
with open('config.json') as f:
    config = json.load(f)
API_KEY = config["API_KEY"]

# YouTube API setup
YOUTUBE = build("youtube", "v3", developerKey=API_KEY)

# SQLite Database Setup
conn = sqlite3.connect("youtube_data.db")  # Connect to your database
cursor = conn.cursor()

# Fetch YouTube Channel Stats
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

# Example: Use the Channel ID of your YouTube Channel
channel_id = "UC5hj4TGquFGqqUpvpH06xrA"  # Replace with your actual Channel ID

# Fetch and store stats in the database
channel_stats = get_channel_stats(channel_id)
cursor.execute("""
    INSERT INTO youtube_stats (date, subscribers, views, videos)
    VALUES (?, ?, ?, ?)
""", (channel_stats["date"], channel_stats["subscribers"], channel_stats["views"], channel_stats["videos"]))

# Commit and close the database connection
conn.commit()

# Fetch all stats from database
def fetch_all_stats():
    cursor.execute("SELECT * FROM youtube_stats ORDER BY date ASC")
    return cursor.fetchall()

# Function to plot data
def plot_data(stats):
    dates = [row[0] for row in stats]
    subscribers = [row[1] for row in stats]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, subscribers, marker="o", color="b", label="Subscribers")
    plt.title("YouTube Channel Subscriber Growth Over Time")
    plt.xlabel("Date")
    plt.ylabel("Subscribers")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    #plt.show()
    plt.savefig("youtube_graph.png") #using to display in venv
    print("Plot saved as png")
    plt.close()

# Run the visualization if data exists
if __name__ == "__main__":
    stats = fetch_all_stats()
    if stats:
        plot_data(stats)
    else:
        print("No data available to plot.")
    
# Close the database connection
conn.close()
