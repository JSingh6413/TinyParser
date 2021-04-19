#! /usr/bin/env python3

from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {
    "keywords": "Corgi",
    "limit": 20,
    "print_urls": True,
    "chromedriver": "../chromedriver",
    "output_directory": "google"
}   #creating list of arguments

paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images
