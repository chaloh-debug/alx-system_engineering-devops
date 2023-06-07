#!/usr/bin/python3
"""
queries the Reddit API
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "query"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        for hot in response.json()["data"]["children"]:
            print(hot["data"]["title"])
    else:
        print(None)
