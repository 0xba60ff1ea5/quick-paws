#!/usr/bin/env python3

import os
import subprocess

def main():
    DIR = os.path.realpath(__file__).rsplit('/', 1)[0] + '/'
    

if __name__ == "__main__":
    retval = main()
    raise SystemExit(retval)
