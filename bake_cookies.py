#!/usr/bin/env python3

import json
import os
import subprocess
import time

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
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

    try:
        with open(TOP + 'src/.cookies/cookie_key.bin', 'rb') as key_file:
            print("Using pre-existing key to encrypt cookies...")
            key = key_file.read()
    except Exception as e:
        print(f"No pre-existing key found, making a new one...\n{e}")
        cmd = "touch " + TOP + "src/.cookies/cookie_key.bin"
        subprocess.run(cmd, shell=True)
        key = get_random_bytes(32)
        with open(TOP + 'src/.cookies/cookie_key.bin', 'wb') as key_file:
            key_file.write(key)

    cipher = AES.new(key, AES.MODE_CTR)
    cmd = "touch " + TOP + "src/.cookies/cookies.json"
    subprocess.run(cmd, shell=True)

    with open(TOP + 'src/.cookies/cookies.json', 'wb') as cookie_file:
        cookie_string = json.dumps(session.get_cookies())
        cookie_bin = cipher.encrypt(cookie_string.encode())
        cookie_file.write(cookie_bin)
        # data = cipher.encrypt(session.get_cookies().__str__().encode())
        # print(f"Matt: cookies = {session.get_cookies()}")
        # print(f"Matt: data = {data}")
        # json.dump(data, cookie_file)
        # cookie_file.write(data)

if __name__ == "__main__":
    retval = main()
    raise SystemExit(retval)
