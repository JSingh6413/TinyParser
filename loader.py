#! /usr/bin/env python3

from bing_image_downloader.downloader import download
from google_images_download import google_images_download


query_string = "Chinese apple tree"
n_samples = 2

# bing load
download(
    query_string,
    limit=n_samples,
    output_dir='images/bing',
    adult_filter_off=True,
    force_replace=False,
    timeout=60
)

# google load
arguments = {
    "keywords": query_string,
    "limit": n_samples,
    "print_urls": True,
    "chromedriver": "chromedriver",
    "output_directory": "images/google"
}

response = google_images_download.googleimagesdownload()
paths = response.download(arguments)
print(paths)
