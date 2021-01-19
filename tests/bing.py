from bing_image_downloader.downloader import download

query_string = "Corgi"

download(
    query_string,
    limit=20,
    output_dir='tests/bing',
    adult_filter_off=True,
    force_replace=False,
    timeout=60
)