from colorama import Fore, Back, Style
from ascii_magic import AsciiArt
from mixiesmods import wordthingmod as wtm, remixermod as rxm, mergemaster as mmg
from matplotlib import pyplot as plt
import matplotlib as mpl

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
    templocation = "./temp.txt"
    textslocation = "./txts"
    if templocation == "":
        templocation = "./temp.txt"
    if textslocation == "":
        textslocation = "./txts/"

def main():
    print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}{Back.BLACK}!!!!! WELCOME !!!!!{Back.RESET}")
    print(f"{Back.RESET}What do you want to run (run setup on first time){Style.RESET_ALL}")

    run = input(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}(r)emixer, {Fore.LIGHTMAGENTA_EX}(m)ergemaster, {Fore.LIGHTCYAN_EX}(w)ord thingy, {Fore.LIGHTYELLOW_EX}(s)etup: {Style.RESET_ALL}").lower()

    match run:
        case "m":
            mmg.merge(textslocation)
            print("-----------------------\nMMMMMERGED!!!!!!!!!!!!!!")
            main()


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
            my_art = AsciiArt.from_image('images/sunny.png')
            my_art.to_terminal()
        case "q"|"quit":
            quit()
        case "ts":
            truesetup()
            main()
        case "mpl":
            plottest()
        
        case other:
            try:
                templocation or textslocation
            except NameError:
                truesetup()
            else:
                print("-----------------------\nWelcome back !!!")
                main()


def plottest():
    mpl.__file__

my_art = AsciiArt.from_image('images/welcome.png')
my_art.to_terminal(columns=80, width_ratio=2.5)
setup()
main()

