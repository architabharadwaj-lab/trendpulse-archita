import requests
import json

url = "https://www.reddit.com/r/all/hot.json"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

data = response.json()

posts = []

for post in data["data"]["children"]:
    info = post["data"]

    posts.append({
        "title": info["title"],
        "subreddit": info["subreddit"],
        "score": info["score"],
        "url": "https://www.reddit.com" + info["permalink"]
    })

with open("data.json", "w") as file:
    json.dump(posts, file, indent=4)

print("✅ Task 1 Done")