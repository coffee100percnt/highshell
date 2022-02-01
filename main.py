import os
import subprocess

version = "0.1-alpha"
cd = os.path.expanduser('~')
os.chdir(cd)
print("HISHELL", version, "By coffee100percnt\n")
def visualcd(dir):
    if dir.startswith(os.path.expanduser("~")):
        idk = cd.split(os.path.expanduser("~"))
        idk2 = "~" + idk[1]
        return idk2

while True:
    inp = input("HS "+ visualcd(cd) +" $ ").split(" ")
    if inp[0] == "help":
        print("help\nversion\ncredits\nexit\nmkdir <file>\nrmdir <file>\nmkfile <file>\nrmfile <file>\ncd <path>\nlist\nrename <file> <new name>\nstartf <file>\ndownload <http url> <file name>\ncopy <file> <new name>")
    elif inp[0] == "version":
        print("HISHELL", version)
    elif inp[0] == "exit":
        exit()
    elif inp[0] == "credits":
        out = """Maintainer:
        coffee100percnt (github)
        Contributors:
        HONAK0 (github)"""
    elif inp[0] == "cd":
        if len(inp) > 1:
            cd += f'/{inp[1]}'
            os.chdir(cd)
        else:
            cd = os.path.expanduser("~")
    else:
        subprocess.run(inp)