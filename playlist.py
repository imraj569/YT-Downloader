from asyncio import streams
from pytube import Playlist
from colorama import Fore
import colorama
colorama.init(autoreset=True)
link = input(Fore.RED+"Enter YouTube Playlist URL: ")

yt_playlist = Playlist(link)

for video in yt_playlist.videos:
    print(Fore.YELLOW+f'please wait {video.title} is downloading...')
    video.streams.get_by_itag(18).download("E:\mca playlist\computer")
    print(Fore.GREEN+"Video Downloaded: ", video.title)
    # print(video.streams.filter(progressive='True'))

print(Fore.GREEN+"\nAll videos are downloaded.")