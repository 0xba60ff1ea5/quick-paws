#!/usr/bin/env python3
"""
Parsers for the various galleries and tabs in FurAffinity
"""

import json
from bs4 import BeautifulSoup

###################################################################################
def favoritesList(url, pages, session):
    """
    Favorites collections are handled differently than Gallery or Scraps
    Inupt : The current page of Favorites, and the List of Favorites
    Output: A list of all items in the collection
    """
    pages.append(url)
    session.get(url)
    soup = BeautifulSoup(session.page_source, "html.parser")
    for next in soup.find_all("a", class_="button standard right", href=True):
        favoritesList("https://www.furaffinity.net" + next["href"], pages, session)

###################################################################################
def imagesList(pages, images, session):
    """
    Input: List of all page URLs in Favorites, and a List for all of the image URLs
    Output: A list of all image URLs the user has favorited
    NOTE: Image URLs are not to be confused with image files
    """
    for entry in pages:
        session.get(entry)
        page = BeautifulSoup(session.page_source, "html.parser")
        gallery = page.find(id="gallery-favorites")
        for entry in gallery.find_all("figure"):
            drawing = entry.find("b").find("u").find("a")
            images.append("https://www.furaffinity.net" + drawing["href"])

###################################################################################
def imageFiles(images, files, session):
    """
    Input : A list of all image URLs the user has favorited
    Output: A list of the image file URLs
    """
    for entry in images:
        session.get(entry)
        image = BeautifulSoup(session.page_source, "html.parser")
        if image == None:
            print("Found a None image")
        f = image.find("img", id="submissionImg") # This produces Nones
        if f == None:
            print("Found a None f")
        try:
            files.append("https:" + f["data-fullview-src"])
        except TypeError as e:
            print("Unable to add f, e =", e)
            print("f =", f)
    return files

