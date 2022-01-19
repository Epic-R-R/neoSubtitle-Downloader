import datetime
import os
import os.path
import platform
import sys
from time import sleep
import webbrowser
from config import creat, read, update
from helper import PATH
from urllib.parse import urlparse
from loadings import (
    firstloading,
    loadingSignIn,
    loadingSignUp,
    loadingGuest,
    loadingwelcome,
    loadinglogout,
)
from Validators import EmptyValidator, EmailValidator, ValidatePassword
import requests
from login import signIn
from logout import logout
from register import signUp
import wget
from pyfiglet import Figlet
from PyInquirer import prompt
from styles import bcolors, style
from helper import exist, screencls, get_name, remove

# get platform name
PLATFORM = platform.system()

# Download Path
PATH, home = PATH()

# url for search and download subtitles
base_url = "https://worldsubtitle.info/page/"


# create func for download subtitle
def download(link, serieName, directory):
    name = serieName
    name.append("Back To Home Menu")
    choice = [
        {
            "type": "list",
            "name": "choice",
            "message": "Choose Your Subtitle/s:",
            "choices": name,
        }
    ]
    answer = prompt(choice, style=style)
    if answer["choice"] == "Back To Home Menu":
        screencls()
        main()
    else:
        index = name.index(answer["choice"])
        linkdownload = link[index]
        hund = linkdownload
        a = urlparse(hund)
        filename = os.path.basename(a.path)
        destination = os.path.join(directory, name[index])
        if ".rar" in filename:
            wget.download(linkdownload, out=f"{destination}_SSD.rar")
        if ".zip" in filename:
            wget.download(linkdownload, out=f"{destination}_SSD.zip")
        print(
            f"""
        {bcolors.GREEN}Subtitle Downloaded.{bcolors.ENDC}
        """
        )
        sleep(2)
        screencls()
        main()


def newDownload(link, movieName, directory):
    name = movieName
    name.append("Back To Home Menu")
    choice = [
        {
            "type": "list",
            "name": "choice",
            "message": "Choose Your Subtitle/s:",
            "choices": name,
        }
    ]
    answer = prompt(choice, style=style)
    if answer["choice"] == "Back To Home Menu":
        screencls()
        main()
    else:
        index = name.index(answer["choice"])
        linkdownload = link[index]
        hund = linkdownload
        a = urlparse(hund)
        filename = os.path.basename(a.path)
        destination = os.path.join(directory, name[index])
        if ".rar" in filename:
            wget.download(linkdownload, out=f"{destination}_SSD.rar")
        if ".zip" in filename:
            wget.download(linkdownload, out=f"{destination}_SSD.zip")
        print(
            f"""
        {bcolors.GREEN}Subtitle Downloaded.{bcolors.ENDC}
        """
        )
        sleep(2)
        screencls()


def welcome_page():
    os.system("clear")
    ssd = Figlet(font="slant")
    print(f"{bcolors.HEADER}{ssd.renderText('SSD')}")
    print(f"{bcolors.OKGREEN}Welcome To Ssubtitle Downloader")
    info = [
        {
            "type": "list",
            "name": "info",
            "message": "Choose:",
            "choices": [
                "Sign in",
                "Sign up",
                "Sign in as Guest",
                "Exit",
            ],
        }
    ]
    ans = prompt(info, style=style)
    if ans["info"] == "Sign in":
        if signIn() == "Username or password is wrong":
            welcome_page()
        else:
            main()
    elif ans["info"] == "Sign up":
        if signUp() == "Registration was successful":
            if signIn() == "Username or password is wrong":
                welcome_page()
            else:
                main()
        elif signUp() == "Username early exists" or signUp() == "SQL Error":
            welcome_page()
    elif ans["info"] == "Sign in as Guest":
        loadingGuest()
        main()
    elif ans["info"] == "Exit":
        confirm = [
            {
                "type": "confirm",
                "message": "Do you want to exit?",
                "name": "exit",
                "default": False,
            },
        ]
        ans = prompt(confirm, style=style)
        if ans["exit"]:
            sys.exit(0)
        else:
            welcome_page()


