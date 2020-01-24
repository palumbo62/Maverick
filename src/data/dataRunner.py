import shelve
import colorama
from root.programs.Installer.install import install

def getUserData():
    return shelve.open("./src/data/data", writeback = True)

def buildData():

    userdata = getUserData()

    userdata.clear()

    userdata["programs"] = []
    userdata["password"] = None

    userdata.close()

    install("apps","./root/programs/apps.py")
    install("psswd","./root/programs/psswd.py")
    install("install","./root/programs/installer.py")