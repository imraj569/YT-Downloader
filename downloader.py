from pytube import YouTube
import os , sys
from pytube import Playlist
from colorama import Fore
import colorama
colorama.init(autoreset=True)

def main():
    ClearCon()
    print(Fore.CYAN+'''   
╭╮╱╱╭┳━━━━╮╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╭╮
┃╰╮╭╯┃╭╮╭╮┃╰╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱┃┃
╰╮╰╯╭┻╯┃┃╰╯╱┃┃┃┣━━┳╮╭╮╭┳━╮┃┃╭━━┳━━┳━╯┣━━┳━╮
╱╰╮╭╯╱╱┃┃╱╱╱┃┃┃┃╭╮┃╰╯╰╯┃╭╮┫┃┃╭╮┃╭╮┃╭╮┃┃━┫╭╯
╱╱┃┃╱╱╱┃┃╱╱╭╯╰╯┃╰╯┣╮╭╮╭┫┃┃┃╰┫╰╯┃╭╮┃╰╯┃┃━┫┃
╱╱╰╯╱╱╱╰╯╱╱╰━━━┻━━╯╰╯╰╯╰╯╰┻━┻━━┻╯╰┻━━┻━━┻╯
------------------------------------------
Author: Rajkishor patra
Git Hub:https://github.com/imraj569   
------------------------------------------''')
    print('''
    [1] Single video
    [2] Playlist
    [3] Exit
    ''')
    v = input('choose you want: ')
    if '1' in v:
        video()
    elif '2' in v:
        playlist()
    elif '3' in v:
        print('bye....')
        sys.exit()
    else:
        print(Fore.RED+'somthing went wrong try again...')

def video():
    url = input('Enter youtube video url: ')
    ClearCon()
    print(Fore.CYAN+'''
------------------------
[1] 360p
[2] 720p
[3] Highest possible !
[4] Exit
------------------------''')
    res = input('Enter resolution of video: ')
    ClearCon()
    try:
        if os.name in ('nt', 'dos'):
            try:
                file = os.mkdir('D:\YT-Downloader')
                
            except:
                file = 'D:\YT-Downloader' 
        else:
            try:  
                file = os.mkdir('/sdcard/Download/YT-Downloader')
            except:
                file = '/sdcard/Download/YT-Downloader'
    except:
        file = input(Fore.YELLOW+'Somthing went wrong type folder path manualy: ') 

    video = YouTube(url)
    tit = video.title
    ClearCon()
    if '1' in res:
        try:
            print(Fore.CYAN+f'please wait downloading {tit} in 360p...')
            video.streams.get_by_itag(18).download(file)
            ClearCon()
            print(Fore.GREEN+f'{tit} Download successful...')
            input(Fore.YELLOW+'Press enter to continue..')          
            
        except:
            print(Fore.RED+'Resolution not found try another resolution..')

    
    elif '2' in res:
        try:
            print(Fore.CYAN+f'please wait downloading {tit} in 720p...')
            video.streams.get_by_itag(22).download(file)
            ClearCon()
            print(Fore.GREEN+f'{tit} Download successful...')
            input(Fore.YELLOW+'Press enter to continue..')        
            
        except:
            print(Fore.RED+'Resolution not found try another resolution..')

    elif '3' in res:
        try:
            print(Fore.CYAN+f'please wait downloading {tit} in high resolution...')
            video.streams.get_highest_resolution().download(file)
            ClearCon()
            print(Fore.GREEN+f'{tit} Download successful...')
            input(Fore.YELLOW+'Press enter to continue..')
                  
            
        except:
            print(Fore.RED+'Resolution not found try another resolution..')


    elif '4' in res:
        print(Fore.BLUE+'Thanks for using YT downloader...')
        sys.exit()

    else:
        print(Fore.RED+'somthing went wrong try again!')

def ClearCon():
    try:
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
            os.system(command)
        else:
            os.system('clear')
    except:
        print('somthing want wrong')

def playlist():
    url = input('Enter Playlist url: ')
    ClearCon()
    print(Fore.CYAN+'''
------------------------
[1] 360p
[2] 720p
[3] Highest possible !
[4] Exit
------------------------''')
    res = input(Fore.BLUE+'Enter resolution of videos: ')
    file_name = input(Fore.BLUE+'Enter playlist Name: ')
    pl_name = file_name.replace(' ','_')
    try:
        if os.name in ('nt', 'dos'):
            try:
                file = os.mkdir(f'D:\YT-Downloader\{pl_name}')
            except:
                file = 'D:\YT-Downloader'
        else:
            try:  
                file = os.mkdir(f'/sdcard/Download/YT-Downloader/{pl_name}')
            except:
                file = '/sdcard/Download/YT-Downloader'
    except:
        file = input(Fore.YELLOW+'Somthing went wrong type folder path manualy: ') 
    
    ClearCon()
    yt_playlist = Playlist(url)
    a = yt_playlist.title
    if '1' in res:
        for video in yt_playlist.videos:
            print(Fore.YELLOW+f'please wait downloading {a}')
            video.streams.get_by_itag(18).download(file)
            print(Fore.GREEN+'Download successful...')

        print(Fore.GREEN+"\nAll videos are downloaded.")
    
    elif '2' in res:
        for video in yt_playlist.videos:
            print(Fore.YELLOW+f'please wait downloading {a}')
            video.streams.get_by_itag(22).download(file)
            print(Fore.GREEN+'Download successful...')

        print(Fore.GREEN+"\nAll videos are downloaded.")

    elif '3' in res:
        for video in yt_playlist.videos:
            print(Fore.YELLOW+f'please wait downloading {a}')
            video.streams.get_highest_resolution().download(file)
            print(Fore.GREEN+'Download successful...')

        print(Fore.GREEN+"\nAll videos are downloaded.")

    elif '4' in res:
        ClearCon()
        print(Fore.GREEN+'Bye Thanks for using YT-Downloader ....')
        sys.exit()
    
    else:
        print(Fore.RED+'somthing went wrong try again...')

if __name__ == "__main__":
    while True:
        main()