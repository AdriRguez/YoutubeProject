from pytube import YouTube
from pytube import Playlist

#link = input("Enter the link: ")
#yt = YouTube("https://www.youtube.com/watch?v=P0coAxDK5L4")
p = Playlist('https://www.youtube.com/watch?v=htcVW-nLV7E&list=PL3qLpIJpAr6VoJYGeNNJ-whY_EY02bXt0')

for video in p.videos:
    video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
print('done')

#Title of video
#print("Title: ",yt.title)
#Number of views of video
#print("Number of views: ",yt.views)
#Length of the video
#print("Length of video: ",yt.length,"seconds")
#Description of video
#print("Description: ",yt.description)
#Rating
#print("Ratings: ",yt.rating)

#yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

