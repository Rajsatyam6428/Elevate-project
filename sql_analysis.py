import sqlite3
import pandas as pd

# Load cleaned data
df = pd.read_csv('dashboard/youtube_dashboard.csv')

# Create SQLite DB
conn = sqlite3.connect("youtube_trending.db")
df.to_sql("videos", conn, if_exists="replace", index=False)

# Run query
query = """
SELECT category_id, region, AVG(views) AS avg_views
FROM videos
GROUP BY category_id, region
ORDER BY avg_views DESC
"""
result = pd.read_sql(query, conn)
result.to_csv("dashboard/category_avg_views.csv", index=False)
print("Query result exported to CSV.")
