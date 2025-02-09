#!/usr/bin/env python3
"""
NOTE: Action items marked with TODO
"""

import datetime
import json
import os
import subprocess
import sys
import time
import wget

from argparse import ArgumentParser
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# TODO: Will these paths work on a non-Linux OS?
TOP = os.path.realpath(__file__).rsplit('/', 1)[0] + '/'
sys.path.append(TOP + 'src/lib/')
from UserLib import User
sys.path.append(TOP + 'src/src/')
import furaffinity

def do_collection(collection, user, session, top_directory):
    directory = top_directory + "/" + collection
    os.mkdir(directory)

    pages = []
    images = []
    files = []

    print(f"Parsing {collection} collection to start downloading, this could take a while...")
    furaffinity.collection_pages(getattr(user, collection), pages, session)
    furaffinity.image_list(pages, images, session)
    furaffinity.image_files(images, files, session)

    for link in files:
        try:
            print(f"\nDownloading {link}...")
            f = wget.download(link, out=directory)
            print("\n")
        except Exception as e:
            print(f"Exception encountered while downloading: {e}")

def main():
    parser = ArgumentParser()
    parser.add_argument('-c', '--cleanup', action='store_true', help='Removes everything in downloads/ except .gitignore (Ignores all other options)')
    parser.add_argument('-f', '--favorites', action='store_true', help='Download user\'s Favorites')
    parser.add_argument('-g', '--gallery', action='store_true', help='Download user\'s Gallery')
    parser.add_argument('-nc', '--no_cookies', action='store_true', help='Download user\'s collection(s) without using cookies')
    parser.add_argument('-s', '--scraps', action='store_true', help='Download user\'s Scraps')
    args = parser.parse_args()

    if args.cleanup:
        # TODO: This will not work on a non-Linux OS, find a better way...
        # TODO: Add . and .. to ignore list
        cmd = f"""cd {TOP}/downloads && rm -rf $(ls -aI ".gitignore")"""
        subprocess.run(cmd, shell=True)
        return 0

    with open(TOP + 'src/config/settings.json', 'r') as settings_file:
        settings = json.load(settings_file)

    user = User(settings['username'])
    verbose = settings['verbosity']

    options = Options()
    options.add_argument("--headless")
    session = webdriver.Firefox(options=options)
    session.get("https://www.furaffinity.net/")
    
    if not args.no_cookies:
        try:
            with open(TOP + 'src/cookies/cookies.json', 'r') as cookies_file:
                cookies = json.load(cookies_file)
            for cookie in cookies:
                session.add_cookie(cookie)
            # Need to get again after adding cookies
            session.get("https://www.furaffinity.net/")
        except Exception as e:
            print(f"ERROR: Cookies not loaded, use --no_cookies option or run bake_cookies.py to create them\n{e}")
            return 1
    else:
        print("--no_cookies option selected, some drawings in collection(s) may be skipped for download...")

    d = datetime.date.today()
    t = time.time()
    directory = TOP + "downloads/" + str(d) + "-" + str(t) + "-" + str(settings['username'])
    os.mkdir(directory)

    if args.favorites:
        do_collection("favorites", user, session, directory)

    if args.gallery:
        do_collection("gallery", user, session, directory)

    if args.scraps:
        do_collection("scraps", user, session, directory)

    return 0

if __name__ == "__main__":
    retval = main()
    raise SystemExit(retval)
