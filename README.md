# 📊 YouTube Trending Video Analytics

This project analyzes YouTube trending video data from multiple countries to uncover patterns in viewer behavior, category popularity, and sentiment. The insights help content creators, marketers, and analysts understand what drives video virality across regions

## 📁 Dataset

- **Source**: [Kaggle - Trending YouTube Video Statistics](https://www.kaggle.com/datasets/datasnaek/youtube-new)
- **Files Used**:
  - `USvideos.csv`
  - `GBvideos.csv`
- **Columns Used**: `video_id`, `title`, `category_id`, `views`, `likes`, `comment_count`, `region`, `tags`, `trending_date`

## 🎯 Objective

- Identify the most popular content categories by region
- Perform sentiment analysis on video titles and tags
- Compare engagement (likes/comments) across regions
- Visualize trends using Power BI

## 🛠️ Tools & Technologies

| Tool       | Purpose                         |
|------------|---------------------------------|
| Python     | Data cleaning, processing       |
| Pandas     | DataFrame manipulation          |
| TextBlob   | Sentiment analysis              |
| SQLite     | SQL queries and aggregation     |
| Power BI   | Interactive visual dashboards   |
| Seaborn    | Data visualization (Python)     |

## 🧪 Steps Involved

1. **Data Cleaning**
   - Combined multiple country datasets
   - Removed duplicates and nulls
   - Standardized column names and data types

2. **Sentiment Analysis**
   - Applied `TextBlob` on `title` and `tags` columns
   - Created `title_sentiment` and `tags_sentiment` scores

3. **SQL Aggregations**
   - Loaded cleaned data into SQLite
   - Queried average views per category and region

4. **Visualization**
   - Created Power BI dashboard:
     - Views over time
     - Sentiment comparison by region
     - Top liked/commented videos
     - Category performance by region

## 📈 Key Insights

- **Music** is the most viewed genre across all regions.
- Titles with **positive sentiment** attract higher engagement.
- **US content dominates** in trending views (≈70% of dataset).
- **Trending durations are short** (1–2 days per video).
- **BTS** videos dominate likes/comments in both US and GB.

## 📦 Project Structure

youtube-trending/
├── datasets/
│ ├── USvideos.csv
│ ├── GBvideos.csv
│ ├── INvideos.csv
├── notebooks/
│ ├── sentiment_analysis.ipynb
│ ├── sql_queries.ipynb
├── sql/
│ └── youtube_trending.db
├── dashboard/
│ ├── youtube_dashboard.csv
│ ├── category_avg_views.csv
│ ├── visuals.png
├── report/
│ └── Youtube_Trending_Analytics_Report.pdf
└── README.md
