import os
import subprocess

version = "0.1-alpha"
cd = os.path.expanduser('~')
#url_download = "http://cdn.discordapp.com/attachments/900323860904292382/900323946702974986/main.exe"
print("HIGH SHELL", version, "By coffee100percnt\n")
def visualcd(dir):
    if dir.startswith(os.path.expanduser("~")):
        idk = cd.split(os.path.expanduser("~"))
        idk2 = "~" + idk[0]
        return idk2

while True:
    inp = input("HS "+ visualcd(cd) +" $ ").split(" ")
    if inp[0] == "help":
        print("help\nversion\ncredits\nexit\nmkdir <file>\nrmdir <file>\nmkfile <file>\nrmfile <file>\ncd <path>\nlist\nrename <file> <new name>\nstartf <file>\ndownload <http url> <file name>\ncopy <file> <new name>")
    elif inp[0] == "version":
        print("HIGH SHELL", version)
    elif inp[0] == "exit":
        exit()
    elif inp[0] == "credits":
        out = """Maintainer:
        coffee100percnt (github)
        Contributors:
        HONAK0 (github)"""
    elif inp[0] == "cd":
        if len(inp) > 1:
            cd += inp[1]
    else:
        try:
            subprocess.call(f'/bin/{inp[0]}')
        except:
            subprocess.call(inp[0])