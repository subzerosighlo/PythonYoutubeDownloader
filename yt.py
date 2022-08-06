from pytube import YouTube
from sys import argv


welcomeMessage = 'Sighlos Youtube Video Downloader'
new_str = welcomeMessage.center(20)
print(new_str)
link = input("Enter Youtube link: ")

yt = YouTube(link)

print("Title: ", yt.title)

yd = yt.streams.get_highest_resolution()
filelocation = input("Enter your file location: ")

yd.download(filelocation)