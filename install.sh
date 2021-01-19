#! /bin/bash

# delete if exists
if [ -d "venv" ]
then
    rm -rf venv
fi

# make new env
virtualenv venv
source venv/bin/activate

# install dependeciens
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt

# install google scraper
cd google-images-download
python3 setup.py install
cd ..

# test scrapers
if [ "$1" = "-t" ]
then
    python3 tests/google.py
    python3 tests/bing.py
fi

deactivate