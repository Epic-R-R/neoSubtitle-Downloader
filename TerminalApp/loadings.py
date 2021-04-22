from halo import Halo
from time import sleep
import sys


def loadingwelcome():
    spinner = Halo(stream=sys.stderr)
    spinner.start("Loading")
    sleep(2)
    spinner.stop()
    spinner.succeed("Loading Completed.")
