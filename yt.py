import progressbar as progress
from pytube import YouTube
from sys import argv
from pytube.cli import on_progress


welcomeMessage = 'Sighlos Youtube Video Downloader'
new_str = welcomeMessage.center(20)
print(new_str)


link = input("Enter Youtube link: ")

yt = YouTube(link, on_progress_callback=on_progress)

print("Is this the video you are trying to download? ", yt.title)
userinput = input("Enter yes or no: ")
if userinput == "yes":

    yd = yt.streams.get_highest_resolution()
    filelocation = input("Enter your file location: ")

    yd.download(filelocation)
    print("Finished Downloading ", yt.title)
else:
    print("We are having issues")
    print("Exiting now")
    exit