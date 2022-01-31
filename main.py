import os
import wget
import shutil
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
    #File System
    elif inp[0] == "mkdir":
        if len(inp) > 1:
            os.mkdir(cd + inp[1])
    elif inp[0] == "rmdir":
        if len(inp) > 1:
            os.rmdir(cd + inp[1])
    elif inp[0] == "mkfile":
        if len(inp) > 1:
            fl = open(cd + inp[1], "w")
            fl.write("")
            fl.close()
    elif inp[0] == "rm":
        if len(inp) > 1:
            os.remove(cd + inp[1])
    elif inp[0] == "cd":
        if len(inp) > 1:
            cd = inp[1]
    elif inp[0] == "ls":
        if len(inp) > 1:
            for cont in os.listdir(cd + "/" + inp[1]):
                if cont.startswith('.'):
                    pass
                else:
                    print(cont)
        else:
            for cont in os.listdir(cd + inp[1]):
                if cont.startswith('.'):
                    pass
                else:
                    print(cont)
    elif inp[0] == "rename":
        if len(inp) > 2:
                os.rename(cd + inp[1], cd + inp[2])
    elif inp[0] == "download":
        if len(inp) > 2:
            wget.download(inp[1], cd + inp[2])
            print()
    elif inp[0] == "copy":
        if len(inp) > 2:
            shutil.copyfile(cd + inp[1], cd + inp[2])
    elif inp[0] == "tty":
        print(os.ctermid())
    else:
        cmd = "/bin/" + inp[0]
        process = subprocess.call(cmd)