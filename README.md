# quick-paws
Scrape your art collections from FurAffinity

# System Requirements
Currently tested with:
- python3 3.8.10
- Operating Systems tested on:
    - Linux Mint 20.3 Cinnamon 5.2.7
    - Pop!_ OS 20.04
- Other requirements listed in requirements.txt
    - See Setup Steps for installation

# Setup Steps
From the top-level directory of this project:
1. `sudo apt-get install python3-pip`
2. `pip3 install -r requirements.txt`
3. Fill out the fields in src/config/settings.json
4. Run bake_cookies.py, follow the prompts to log in

# Usage
Current options are cleanup, favorites, gallery, and scraps
Examples:
- `python3 scrape.py --help`
- `./scrape.py --favorites`
- `python3 scrape.py --gallery --scraps`
- `./scrape.py -f -g -s`

# Dev Team
0xBA60FF1EA5 - Lead Developer
