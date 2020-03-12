from termcolor import colored
import random

banner1 =  """
 _____     _       _____         
|  _  |_ _| |_ ___|     |_ _ _ _ 
|     | | |  _| . | | | | | |_'_|
|__|__|___|_| |___|_|_|_|___|_,_|
"""   
banner2 = """
  ___        _       ___  ___           
 / _ \      | |      |  \/  |           
/ /_\ \_   _| |_ ___ | .  . |_   ___  __
|  _  | | | | __/ _ \| |\/| | | | \ \/ /
| | | | |_| | || (_) | |  | | |_| |>  < 
\_| |_/\__,_|\__\___/\_|  |_/\__,_/_/\_\\
"""

banner3 = """
 ________
< AutoMux >
 --------
       \   ,__,
        \  (oo)____
           (__)    )\\
              ||--|| *
"""

banner4 = """

 ▄▄▄       █    ██ ▄▄▄█████▓ ▒█████   ███▄ ▄███▓ █    ██ ▒██   ██▒
▒████▄     ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒▓██▒▀█▀ ██▒ ██  ▓██▒▒▒ █ █ ▒░
▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒▓██    ▓██░▓██  ▒██░░░  █   ░
░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░▒██    ▒██ ▓▓█  ░██░ ░ █ █ ▒ 
 ▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░ ████▓▒░▒██▒   ░██▒▒▒█████▓ ▒██▒ ▒██▒
 ▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓▒ ▒ ▒ ▒▒ ░ ░▓ ░
  ▒   ▒▒ ░░░▒░ ░ ░     ░      ░ ▒ ▒░ ░  ░      ░░░▒░ ░ ░ ░░   ░▒ ░
  ░   ▒    ░░░ ░ ░   ░      ░ ░ ░ ▒  ░      ░    ░░░ ░ ░  ░    ░  
      ░  ░   ░                  ░ ░         ░      ░      ░    ░                                                                    
"""

banner5 = """
  ,---.            ,--.         ,--.   ,--.                   
 /  O  \ ,--.,--.,-'  '-. ,---. |   `.'   |,--.,--.,--.  ,--. 
|  .-.  ||  ||  |'-.  .-'| .-. ||  |'.'|  ||  ||  | \  `'  /  
|  | |  |'  ''  '  |  |  ' '-' '|  |   |  |'  ''  ' /  /.  \  
`--' `--' `----'   `--'   `---' `--'   `--' `----' '--'  '--' 
"""

banner6 = """

 ▄▄▄· ▄• ▄▌▄▄▄▄▄      • ▌ ▄ ·. ▄• ▄▌▐▄• ▄ 
▐█ ▀█ █▪██▌•██  ▪     ·██ ▐███▪█▪██▌ █▌█▌▪
▄█▀▀█ █▌▐█▌ ▐█.▪ ▄█▀▄ ▐█ ▌▐▌▐█·█▌▐█▌ ·██· 
▐█ ▪▐▌▐█▄█▌ ▐█▌·▐█▌.▐▌██ ██▌▐█▌▐█▄█▌▪▐█·█▌
 ▀  ▀  ▀▀▀  ▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀ ▀▀▀ •▀▀ ▀▀
"""

banner7 ="""
     ,           ,                                                                                              
    /             \                                                                                                
   ((__---,,,---__))                                                                                               
      (_) O O (_)_________                                                                                            
         \ _ /            |\                                                                                              
          o_o \  AutoMux  | \                                                                                             
               \   _____  |  *     
                |||   WW|||        
                |||     |||                     
"""

banner8 = '''                                                
  +-------------------------------------------------------+
  |  AutoMux by Bcap03                                    |                                                                                        
  +---------------------------+---------------------------+                                                                                        
  |      __________________   |                           |                                                                                        
  |  ==c(______(o(______(_()  | |""""""""""""|======[***  |                                                                                        
  |             )=\           | |  install   \            |                                                                                        
  |            // \\\          | |_____________\_______    |                                                                                        
  |           //   \\\         | |==[AutoMux >]========\   |                                                                                        
  |          //     \\\        | |______________________\  |                                                                                        
  |         // Tools \\\       | \(@)(@)(@)(@)(@)(@)(@)/   |                                                                                        
  |        //         \\\      |  *********************    |                                                                                        
  +---------------------------+---------------------------+                                                                                        
  |      o O o                |        \\'\/\/\/'/         |                                                                                        
  |              o O          |         )======(          |                                                                                        
  |                 o         |       .' TROJAN '.        |                                                                                        
  | |^^^^^^^^^^^^^^|l___      |      /    _||__   \       |                                                                                        
  | |    Repair      |""\___, |     /    (_||_     \      |                                                                                        
  | |________________|__|)__| |    |     __||_)     |     |                                                                                        
  | |(@)(@)"""**|(@)(@)**|(@) |    "       ||       "     |                                                                                        
  |  = = = = = = = = = = = =  |     '--------------'      |                                                                                        
  +---------------------------+---------------------------+                                                                                        
'''
banner9 = '''
                                                  
IIIIII \033[31m  dTb.dTb \033[34m       _.---._
  II   \033[31m 4'  v  'B \033[34m  .'"".'/|\`.""'.
  II   \033[31m 6.     .P \033[34m :  .' / | \ `.  :
  II   \033[31m 'T;. .;P' \033[34m '.'  /  |  \  `.'
  II   \033[31m  'T; ;P'  \033[34m  `. /   |   \ .'
IIIIII \033[31m   'YvP'   \033[34m    `-.__|__.-'

I love shells --egypt
'''

banner10 = """                                                
 ______________________________________________________________________________
|                                                                              |
|                          3Kom SuperHack II Logon                             |
|______________________________________________________________________________|
|                                                                              |
|                                                                              |
|                                                                              |
|                 User Name:          [   security    ]                        |
|                                                                              |
|                 Password:           [               ]                        |
|                                                                              |
|                                                                              |
|                                                                              |
|                                   [ OK ]                                     |
|______________________________________________________________________________|
|                                                                              |
|                                                       https://bcap03.top     |
|______________________________________________________________________________|

"""

banner_info ="""
+ -- --=[ By Bcap03        Version:v2.5.6           ]
+ -- --=[ Blog:https://bcap03.top                   ]
+ -- --=[ Root permission required with \033[31m '*'\033[34m        ]
+ -- --=[ Type 'help' for a list of commands        ]
"""



def banner():
    x = random.randint(1,10)
    if x == 1:
        print(colored(banner1,"blue"))
        print(colored(banner_info,"blue"))
    elif x == 2:  
        print(colored(banner2,"blue"))
        print(colored(banner_info,"blue"))
    elif x == 3:
        print(colored(banner3,"blue"))
        print(colored(banner_info,"blue"))
    elif x == 4:
        print(colored(banner4,"blue"))
        print(colored(banner_info,"blue"))
    elif x == 5:
        print(colored(banner5,"blue"))
        print(colored(banner_info,"blue"))
    elif x == 6:
        print(colored(banner6,"blue"))
        print(colored(banner_info,"blue"))
    elif x == 7:
        print(colored(banner7,"blue"))
        print(colored(banner_info,"blue"))
    elif x == 8:
        print(colored(banner8,"blue"))
        print(colored(banner_info,"blue"))
    elif x == 9:
        print(colored(banner9,"blue"))
        print(colored(banner_info,"blue"))
    elif x == 10:
        print(colored(banner10,"blue"))
        print(colored(banner_info,"blue"))
    else:
        print("Failed to load")