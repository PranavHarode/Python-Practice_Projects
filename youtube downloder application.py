import yt_dlp

url = input("Enter the URL of the video:\n")

ydl_opts = {'outtmpl': r'C:\Users\prana\Downloads\%(title)s.%(ext)s'}  # Save in Downloads with video title as filename}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

