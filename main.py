import os
import subprocess

version = "0.2-beta"
cd = os.path.expanduser('~')
os.chdir(cd)
print("HISHELL", version, "By coffee100percnt\n")
def visualcd(dir):
    if dir.startswith(os.path.expanduser("~")):
        idk = cd.split(os.path.expanduser("~"))
        idk2 = "~" + idk[1]
        return idk2
def parse(inp, dir):
    if inp == None:
        print()
    elif inp[0] == "help":
            print("help\nversion\ncredits\nexit\nmkdir <file>\nrmdir <file>\nmkfile <file>\nrmfile <file>\ncd <path>\nlist\nrename <file> <new name>\nstartf <file>\ndownload <http url> <file name>\ncopy <file> <new name>")
    elif inp[0] == "version":
        print("HISHELL", version)
    elif inp[0] == "exit":
        exit()
    elif inp[0] == "credits":
        print("""Maintainer:
        coffee100percnt (github)
        Contributors:
        HONAK0 (github)""")
    elif inp[0] == "cd":
        if len(inp) > 1:
            dir += f'/{inp[1]}'
            os.chdir(dir)
        else:
            dir = os.path.expanduser("~")
    else:
        subprocess.run(inp)

while True:
    try:
        inp = input("HS "+ visualcd(cd) +" $ ").split(" ")
        parse(inp, cd)
    except EOFError:
        print("\nexit")
        exit()
    except KeyboardInterrupt:
        inp = None
        parse(inp, cd)