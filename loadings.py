from halo import Halo
from time import sleep
import sys, os
from config import creat
from helper import screencls

# from login import signIn
from pathlib import Path

PATH = "{}/Downloads/SsubDownloader".format(str(Path.home()))

#
def firstloading():
    spinner = Halo(stream=sys.stderr)
    spinner.start("Loading")
    os.mkdir(PATH)
    creat()
    sleep(2)
    spinner.stop()
    spinner.succeed("Loading Completed.")
    # welcome_page()


# create func for loading screen in sign in page
def loadingSignIn(message):
    if message == "Username or password is wrong":
        spinner = Halo(stream=sys.stderr)
        spinner.start("Loading")
        sleep(3)
        spinner.stop()
        spinner.fail("Sign in failed, Username or password is invalid.")
        sleep(3)
        screencls()
    elif message == "succeed":
        spinner = Halo(stream=sys.stderr)
        spinner.start("Loading")
        sleep(3)
        spinner.stop()
        spinner.succeed("Sign in successful.")
        sleep(1)
        screencls()


# create func for loading screen in sign up page
def loadingSignUp(message):
    if message == "Registration was successful":
        spinner = Halo(stream=sys.stderr)
        spinner.start("Loading")
        sleep(3)
        spinner.stop()
        spinner.succeed(
            "Registration was successful, Now you can sign in with your account"
        )
        sleep(2)
        os.system("clear")
    elif message == "Username early exists":
        spinner = Halo(stream=sys.stderr)
        spinner.start("Loading")
        sleep(3)
        spinner.stop()
        spinner.fail("Username Early Exists.")
        sleep(2)
        os.system("clear")
    elif message == "SQL Error":
        spinner = Halo(stream=sys.stderr)
        spinner.start("Loading")
        sleep(3)
        spinner.stop()
        spinner.fail("Create account failed, Try again later.")
        sleep(2)
        os.system("clear")


# Create loading for login as guest
def loadingGuest():
    spinner = Halo(stream=sys.stderr)
    spinner.start("Loading for Sign in as Guest")
    sleep(3)
    spinner.stop()
    spinner.succeed("Loading Completed.")


# Create loading for logout account
def loadinglogout():
    spinner = Halo(stream=sys.stderr)
    spinner.start("Loading")
    sleep(2)
    spinner.stop()
    spinner.succeed("Logout Completed.")


# Create loading for welcome
def loadingwelcome():
    spinner = Halo(stream=sys.stderr)
    spinner.start("Loading")
    sleep(3)
    spinner.stop()
    spinner.succeed("Loading Completed.")