#!/usr/bin/python3
"""
This module contains a recursive function to query the Reddit API and return a list
containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API recursively and returns a list of titles of all hot articles
    for a given subreddit. If not a valid subreddit, return None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditAPI/0.1'}
    params = {'after': after, 'limit': 100}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            after = data.get('after', None)
            children = data.get('children', [])
            for child in children:
                hot_list.append(child.get('data', {}).get('title', None))
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None

