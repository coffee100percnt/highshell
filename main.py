import os
import subprocess

VERSION = "1.0a"
cd = os.path.expanduser('~')
os.chdir(cd)
print("HISHELL", VERSION, "By coffee100percnt\n")
def visualcd(dir):
    if dir.startswith(os.path.expanduser("~")):
        idk = cd.split(os.path.expanduser("~"))
        idk2 = "~" + idk[1]
        return idk2
    else:
        return dir
def parse(inp, dir):
    if inp == None:
        print()
    elif inp[0] == "help":
        print("help\nversion\ncredits\nexit\ncd <dir>")
    elif inp[0] == "version":
        print("HISHELL", VERSION)
    elif inp[0] == "exit":
        exit()
    elif inp[0] == "credits":
        print("""       Maintainer:
            coffee100percnt (github)
        Contributors:
            HONAK0 (github)
            OctoBanon-Main (github)""")
    elif inp[0] == "cd":
        try:
            if len(inp) > 1:
                if inp[1][0:1] != "/":
                    dir += f'/{inp[1]}'
                    return(dir)
                elif inp[1][0:1] == "/":
                    dir = inp[1]
                    return(dir)
            else:
                dir = os.path.expanduser("~")
                return(dir)
        except FileNotFoundError:
            print('No such directory')
    else:
        subprocess.run(inp)

while True:
    try:
        inp = input("HS "+ visualcd(cd) +" $ ").split(" ")
        try:
            moo = parse(inp, cd)
            os.chdir(moo)
            cd = moo
        except:
            pass
    except EOFError:
        print("\nexit")
        exit()
    except KeyboardInterrupt:
        inp = None
        parse(inp, cd)
        