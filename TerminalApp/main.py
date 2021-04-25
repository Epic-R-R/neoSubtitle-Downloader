from PyInquirer import prompt
from styles import style
from helper import screencls, whyUse
from pyfiglet import Figlet
import sys
from colorama import init, Fore
from loadings import loadingwelcome
from donate import donate

def welcome_page():
    screencls()
    ssd = Figlet(font="slant")
    print(f"{Fore.LIGHTMAGENTA_EX}{ssd.renderText('neoSubtitle DW')}")
    print(f"{Fore.BLUE}Welcome To neoSubtitle Downloader")
    info = [
        {
            "type": "list",
            "name": "info",
            "message": "Choose:",
            "choices": [
                "Sign in",
                "Sign up",
                "Explorer",
                "Why use neoSubtitle Downloader ?",
                "Donate",
                "Exit",
            ],
        }
    ]
    ans = prompt(info, style=style)
    if ans["info"] == "Sign in":
        # if signIn() == "Username or password is wrong":
        #     welcome_page()
        # else:
        #     main()
        pass
    elif ans["info"] == "Sign up":
        # if signUp() == "Registration was successful":
        #     if signIn() == "Username or password is wrong":
        #         welcome_page()
        #     else:
        #         main()
        # elif signUp() == "Username early exists" or signUp() == "SQL Error":
        #     welcome_page()
        pass
    elif ans["info"] == "Explorer":
        pass
    elif ans["info"] == "Why use neoSubtitle Downloader ?":
        whyUse()
    elif ans["info"] == "Donate":
        donate()
    elif ans["info"] == "Exit":
        confirm = [
            {
                "type": "confirm",
                "message": "Do you want to exit?",
                "name": "exit",
                "default": False,
            }
        ]
        ans = prompt(confirm, style=style)
        if ans["exit"]:
            sys.exit(0)
        else:
            welcome_page()


if __name__ == "__main__":
    init(autoreset=True)  # Colorama autoreset terminal color True
    loadingwelcome()
    welcome_page()
