from colorama import Fore, Style
def merge(txtslocation):
    print(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}THIS IS THE {Fore.LIGHTWHITE_EX}*car crash sfx* {Fore.LIGHTMAGENTA_EX} MERGE MASTER {Fore.LIGHTWHITE_EX}*elephant toot* MERGING YOUR DUMB SHIT SINCE BEFORE THOSE {Fore.LIGHTRED_EX}FUCKS{Fore.LIGHTWHITE_EX} AT REMIXER")
    print(f"{Fore.LIGHTMAGENTA_EX} NOW PLAYING: MERRRRRRRRRRRGEEEEEEEEEE MASSSSSSSSTERRRRRRRRRR {Style.RESET_ALL}")

    filedictionary = {}
    guten = input("Are you using one or more project gutenberg books? (1) yes, (0) no : ")

    
    zz = int(input("how many files do you want to join? ")) + 1
    
    data = ""
    for x in range(1, zz):
        filedictionary["file{0}".format(x)] = input("File name: ")
        if zz-x-1 != 0:
            print("only {0} left".format(zz-x-1))
    
    for elem in filedictionary:
        with open(f'{txtslocation}{filedictionary[elem]}.txt', "r") as fp:
            tempdata = ""
            tempdata += fp.read()
            substring = "***"
            xid = 0
            indx = 0
            try:
                while xid <=2:
                    if xid != 2:
                        indx = tempdata.find(substring, indx+2)
                    else:
                        endx = tempdata.find(substring, indx+2)
                    xid += 1
            except ValueError:
                print("Not found!")
            else: 
                print(indx)
                data += tempdata[indx+3:endx]
                data += "\n\n"


    f = open(f'{txtslocation}..filemax.txt', 'w')
    f.write(data)
    f.close()
    print("All done !!!")
    print(data)

if __name__ == "__main__":
    merge("./txts/")
