'''Getting images from specifics links.

The links must be listed in a .txt file.
Informe the file path by a command line parameter.

    python fetching_images.py --links chihiro.txt
'''

import requests
import shutil
import argparse
import os

def get_image(link):

    filename = os.path.basename(link)

    response = requests.get(link, stream=True, headers={'User-Agent': 'Custom'})

    if not os.path.exists("images"):
        os.mkdir("images")

    if response.status_code == 200:
        response.raw.decode_content = True
        with open(os.path.join("images", filename), 'wb') as file:
            shutil.copyfileobj(response.raw, file)

        print(f"Downloaded image at {filename}")

    else:
        print(f"Could not retrive image {filename} from {link} : {response.status_code}")
        print(f"Request headers: {response.request.headers}")
        print(f"Response headers: {response.headers}")



parser = argparse.ArgumentParser("Downloading images")
parser.add_argument("--links", dest="links")

args = parser.parse_args()

with open(args.links, "r") as links :
    for link in links:
        get_image(link.strip())

