from colorama import Fore, Back, Style
from ascii_magic import AsciiArt
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

    templocation = "./temp.txt"
    textslocation = "./txts/"

    try:
        templocation or textslocation
    except NameError:
        truesetup()
    else:
        print("-----------------------\nAll set up !!!")
        main()
def truesetup():
    if input("(c)ustom setup or (d)efault: ") == "c":
        custom_setup()
    else:
        templocation = "./temp.txt"
        textslocation = "./texts"
    if templocation == "":
        templocation = "./temp.txt"
    if textslocation == "":
        textslocation = "./txts/"

def main():
    print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}{Back.BLACK}!!!!! WELCOME !!!!!{Back.RESET}")
    print(f"{Back.RESET}What do you want to run (run setup on first time){Style.RESET_ALL}")

    run = input(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}(r)emixer, {Fore.LIGHTCYAN_EX}(w)ord thingy, {Fore.LIGHTYELLOW_EX}(s)etup: {Style.RESET_ALL}").lower()

    match run:
        case "r":
            rxm.remixer(templocation, textslocation)
            print("-----------------------\nAll remixed up !!!")
            main()

        case "w":
            wtm.wordthing(templocation, textslocation)
            print("-----------------------\nWorded !!!")
            main()

        case "s":
            setup()
            print("-----------------------\nAll set up !!!")
            main()

        case "sunny":
            my_art = AsciiArt.from_image('sunny.png')
            my_art.to_terminal()
        case "q"|"quit":
            quit()
        case "ts":
            truesetup()
            main()
        case other:
            try:
                templocation or textslocation
            except NameError:
                truesetup()
            else:
                print("-----------------------\nWelcome back !!!")
                main()




my_art = AsciiArt.from_image('welcome.png')
my_art.to_terminal(columns=80, width_ratio=2.5)
setup()
main()

