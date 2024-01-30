#!/usr/bin/env python3

"""
NOTE: Action items marked with TODO
"""

import json
import os
import sys
from argparse import ArgumentParser
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Determine top-level directory of the project
TOP = os.path.realpath(__file__).rsplit('/', 1)[0] + '/'
sys.path.append(TOP + 'src/lib/')
from UserLib import User
sys.path.append(TOP + 'src/src/')
import furaffinity

def main():
    # Parse user input
    parser = ArgumentParser()
    parser.add_argument('-f', '--favorites', action='store_true', help='Download user\'s Favorites')
    parser.add_argument('-g', '--gallery', action='store_true', help='Download user\'s Gallery')
    parser.add_argument('-s', '--scraps', action='store_true', help='Download user\'s Scraps')
    args = parser.parse_args()

    # Build variables from user input
    FAVORITES = args.favorites
    GALLERY = args.gallery
    SCRAPS = args.scraps

    # Read the settings.json file
    with open(TOP + 'src/config/settings.json', 'r') as settings_file:
        settings = json.load(settings_file)

    # Set up User class
    user = User(settings['username'])

    # Create session and add cookies
    options = Options()
    options.add_argument("--headless")
    session = webdriver.Firefox(options=options)
    session.get("https://www.furaffinity.net/")
    with open(TOP + 'src/config/cookies.json', 'r') as cookies_file:
        cookies = json.load(cookies_file)
    for cookie in cookies:
        session.add_cookie(cookie)
    session.get("https://www.furaffinity.net/")
    
    # Take actions based on user input
    if FAVORITES:
        faves = []
        images = []
        files = []
        furaffinity.favoritesList(user.favorites, faves, session)
        furaffinity.imagesList(faves, images, session)
        furaffinity.imageFiles(images, files, session)

    # Download each file to the download directory

if __name__ == "__main__":
    retval = main()
    raise SystemExit(retval)
