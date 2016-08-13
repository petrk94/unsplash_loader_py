#import libaries
import requests
import subprocess


with open("TranscodedWallpaper", "wb") as f:
    response = requests.get("https://source.unsplash.com/random", stream=True)

    if not response.ok:
        print("URL could been retrieved")
        exit

    # Write the content of 'response' (photo_url)
    # in pieces into the file
    for block in response.iter_content(1024):
        f.write(block)

		
subprocess.call(["move", "TranscodedWallpaper", "C:\\Users\%username%\AppData\Roaming\Microsoft\Windows\Themes"], shell=True)

subprocess.call(["cd", "C:\\Users\%username%\AppData\Roaming\Microsoft\Windows\Themes"], shell=True)
subprocess.call(["RUNDLL32.EXE", "USER32.DLL","UpdatePerUserSystemParameters", "1", "True"], shell=True)
