from colorama import Fore, Back, Style
from ascii_magic import AsciiArt
import time
import collections
from mixiesmods import wordthingmod as wtm, remixermod as rxm


deflist = []

with open("defaults.txt", encoding="utf8") as file:
    while line := file.readline():
        deflist.append(line)



defaulttemp = deflist[0]
defaulttexts = deflist[1]


def custom_setup():

    templocation = input("set templocation directory: ")
    textslocation = input("set textslocation directory: ")

    if input("Save to file? (y) (n)") == "y":
        with open("defaults.txt", encoding="utf8") as file:
            file.write(f"{templocation}\n{textslocation}")

        main()

def setup():
    global templocation
    global textslocation

    templocation = "/home/mooky/PycharmProjects/megamega/temp.txt"
    textslocation = "/home/mooky/PycharmProjects/megamega/txts/"

    try:
        templocation or textslocation
    except NameError:
        setup()
        print("-----------------------\nAll set up !!!")
        main()
def truesetup():
    x = input("(c)ustom setup or (d)efault: ")

    if x == "c":
        custom_setup()
    else:
        templocation = "/home/mooky/PycharmProjects/megamega/temp.txt"
        textslocation = "/home/mooky/PycharmProjects/megamega/txts/"
    if templocation == "":
        templocation = "/home/mooky/PycharmProjects/megamega/temp.txt"
    if textslocation == "":
        textslocation = "/home/mooky/PycharmProjects/megamega/txts/"



def main():
    print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}{Back.BLACK}!!!!! WELCOME !!!!!{Back.RESET}")
    print(f"{Back.RESET}What do you want to run (run setup on first time){Style.RESET_ALL}")



    run = input(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}(r)emixer, {Fore.LIGHTCYAN_EX}(w)ord thingy, {Fore.LIGHTYELLOW_EX}(s)etup: {Style.RESET_ALL}").lower()

    match run:
        case "r":
            #print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}★ ★ This is the remixer !!! Deleting your special characters since 1995 ★ ★{Style.RESET_ALL}")
            #f"Press enter to start{Fore.LIGHTRED_EX}{Style.BRIGHT} ★ remixing ★ {Style.RESET_ALL}!!! Press 0 to cancel and go back : "
            rxm.remixer(templocation, textslocation)
            print("-----------------------\nAll remixed up !!!")
            main()

        case "w":
            #wrprint(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}Welcome to the word thingy !!! Please follow the instructionszzz{Style.RESET_ALL}")
            wtm.wordthing(templocation, textslocation)
            print("-----------------------\nWorded !!!")
            main()

        case "s":
            setup(1)
            print("-----------------------\nAll set up !!!")
            main()

        case "sunny":
            my_art = AsciiArt.from_image('sunny.png')
            my_art.to_terminal()
        case "q"|"quit":
            quit()
        case other:
            try:
                templocation or textslocation
            except NameError:
                setup()
                print("-----------------------\nAll set up !!!")
                main()
            else:
                print("-----------------------\nWelcome back !!!")
                main()




my_art = AsciiArt.from_image('welcome.png')
my_art.to_terminal(columns=80, width_ratio=2.5)
setup()
main()

