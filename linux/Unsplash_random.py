#import libaries
import requests

with open("Unsplash_random.jpg", "wb") as f:
    response = requests.get("https://source.unsplash.com/random", stream=True)

    if not response.ok:
        print("URL could been retrieved")
        exit

    # Write the content of 'response' (photo_url)
    # in pieces into the file
    for block in response.iter_content(1024):
        f.write(block)
