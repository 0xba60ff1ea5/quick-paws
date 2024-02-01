#!/usr/bin/env python3

import json
import os
import subprocess
import time
from selenium import webdriver

TOP = os.path.realpath(__file__).rsplit('/', 1)[0] + '/'

def main():
    """
    Script for first-time setup of cookies
    """
    url = "https://www.furaffinity.net/login/"

    # Prompt user to log in
    session = webdriver.Firefox()
    session.get(url)
    # TODO: Find a better solution than this...
    print("Waiting 60 seconds for user to log in...")
    time.sleep(60)

    # Store cookies in .json file
    cmd = "touch " + TOP + "src/config/cookies.json"
    subprocess.run(cmd, shell=True)
    with open(TOP + 'src/config/cookies.json', 'w') as cookie_file:
        json.dump(session.get_cookies(), cookie_file)

if __name__ == "__main__":
    retval = main()
    raise SystemExit(retval)
