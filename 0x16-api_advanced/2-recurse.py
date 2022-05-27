#!/usr/bin/python3
"""
Function that queries Reddit API and returns
the titles of all hot articles for a given subreddit
"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Request to reddit api and process response"""
    import requests

    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": count, "after": after},
                            headers={"User-Agent": "mozilla"},
                            allow_redirects=False)
    if response.status_code >= 400:
        return None

    h_list = hot_list + [child.get("data").get("title")
                         for child in response.json()
                         .get("data")
                         .get("children")]

    info = response.json()
    if not info.get("data").get("after"):
        return h_list

    return recurse(subreddit, h_list, info.get("data").get("count"),
                   info.get("data").get("after"))
