#import libaries
import feedparser
import requests

#parse the rss feed of unsplash
d = feedparser.parse('https://unsplash.com/rss')

#save the content of summary entries in variable
e = (d.entries[0]["summary"])

# create file to save the content
file = open("unsplash.dat", "w")
file.write(d.entries[0]["summary"])
file.close()
file = open("unsplash.dat", "r")

xml = file.read()

#Split the necessary tags to get the img tag
xml_splitted = xml.split(" ")
photo_tag = (xml_splitted[4])
photo_img = photo_tag.split("\"")
#print(photo_img)


# print the image raw URL
photo_url = (photo_img[1])
print("done")
print(photo_url)

# Download the photo
# get the photo by requests.get from photo_url
# and safe it in variable f
with open("Unsplash.jpg", "wb") as f:
    response = requests.get(photo_url, stream=True)

    if not response.ok:
        print("URL could been retrieved")
        exit

    # Write the content of 'response' (photo_url)
    # in pieces into the file
    for block in response.iter_content(1024):
        f.write(block)
