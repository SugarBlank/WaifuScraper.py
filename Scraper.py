import pixivapi
from pixivapi import ContentType
from pixivapi import Client
from datetime import datetime
from pathlib import Path
from pixivapi import Size
from pixivapi import Sort
from pixivapi import SearchTarget
from pixivapi import Visibility
#login section.

client = Client()



userid = input("Enter your userid.\n")

password = input("Enter your password.\n")

client.login(username, password)

print(f"Logged in as {username}")


needs = input("What would you like to do today?\n")

#fetch an illustration found, using the id provided.
if needs == "illustration download":
    illustration_id = input("Enter the illustration id.\n")
    illustration = client.fetch_illustration(illustration_id)
    illustration.download(directory=Path.home() / "PixivImages", size=Size.ORIGINAL)
    print(f"{illustration_id} was downloaded.")
else:
    pass

#downloads the artist id's art.

if needs == "artist download":
    
    downloaded = 0
    artist_id = input("Enter artist id to download their art:\n")
    num = input("How much art do you want to download?\n")    
    print(f"Looking for {num} images.")
    directory = Path.home() / 'PixivImages'
    get = client.fetch_user_illustrations(artist_id)
    print(f"Downloading files from artist id {artist_id}.")
    while True:
        for illustration in get['illustrations']:
            illustration.download(directory=directory, size=Size.ORIGINAL)
            downloaded += 1
            
            if int(downloaded) == int(num):
                print("Finished downloading all the images.")
                stop = True
                break    
        if not get['next']:
            print("No more art to download.")
            break
    get = client.fetch_user_illustrations(artist_id, offset=get['next'])

#searches for tags provided.

if needs == "search":
    tags = input("Enter the tags you want to look up.\n")
    downloaded = 0
    num = input("How much art do you want to donwload?\n")    
    print(f"Looking for {num} images.")
    directory = Path.home() / 'PixivImages'
    get = client.search_illustrations(word=tags, search_target=SearchTarget.TAGS_PARTIAL, sort=Sort.DATE_DESC)
    print(f"Searching for {tags}")
    while True:
        for illustration in get['illustrations']:
            illustration.download(directory=directory, size=Size.ORIGINAL)
            downloaded += 1
            
            if int(downloaded) == int(num):
                print("Finished downloading all the images.")
                stop = True
                break    
        if stop:
            break
        if not get['next']:
            print("No more art to download.")
            break

#downloads x amount of art from y's recommended feed.

if needs == "recommended":
    directory = Path.home() / "PixivImages"
    downloaded = 0
    num = input("How many images do you want to download?\n")
    
    print(f"Looking for {num} images.")
    get = client.fetch_illustrations_recommended(content_type=ContentType.ILLUSTRATION)
    print("Downloading recommended art....")
    while True:
        for illustration in get['illustrations']:
            illustration.download(directory=directory, size=Size.ORIGINAL)
            downloaded += 1
            
            if int(downloaded) == int(num):
                print("Finished downloading all the images.")
                stop = True
                break    
        if stop:
            break
        if not get['next']:
            print("Finished downloading recommended pictures.")
            break

#downloads x amount of art from y's followed artists.

if needs == "followed":
    directory = Path.home() / "PixivImages"
    downloaded = 0
    num = input("How many images do you want to download?\n")
    
    print(f"Looking for {num} images....")
    get = client.fetch_illustrations_following(visibility=Visibility.PUBLIC)
    print("Downloading art from followed creators....")
    while True:
        for illustration in get['illustrations']:
            illustration.download(directory=directory, size=Size.ORIGINAL)
            downloaded += 1
            
            if int(downloaded) == int(num):
                print("Finished downloading all the images.")
                stop = True
                break    
        if stop:
            break
        if not get['next']:
            print("Finished downloading artist feed.")
            break

#downloads related images.

if needs == "related download":
    directory = Path.home() / "PixivImages"
    illustration_id = input("Enter the illustration id.\n")
    downloaded = 0
    num = input("How many related images do you want to download?\n")
    
    print(f"Looking for {num} images....")
    illustration = client.fetch_illustration_related(illustration_id)
    
    while True:
        for illustration in illustration['illustrations']:
            illustration.download(directory=directory, size=Size.ORIGINAL)
            downloaded += 1
            
            if int(downloaded) == int(num):
                print("Finished downloading all the images.")
                stop = True
                break    
        if stop:
            break
        if not get['next']:
            print("Finished downloading recommended pictures.")
            break

if needs == "help":
    print("Hello, welcome to PixivWaifuScraper! Here is what you can do with the scraper:\n illustration download: Makes a folder called PixivImages and sends an image there. You must provide the id.\n", 
    "artist download: Downloads art from a certain artist to PixivImages. Must provide their id.\n search: Searches for tags you typed in and downloads them to PixivImages.\n", 
    "recommended: Downloads recommended art for you to PixivImages folder.\n followed: Downloads images from people you follow to Pixiv Images folder.\n related: Downloads images related to the one you provided.")