import os
import wget
import getpass
import shutil

version = "0.1-alpha"
cd = "~"
#url_download = "http://cdn.discordapp.com/attachments/900323860904292382/900323946702974986/main.exe"
print("HIGH SHELL", version, "By 0LungSkill0\n")

while 1 == 1:
    inp = input("HS "+ cd +" $ ").split()
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
    elif inp[0] == "rmfile":
        if len(inp) > 1:
            os.remove(cd + inp[1])
    elif inp[0] == "cd":
        if len(inp) > 1:
            cd = inp[1]
    elif inp[0] == "list":
        for cont in os.listdir(cd):
            print(cont)
    elif inp[0] == "rename":
        if len(inp) > 2:
                os.rename(cd + inp[1], cd + inp[2])
    elif inp[0] == "startf":
        if len(inp) > 1:
            os.startfile(cd + inp[1])
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
        os.startfile("/bin" + inp[0])