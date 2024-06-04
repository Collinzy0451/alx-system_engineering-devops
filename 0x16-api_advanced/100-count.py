#!/usr/bin/python3
"""
This module contains a recursive function to query the Reddit API,
parse the titles of all hot articles, and print a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Queries the Reddit API recursively, parses titles of hot articles,
    and prints a sorted count of given keywords.
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
                title = child.get('data', {}).get('title', "").lower()
                for word in word_list:
                    count = title.split().count(word.lower())
                    if count > 0:
                        if word.lower() in word_count:
                            word_count[word.lower()] += count
                        else:
                            word_count[word.lower()] = count
            
            if after is not None:
                return count_words(subreddit, word_list, after, word_count)
            else:
                if not word_count:
                    return
                sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_word_count:

