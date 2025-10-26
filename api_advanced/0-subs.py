#!/usr/bin/python3
"""
Reddit API: number_of_subscribers

PEP 8–compliant implementation that queries the Reddit API
and returns total subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers for a subreddit, or 0 if invalid.

    Args:
        subreddit (str): Subreddit name (e.g., "python").

    Returns:
        int: Subscriber count, or 0 for invalid/redirected responses.
    """
    if not isinstance(subreddit, str) or not subreddit:
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "alu-scripting-task0:nawaf/1.0 (contact: example@example.com)"
    }

    try:
        # Do not follow redirects to avoid search-result fallbacks
        resp = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
    except requests.RequestException:
        return 0

    if resp.status_code != 200:
        return 0

    try:
        data = resp.json()
    except ValueError:
        return 0

    # Extract subscribers from JSON safely
    return int(data.get("data", {}).get("subscribers", 0))
