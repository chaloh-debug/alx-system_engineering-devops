#!/usr/bin/python3
"""
Recursive queries. Reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    recursive query of titles of all hot articles
    """
    url = "https://www.reddit.com/r/{}/hot.json?after={}".
    format(subreddit, after)
    headers = {
        "User-Agent": "query"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        results = response.json()["data"]
        after = results.get("after")
        results = results.get("children")
        for res in results:
            hot_list.append(res["data"]["title"])
        if after is not None:
            recurse(subreddit, hot_list, after)
        return (hot_list)
    else:
        return (None)
