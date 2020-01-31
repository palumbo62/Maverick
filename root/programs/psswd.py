import sys

sys.path += "../../"

from getpass import getpass
from src.data.dataRunner import getUserData
import hashlib

userdata = getUserData()

def reset():

    usesOld = False

    if not userdata["password"] == None:
        old = getpass("Old password: ")
        usesOld = True

    new = getpass("New password: ")

    if usesOld:
        if not hashlib.sha256(old.encode()).hexdigest() == userdata["password"]:
            print("Password is incorrect.")
            exit()

    userdata["password"] = hashlib.sha256(new.encode()).hexdigest()

    userdata.close()

if __name__ == "__main__":
    reset()