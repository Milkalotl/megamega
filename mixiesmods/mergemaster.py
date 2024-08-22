from colorama import Fore, Style
def merge(txtslocation):
    print(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}THIS IS THE {Fore.LIGHTWHITE_EX}*car crash sfx* {Fore.LIGHTMAGENTA_EX} MERGE MASTER {Fore.LIGHTWHITE_EX}*elephant toot* MERGING YOUR DUMB SHIT SINCE BEFORE THOSE {Fore.LIGHTRED_EX}FUCKS{Fore.LIGHTWHITE_EX} AT REMIXER")
    print(f"{Fore.LIGHTMAGENTA_EX} NOW PLAYING: MERRRRRRRRRRRGEEEEEEEEEE MASSSSSSSSTERRRRRRRRRR {Style.RESET_ALL}")

    filedictionary = {}
    zz = int(input("how many files do you want to join? ")) + 1
    for x in range(1, zz):
        filedictionary["file{0}".format(x)] = input("File name: ")
        if zz-x-1 != 0:
            print("only {0} left".format(zz-x-1))
    data = ""
    for elem in filedictionary:
        with open(f'{txtslocation}{filedictionary[elem]}.txt') as fp:
            data += fp.read()
            data += "\n\n"


    open(f'{txtslocation}filemax.txt', 'w').write(data)
    print("All done !!!")

if __name__ == "__main__":
    merge("/home/mooky/PycharmProjects/megamega/txts/")
