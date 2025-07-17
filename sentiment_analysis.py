import pandas as pd
from textblob import TextBlob

# Load datasets
us = pd.read_csv('datasets/USvideos.csv')
gb = pd.read_csv('datasets/GBvideos.csv')

# Add region columns
us['region'] = 'US'
gb['region'] = 'GB'


# Combine
df = pd.concat([us, gb], ignore_index=True)

# Clean
df['trending_date'] = pd.to_datetime(df['trending_date'], format='%y.%d.%m')
df['views'] = pd.to_numeric(df['views'], errors='coerce')
df['likes'] = pd.to_numeric(df['likes'], errors='coerce')
df['comment_count'] = pd.to_numeric(df['comment_count'], errors='coerce')

# Sentiment Analysis
df['title_sentiment'] = df['title'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
df['tags'] = df['tags'].str.replace('|', ' ')
df['tags_sentiment'] = df['tags'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

# Save cleaned file
df.to_csv('dashboard/youtube_dashboard.csv', index=False)
print("Cleaned dataset saved for Tableau.")
