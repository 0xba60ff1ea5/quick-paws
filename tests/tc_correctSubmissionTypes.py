#!/usr/bin/env python3

"""
run imagesList and imageFiles
"""

import os
import sys

TOP = os.path.realpath(__file__).rsplit('/', 1)[0] + '/../'
sys.path.append(TOP + 'src/src/')
import furaffinity

def main():
    test_files = [
        # Animation
        "https://www.furaffinity.net/view/53354589/",
        # Text
        "https://www.furaffinity.net/view/12573381/",
        # Text
        "https://www.furaffinity.net/view/37322622/",
        # Audio
        "https://www.furaffinity.net/view/55369678/",
        # Sculpt
        "https://www.furaffinity.net/view/55372540/",
        # General
        "https://www.furaffinity.net/view/54286607/",
        # Mature
        "https://www.furaffinity.net/view/53154751/",
        # Adult
        "https://www.furaffinity.net/view/50726957/"
    ]

    # Set up a session
    session = webdriver.Firefox()
    session.get("https://www.furaffinity.net/")
    with open(TOP + 'src/config/cookies.json', 'r') as cookies_file:
        cookies = json.load(cookies_file)
    for cookie in cookies:
        session.add_cookie(cookie)
    session.get("https://www.furaffinity.net/")

    # Scrape pages
    files = []
    furaffinity.imageFiles(images, files, session)

if __name__ == "__main__":
    retval = main()
    raise SystemExit(retval)