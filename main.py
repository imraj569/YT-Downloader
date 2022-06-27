from pytube import YouTube
import os , sys
from colorama import Fore
import colorama
colorama.init(autoreset=True)


def intro():
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
    url = input('Enter youtube video url: ')
    ClearCon()
    print(Fore.CYAN+'''
------------------------
[1] 360p
[2] 480p
[3] 720p
[4] Highest possible !
[5] Exit
------------------------''')
    res = input('Enter resolution of video: ')
    ClearCon()
    file = input(Fore.YELLOW+'Enter Downloading path: ')
    video = YouTube(url)
    tit = video.title
    ClearCon()
    if '1' in res:
        try:
            print(Fore.CYAN+f'please wait downloading {tit} in 360p...')
            video.streams.get_by_itag(18).download(file)
            print(Fore.GREEN+'Download successful...')        
            
        except:
            print(Fore.RED+'somthing went wrong...')

    elif '2' in res:
        try:
            print(Fore.CYAN+f'please wait downloading {tit} in 480p...')
            video.streams.get_by_itag(135).download(file)
            print(Fore.GREEN+'Download successful...')        
            
        except:
            print(Fore.RED+'somthing went wrong...')

    elif '3' in res:
        try:
            print(Fore.CYAN+f'please wait downloading {tit} in 720p...')
            video.streams.get_by_itag(22).download(file)
            print(Fore.GREEN+'Download successful...')        
            
        except:
            print(Fore.RED+'somthing went wrong...')

    elif '4' in res:
        try:
            print(Fore.CYAN+f'please wait downloading {tit} in high resolution...')
            video.streams.get_highest_resolution().download(file)
            print(Fore.GREEN+'Download successful...')        
            
        except:
            print(Fore.RED+'somthing went wrong...')


    elif '5' in res:
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

intro()