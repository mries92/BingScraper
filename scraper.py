"""Scrapes images from Bing's image of the day"""
import os
import urllib
import urllib.request
import json
from bs4 import BeautifulSoup

def scrape():
    download_images('https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8&mkt=en-US', 0)
    download_images('https://www.bing.com/HPImageArchive.aspx?format=js&idx=8&n=8&mkt=en-US', 1)

def download_images(url, imageStart):
    save_location = os.path.dirname(os.path.realpath(__file__)) + "/scrape/"
    if not os.path.exists(save_location):
        print("Making image directory...")
        os.makedirs(save_location)
    
    website = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(website, "html.parser")
    raw_json = soup.get_text()
    formatted_json = json.loads(raw_json)
    num_items = len(formatted_json['images'])
    for j in range(imageStart, num_items):
        filename = formatted_json['images'][j]['url']
        parts = filename.split("/")
        if os.path.isfile(save_location + parts[4]):
            print("Image '" + save_location + parts[4] + "' already exists.")
        else:
            print("Image output to: " + save_location + parts[4])
            urllib.request.urlretrieve("http://www.bing.com" + formatted_json['images'][j]['url'], save_location + parts[4])

def main():
    """Main entry point"""
    scrape()

if __name__ == "__main__":
    main()
