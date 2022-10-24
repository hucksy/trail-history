import io
import json
import requests
import tarfile
from . import sentinel_api_params as sp


def get_first_image():
    sentinel_response = requests.post(url=sp.SENTINEL_BASE_URL,
                                      headers=sp.sentinel_headers,
                                      json=sp.sentinel_request_body)
    print(sentinel_response)
    with open('sntl1.jpeg', 'wb') as file:
        file.write(sentinel_response.content)

    tar = tarfile.open(fileobj=io.BytesIO(sentinel_response.content))
    userdata = json.load(tar.extractfile(tar.getmember('userdata.json')))
    print(f"userdata: \n{userdata}")

# get_new_images():
"""
- check if we should get new images, ie, is the date greater than the most recent file date?
  - if so, request new files from API: ...request more than 1 day?
"""


# backfill():
"""
- run when filesystem is empty, request multiple images for storage
"""


# save_image()
"""
- saves image to file system
- saves filename and meta to db
"""
