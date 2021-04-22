from halo import Halo
from time import sleep


def loadingwelcome():
    spinner = Halo(stream=sys.stderr)
    spinner.start("Loading")
    sleep(3)
    spinner.stop()
    spinner.succeed("Loading Completed.")