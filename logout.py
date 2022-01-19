from config import creat, update
from helper import PATH

PATH, home = PATH()


def logout():
    creat()
    update(newkey=PATH, obj="path", key="SOFTWAREINFO")
    update(newkey="False", obj="first", key="SOFTWAREINFO")