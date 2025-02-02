# youtube-growth-analytics
# YouTube Growth Analytics

This project tracks the **growth of a YouTube channel** by fetching and visualizing channel statistics such as **subscribers**, **view count**, and **video count** over time.

The project uses the **YouTube Data API v3** to collect data and stores it in a local **SQLite database**. The data is visualized using **Matplotlib** as a line graph showing subscriber growth.

## Features

- Fetches **YouTube channel statistics** (subscriber count, views, and video count).
- Stores statistics in an **SQLite database** (`youtube_data.db`).
- **Visualizes growth** in a graph using **Matplotlib**.
- **Data collection** is done manually by running the script.

## Prerequisites

Make sure you have the following installed on your machine:
- **Python 3.x**: Install Python from [here](https://www.python.org/downloads/).
- **pip** (Python package manager): You can install it from [here](https://pip.pypa.io/en/stable/installation/).
- **SQLite3**: Usually comes pre-installed with Python, but can be installed separately if needed.

## Setup

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/youtube-growth-analytics.git
   cd youtube-growth-analytics

