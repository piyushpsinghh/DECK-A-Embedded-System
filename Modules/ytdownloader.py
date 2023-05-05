from pytube import YouTube
def downloader():
    link = input('enter the link : ')
    yt = YouTube(link)
    print('Title : ',yt.title)
    print('Number of view : ',yt.views)


    yt.streams.filter(only_audio=True)
    yt.streams.filter(only_video=True)
    yt.streams.filter(progressive=True)
    ys=yt.streams.get_highest_resolution()

    ys.download()
    ys.download('location')

    print("VIDEO DOWNLOAD SUCCESFULLY")


#kartik