import platform
import os
from config import read
from pathlib import Path


# create func for remove space from string
def remove(string):
    return string.strip()


# create func for clear screen
def screencls():
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("clear")
    if platform.system() == "Windows":
        os.system("cls")


# create func for check exist folder
def exist(directory):
    check = os.path.isdir(directory)
    if check:
        return True
    else:
        return False


# create func for get user name
def get_name():
    if read("USERINFO")["account"] == "False":
        return "Guest"
    else:
        return read("USERINFO")["name"].upper()


# download path
def PATH():

    return "{}/Downloads/SsubDownloader".format(str(Path.home())), str(Path.home())