# create main func
def main():
    if read("SOFTWARE")["first"] == "True":
        update(newkey=PATH, obj="path", key="SOFTWARE")
        update(newkey="False", obj="first", key="SOFTWARE")
    ssd = Figlet(font="slant")
    while True:
        os.system("clear")
        print(
            f"{bcolors.HEADER}{ssd.renderText('SSD')}{bcolors.WARNING}Welcome {get_name()}{bcolors.OKBLUE}"
        )
        info = []
        if get_name() == "Guest":
            info = [
                {
                    "type": "list",
                    "name": "info",
                    "message": "Choose:",
                    "choices": [
                        "Search For Subtitle",
                        "Account",
                        "About",
                        "Donate",
                        "Exit",
                    ],
                }
            ]
        else:
            info = [
                {
                    "type": "list",
                    "name": "info",
                    "message": "Choose:",
                    "choices": [
                        "Search For Subtitle",
                        "Show Your Downloads",
                        "Settings",
                        "Account",
                        "Check For Update",
                        "About",
                        "Donate",
                        "Exit",
                    ],
                }
            ]
        ans = prompt(info, style=style)

        if ans["info"] == "Search For Subtitle":
            if get_name() == "Guest":
                name = [
                    {
                        "type": "list",
                        "name": "search",
                        "message": "Choose: ",
                        "choices": [
                            "Search For Movie",
                            "Back To Home Menu",
                        ],
                    },
                ]
            else:
                name = [
                    {
                        "type": "list",
                        "name": "search",
                        "message": "Choose: ",
                        "choices": [
                            "Search For Movie",
                            "Search For Serie",
                            "Back To Home Menu",
                        ],
                    },
                ]
            answer = prompt(name, style=style)
            if answer["search"] == "Search For Movie":
                name = [
                    {
                        "type": "input",
                        "name": "name",
                        "message": "Enter Name Of Movie:",
                        "validate": EmptyValidator,
                    },
                ]
                ans = prompt(name, style=style)
                req = requests.get(
                    "http://api.ssubdownloader.ir/search.php?movie={}".format(
                        ans["name"]
                    )
                ).json()
                if len(req["info"]) == 0:
                    print(
                        f"""
                    {bcolors.WARNING}0 Result For This Search
                    """
                    )
                    sleep(3)
                    screencls()
                elif len(req["info"]) > 0:
                    movieName = []
                    for i in range(len(res["info"])):
                        movieName.append(res["info"][i]["movieName"])
                    movieName.append("Back To Home Menu")
                    movies = [
                        {
                            "type": "list",
                            "name": "names",
                            "message": "Choose: ",
                            "choices": movieName,
                        },
                    ]
                    answer = prompt(movies, style=style)
                    if answer["names"] == "Back To Home Menu":
                        screencls()
                    else:
                        index = res["info"][0]["movieName"]
                        req = requests.get(
                            "http://api.ssubdownloader.ir/search.php?movieName={}".format(
                                index
                            )
                        ).json()
                        movieLink = []
                        movieName = []
                        for i in range(len(req["info"])):
                            movieLink.append(req["info"][i]["movieLink"])
                            movieName.append(req["info"][i]["movieName"])
                        if len(movieLink) == 0:
                            print(
                                f"""
                            {bcolors.WARNING}Sorry Can't Download This Subtitle.{bcolors.ENDC}
                            """
                            )
                        else:
                            newDownload(
                                link=movieLink, movieName=movieName, directory=PATH
                            )
            elif answer["search"] == "Search For Serie":
                name = [
                    {
                        "type": "input",
                        "name": "name",
                        "message": "Enter Name Of Movie:",
                        "validate": EmptyValidator,
                    },
                ]
                ans = prompt(name, style=style)
                req = requests.get(
                    "http://api.ssubdownloader.ir/search.php?serie={}".format(
                        ans["name"]
                    )
                ).json()
                if len(req["info"]) == 0:
                    print(
                        f"""
                    {bcolors.WARNING}0 Result For This Search
                    """
                    )
                    sleep(3)
                    screencls()
                elif len(req["info"]) > 0:
                    serieName = []
                    for i in range(len(res["info"])):
                        serieName.append(res["info"][i]["serieName"])
                    serieName.append("Back To Home Menu")
                    series = [
                        {
                            "type": "list",
                            "name": "names",
                            "message": "Choose: ",
                            "choices": serieName,
                        },
                    ]
                    answer = prompt(series, style=style)
                    if answer["names"] == "Back To Home Menu":
                        screencls()
                    else:
                        index = res["info"][0]["serieName"]
                        req = requests.get(
                            "http://api.ssubdownloader.ir/search.php?serieName={}".format(
                                index
                            )
                        ).json()
                        serieLink = []
                        serieName = []
                        for i in range(len(req["info"])):
                            serieLink.append(req["info"][i]["serieLink"])
                            serieName.append(req["info"][i]["serieName"])
                        if len(serieLink) == 0:
                            print(
                                f"""
                            {bcolors.WARNING}Sorry Can't Download This Subtitle.{bcolors.ENDC}
                            """
                            )
                        else:
                            download(
                                link=serieLink, serieName=serieName, directory=PATH
                            )
            elif answer["search"] == "Back To Home Menu":
                screencls()
        elif ans["info"] == "Show Your Downloads":
            print(
                f"""
            {bcolors.WARNING}This Field is Disabled.{bcolors.ENDC}
            """
            )

        elif ans["info"] == "Settings":
            setting = [
                {
                    "type": "list",
                    "name": "setting",
                    "message": "choice Option",
                    "choices": [
                        "Change Download Directory Path",
                        "Show Settings",
                        "Back To Home Menu",
                    ],
                }
            ]
            ans = prompt(setting, style=style)
            if ans["setting"] == "Change Download Directory Path":
                while True:
                    path = []
                    if PLATFORM == "Linux":
                        path = [
                            {
                                "type": "input",
                                "name": "path",
                                "message": "Enter Path(Ex Linux: /home/Username/Downloads/SsubDownloader): ",
                                "validate": EmptyValidator,
                            }
                        ]
                    if PLATFORM == "Windows":
                        path = [
                            {
                                "type": "input",
                                "name": "path",
                                "message": "Enter Path(Ex Windows: C:/Users/Myname/Downloads/SsubDownloader): ",
                                "validate": EmptyValidator,
                            }
                        ]
                    anspath = prompt(path, style=style)
                    if home not in anspath["path"]:
                        print(
                            f"""
                        {bcolors.WARNING}Con't Change Download Directory To This Directory
                        """
                        )
                        continue
                    elif anspath["path"][-1] == "/":
                        anspath["path"] = anspath["path"][:-1]
                        if exist(anspath["path"]) == True:
                            auth = [
                                {
                                    "type": "confirm",
                                    "message": "Confirm This Path {}:".format(
                                        anspath["path"]
                                    ),
                                    "name": "continue",
                                    "default": True,
                                },
                            ]
                            auth = prompt(auth, style=style)
                            if auth["continue"]:
                                update(
                                    newkey=str(anspath), obj="path", key="SOFTWARE"
                                )
                                print(
                                    f"""
                                {bcolors.OKGREEN}Download Directory Changed Success.{bcolors.ENDC}
                                """
                                )
                                sleep(3)
                                break
                            else:
                                print(
                                    f"""
                                {bcolors.WARNING}Download Directory Not Changed.
                                """
                                )
                                sleep(3)
                                break
                        else:
                            print(
                                f"""
                                {bcolors.WARNING}Directory Not Exist.
                                """
                            )
                            auth = [
                                {
                                    "type": "confirm",
                                    "message": "Create Directory ({}): ".format(
                                        anspath["path"]
                                    ),
                                    "name": "continue",
                                    "default": True,
                                },
                            ]
                            auth = prompt(auth, style=style)
                            if auth["continue"]:
                                os.mkdir(anspath["path"])
                                update(
                                    newkey=str(anspath), obj="path", key="SOFTWARE"
                                )
                                print(
                                    f"""
                                {bcolors.OKGREEN}Download Directory Changed Success.{bcolors.ENDC}
                                """
                                )
                                sleep(3)
                                break
                            else:
                                print(
                                    f"""
                                    {bcolors.WARNING}Download Directory Not Changed.
                                    """
                                )
                                sleep(3)
                                break
                    else:
                        if exist(anspath["path"]) == True:
                            auth = [
                                {
                                    "type": "confirm",
                                    "message": "Confirm This Path ({}):".format(
                                        anspath["path"]
                                    ),
                                    "name": "continue",
                                    "default": True,
                                },
                            ]
                            auth = prompt(auth, style=style)
                            if auth["continue"]:
                                update(
                                    newkey=str(anspath), obj="path", key="SOFTWARE"
                                )
                                print(
                                    f"""
                                {bcolors.OKGREEN}Download Directory Changed Success.{bcolors.ENDC}
                                """
                                )
                                sleep(3)
                                break
                            else:
                                print(
                                    f"""
                                {bcolors.WARNING}Download Directory Not Changed.
                                """
                                )
                                sleep(3)
                                break
                        else:
                            print(
                                f"""
                                {bcolors.WARNING}Directory Not Exist.
                                """
                            )
                            auth = [
                                {
                                    "type": "confirm",
                                    "message": "Create Directory ({}): ".format(
                                        anspath["path"]
                                    ),
                                    "name": "continue",
                                    "default": True,
                                },
                            ]
                            auth = prompt(auth, style=style)
                            if auth["continue"]:
                                os.mkdir(anspath["path"])
                                update(
                                    newkey=str(anspath), obj="path", key="SOFTWARE"
                                )
                                print(
                                    f"""
                                {bcolors.OKGREEN}Download Directory Changed Success.{bcolors.ENDC}
                                """
                                )
                                sleep(3)
                                break
                            else:
                                print(
                                    f"""
                                    {bcolors.WARNING}Download Directory Not Changed.
                                    """
                                )
                                sleep(3)
                                break
            elif ans["setting"] == "Show Settings":
                print(
                    f"""
                {bcolors.OKGREEN}Directory  :  {read(keys="SOFTWARE")["path"]}{bcolors.ENDC}
                """
                )
                back = [
                    {
                        "type": "list",
                        "name": "back",
                        "message": "Back To Home Menu",
                        "choices": ["Back To Home Menu"],
                    }
                ]
                answer = prompt(back, style=style)
                if answer["back"] == "Back To Home Menu":
                    screencls()
            elif ans["setting"] == "Back To Home Menu":
                screencls()
        elif ans["info"] == "About":
            print(
                f"""
            Application : {bcolors.HEADER}{read("SOFTWARE")["Name"]}{bcolors.ENDC}
            Powered By  : {bcolors.OKGREEN}{read("SOFTWARE")["powered"]}{bcolors.ENDC}
            Email       : {bcolors.OKBLUE}{read("SOFTWARE")["Email"]}{bcolors.ENDC}
            Discription : {bcolors.WARNING}{read("SOFTWARE")["Discription"]}{bcolors.ENDC}
            Version     : {bcolors.BOLD}{read("SOFTWARE")["version"]}{bcolors.ENDC}
            """
            )
            back = [
                {
                    "type": "list",
                    "name": "back",
                    "message": "Back to menu",
                    "choices": ["Back To Home Menu"],
                }
            ]
            answer = prompt(back, style=style)
            if answer["back"] == "Back To Home Menu":
                screencls()
        elif ans["info"] == "Account":
            if read(keys="USERINFO")["account"] == "False":
                choice = [
                    {
                        "type": "list",
                        "name": "login",
                        "message": "Choose",
                        "choices": ["Sign in", "Sign up", "Back To Home Menu"],
                    }
                ]
                print(
                    f"""
                {bcolors.WARNING}You Don't Have Account
                """
                )
                ans = prompt(choice, style=style)
                if ans["login"] == "Sign in":
                    signIn()
                elif ans["login"] == "Sign up":
                    signUp()
                elif ans["login"] == "Back To Home Menu":
                    screencls()
            elif read(keys="USERINFO")["account"] == "True":
                choice = [
                    {
                        "type": "list",
                        "name": "info",
                        "message": "Choose",
                        "choices": [
                            "Details",
                            "Update Information",
                            "Logout",
                            "Back To Home Menu",
                        ],
                    }
                ]
                ans = prompt(choice, style=style)
                if ans["info"] == "Details":
                    print(
                        f"""
                    {bcolors.BLUE}Name     : {bcolors.GREEN}{read(keys="USERINFO")["name"]}
                    {bcolors.OKBLUE}Username : {bcolors.OKGREEN}{read(keys="USERINFO")["username"]}
                    {bcolors.MAGENTA}Email    : {bcolors.WARNING}{read(keys="USERINFO")["email"]}
                    """
                    )
                    back = [
                        {
                            "type": "list",
                            "name": "back",
                            "message": "Back",
                            "choices": ["Back To Home Menu"],
                        }
                    ]
                    ans = prompt(back, style=style)
                    if ans["back"] == "Back To Home Menu":
                        screencls()
                elif ans["info"] == "Update Information":
                    info = [
                        {
                            "type": "list",
                            "name": "info",
                            "message": "Choice",
                            "choices": [
                                "Change Email",
                                "Change Password",
                                "Back To Home Menu",
                            ],
                        }
                    ]
                    ans = prompt(info, style=style)
                    if ans["info"] == "Change Email":
                        infoemail = [
                            {
                                "type": "input",
                                "name": "email",
                                "message": "Enter Your Email   :",
                                "validate": EmailValidator,
                            },
                            {
                                "type": "password",
                                "name": "password",
                                "message": "Enter Your Password:",
                                "validate": EmptyValidator,
                            },
                        ]
                        ans = prompt(infoemail, style=style)
                        req = requests.get(
                            "http://api.ssubdownloader.ir/login.php?username={}&password={}".format(
                                read(keys="USERINFO")["username"], ans["password"]
                            )
                        ).json()
                        if req["message"] == "Username or password is wrong":
                            print(
                                f"""
                            {bcolors.WARNING}Wrong Password, Try Again{bcolors.ENDC}
                            """
                            )
                            sleep(3)
                            screencls()
                        elif req["message"] == "Login Success":
                            update(newkey=ans["email"], obj="email", key="USERINFO")
                            req = requests.get(
                                "http://api.ssubdownloader.ir/update.php?username={}&email={}".format(
                                    read(keys="USERINFO")["email"], ans["email"]
                                )
                            )
                            print(
                                f"""
                            {bcolors.GREEN}Email Changed successfully{bcolors.ENDC}
                            """
                            )
                            sleep(2)
                    elif ans["info"] == "Change Password":
                        infopass = [
                            {
                                "type": "password",
                                "name": "oldpassword",
                                "message": "Enter Your Password:",
                                "validate": EmptyValidator,
                            },
                        ]
                        ans = prompt(infopass, style=style)
                        req = requests.get(
                            "http://api.ssubdownloader.ir/login.php?username={}&password={}".format(
                                read(keys="USERINFO")["username"], ans["oldpassword"]
                            )
                        ).json()
                        if req["message"] == "Login Success":
                            newpass = [
                                {
                                    "type": "password",
                                    "name": "newpassword",
                                    "message": "Enter New Password :",
                                    "validate": ValidatePassword,
                                },
                            ]
                            ans = prompt(newpass, style=style)
                            req = requests.get(
                                "http://api.ssubdownloader.ir/update.php?username={}&password={}".format(
                                    read(keys="USERINFO")["username"],
                                    ans["newpassword"],
                                )
                            ).json()
                            if req["message"] == "Passowrd updated successfully":
                                print(
                                    f"""
                                {bcolors.GREEN}Password Updated Successfully.{bcolors.ENDC}
                                """
                                )
                                sleep(3)
                        elif req["message"] == "Username or password is wrong":
                            print(
                                f"""
                            {bcolors.WARNING}Password Is Invalid.{bcolors.ENDC}
                            """
                            )
                            sleep(3)
                    elif ans["info"] == "Back To Home Menu":
                        screencls()
                elif ans["info"] == "Logout":
                    logout()
                    loadinglogout()
                    welcome_page()
                elif ans["info"] == "Back To Home Menu":
                    screencls()
        elif ans["info"] == "Donate":
            choice = [
                {
                    "type": "list",
                    "name": "donate",
                    "message": "Choice Your Option:",
                    "choices": ["BTC", "Back To Home Menu"],
                }
            ]
            answer = prompt(choice, style=style)
            if answer["donate"] == "BTC":
                print(
                    f"""
                {bcolors.OKGREEN}Thanks For You Support{bcolors.ENDC}
                """
                )
                sleep(2)
                webbrowser.open(
                    "https://blockchain.com/btc/payment_request?address=1EtdgCxD6psi1JHKzFacHPXJaaTVJabxJP&amount=0.00007272&message=Donate SsubDownlaoder"
                )
            if answer["donate"] == "Back To Home Menu":
                screencls()
        elif ans["info"] == "Check For Update":
            req = requests.get(
                "https://raw.githubusercontent.com/Epic-R-R/Subtitle-Downloader/Sullivan/package.json"
            ).json()
            if float(req["versions"][-1]) == float(read("SOFTWARE")["version"]):
                print(
                    f"""
                {bcolors.GREEN}You use latest version{bcolors.ENDC}
                """
                )
                sleep(3)
                screencls()
            if float(req["versions"][-1]) > float(read("SOFTWARE")["version"]):
                print(
                    f"""
                {bcolors.WARNING}You use older version{bcolors.ENDC}
                {bcolors.FAIL}Download new version from here: https://github.com/Epic-R-R/Subtitle-Downloader{bcolors.ENDC}
                """
                )
                sleep(3)
                webbrowser.open("https://github.com/Epic-R-R/Subtitle-Downloader")
                screencls()

        elif ans["info"] == "Exit":
            confirm = [
                {
                    "type": "confirm",
                    "message": "Do you want to exit?",
                    "name": "exit",
                    "default": False,
                },
            ]
            ans = prompt(confirm, style=style)
            if ans["exit"]:
                sys.exit(0)
            else:
                main()


if __name__ == "__main__":
    check = os.path.isdir(PATH)
    if check:
        if read("USERINFO")["account"] == "False":
            welcome_page()
        else:
            loadingwelcome()
            main()
    else:
        firstloading()
        welcome_page()
