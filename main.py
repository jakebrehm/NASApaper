# -*- coding: utf-8 -*-

'''
Updates your wallpaper to today's NASA Astronomy Picture of the Day.
'''

import configparser
import ctypes
import datetime
import json
import os
from urllib.request import urlretrieve

import requests

# Get the NASA APoD API key from the configuration file
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config.get('credentials', 'api key')

# Construct and connect to the URL
api_url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'
api_response = requests.get(api_url)

# Get the image URL from the JSON file of the API response
picture_url = api_response.json()['url']

# Construct the filepath to the NASA APoD folder
user_folder = os.path.join(os.environ['USERPROFILE'])
pictures_folder = os.path.join(user_folder, 'Pictures')
destination = os.path.join(pictures_folder, 'Wallpapers', 'NASA APoD')
# Create the directory if it doesn't already exist
if not os.path.exists(destination):
	os.makedirs(destination)

# Construct the filename of filepath of the image
formatted_date = datetime.datetime.today().strftime('%m-%d-%Y')
filename = f'APoD {formatted_date}.jpg'
filepath = os.path.join(destination, filename)

# Download the file
urlretrieve(picture_url, filepath)

# Set the user's wallpaper to the downloaded file
ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 3)
