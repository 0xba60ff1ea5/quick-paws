#!/usr/bin/env python3
"""
Parsers for the various galleries and tabs in FurAffinity
"""

import json
from bs4 import BeautifulSoup

###################################################################################
def collection_pages(url, pages, session):
    """
    Populate the pages list with each page of a given collection
    """
    pages.append(url)
    session.get(url)
    soup = BeautifulSoup(session.page_source, "html.parser")
    for button in soup.find_all("form"):
        if button["action"].split("/")[-1] == "next":
            page = f"https://www.furaffinity.net{button['action']}"
            print(f"Matt: Adding page {page}")
            collection_pages(page, pages, session)
            break

###################################################################################
def image_list(pages, images, session):
    """
    Populate the images list with each image on a given page
    """
    for page in pages:
        print(f"Matt: Parsing page {page}")
        session.get(page)
        soup = BeautifulSoup(session.page_source, "html.parser")
        gallery = soup.find(class_="gallery-section")
        for figure in gallery.find_all("figure"):
            drawing_link = figure.find("b").find("u").find("a")
            images.append(f"https://www.furaffinity.net{drawing_link['href']}")

###################################################################################
def image_files(images, files, session):
    """
    Populate the files list with the download link in a given image
    """
    # TODO: They're not images, they could be text files, sound files, etc.
    for image in images:
        print(f"Matt: Parsing image {image}")
        session.get(image)
        soup = BeautifulSoup(session.page_source, "html.parser")
        # The buttons that appear directly beneath an image
        image_buttons = soup.find_all("a", class_="button standard mobile-fix")
        for button in image_buttons:
            if "Download" in button.string:
                try:
                    files.append(f"https:{button['href']}")
                except TypeError as e:
                    print(f"Unable to add f, e = {e}\nbutton = {button}")
                break
    return files

