from bing_image_downloader.downloader import download
from google_images_download import google_images_download   #importing the library


query_string = "Chinese apple tree"
n_samples = 200

# bing load
download(
    query_string,
    limit=n_samples,
    output_dir='tests/bing',
    adult_filter_off=True,
    force_replace=False,
    timeout=60
)

# google load
arguments = {
    "keywords": query_string,
    "limit": n_samples,
    "print_urls": True,
    "chromedriver": "../chromedriver",
    "output_directory": "tests/google"
}   #creating list of arguments

paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images