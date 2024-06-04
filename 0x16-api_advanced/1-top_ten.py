#!/usr/bin/python3
"""
This module contains a function to query the Reddit API and print the titles of the
first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
    If not a valid subreddit, print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyRedditAPI/0.1'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if not posts:
                print(None)
                return
            for post in posts:
                print(post.get('data', {}).get('title', None))
        else:
            print(None)
    except requests.RequestException:
        print(None)

