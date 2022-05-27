#!/usr/bin/python3
"""
Function that queries Reddit API
and returns the number of suscribers
"""


def number_of_subscribers(subreddit):
    """Request to reddit api and process response"""
    import requests

    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "Mozilla",
                                     "Content-Type": "application/json"},
                            allow_redirects=False,)
    if response.status_code >= 300:
        return 0

    return response.json().get("data").get("subscribers")
