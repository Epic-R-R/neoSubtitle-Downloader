from configparser import ConfigParser
from pathlib import Path

PATH = "{}/Downloads/SsubDownloader".format(str(Path.home()))


def creat():
    # Get the configparser object
    config_object = ConfigParser()

    # Assume we need 2 sections in the config file, let's call them USERINFO and SERVERCONFIG
    config_object["USERINFO"] = {
        "account": "False",
        "username": "",
        "name": "",
        "email": "",
    }
    config_object["SOFTWAREINFO"] = {
        "first": "True",
        "path": f"{PATH}",
        "version": 0.3,
        "name": "S Subtitle Downloader",
        "powered": "SSM",
        "email": "salar.z@outlook.de",
        "discription": "Ssubtitle-Downloader A Tool For Download FA Subtitle",
    }

    # Write the above sections to config.ini file
    with open(f"{PATH}/.config.ini", "w") as conf:
        config_object.write(conf)


def read(keys):
    # Read config.ini file
    config_object = ConfigParser()
    config_object.read(f"{PATH}/.config.ini")
    # Get the password
    userinfo = config_object[keys]
    return userinfo


def update(newkey, obj, key):
    # Read config.ini file
    config_object = ConfigParser()
    config_object.read(f"{PATH}/.config.ini")

    # Get the  section
    section = config_object[key]
    # Update object in section
    section[obj] = newkey
    # Write changes back to file
    with open(f"{PATH}/.config.ini", "w") as conf:
        config_object.write(conf)