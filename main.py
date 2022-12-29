from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try: 
        youtubeObject.download()
    except:
        print("There has been an error downloading your youtube video")
    print("This download has completed! yay!")

link = input("Put your youtube link here! URL: ")
Download(link)
