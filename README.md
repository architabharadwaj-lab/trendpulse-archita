# TrendPulse – What's Actually Trending Right Now

A 4-script Python data pipeline that fetches, cleans, analyses and visualises trending posts.

## Pipeline Order
- task1.py → Fetches trending data from HackerNews API → saves as JSON
- task2.py → Cleans data using Pandas → saves as CSV
- task3.py → Analyses data using NumPy & Pandas → saves analysis CSV
- task4.py → Creates 4 charts using Matplotlib

## Output Charts
- Top 10 posts by score
- Score distribution
- Score vs Comments
- Top 5 posts by comments

## Install
pip install requests pandas numpy matplotlib
