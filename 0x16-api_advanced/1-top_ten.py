#!/usr/bin/python3
"""
Function that queries Reddit API
and prints the first 10 hot post titles
"""


def top_ten(subreddit):
    """Request to reddit api and process response"""
    import requests

    response = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "Mozilla"},
                            allow_redirects=False)

    if response.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in response.json().get("data").get("children")]
