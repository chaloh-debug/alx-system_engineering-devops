#!/usr/bin/python3
"""
queries the Reddit API and returns the number of
subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns number of subscribers to a subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "query"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return (response.json()["data"]["subscribers"])
    return 0
