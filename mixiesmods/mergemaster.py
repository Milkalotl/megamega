from colorama import Fore, Style
def merge(txtslocation):
    print(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}THIS IS THE {Fore.LIGHTWHITE_EX}*car crash sfx* {Fore.LIGHTMAGENTA_EX} MERGE MASTER {Fore.LIGHTWHITE_EX}*elephant toot* MERGING YOUR DUMB SHIT SINCE BEFORE THOSE {Fore.LIGHTRED_EX}FUCKS{Fore.LIGHTWHITE_EX} AT REMIXER")
    print(f"{Fore.LIGHTMAGENTA_EX} NOW PLAYING: MERRRRRRRRRRRGEEEEEEEEEE MASSSSSSSSTERRRRRRRRRR {Style.RESET_ALL}")
    if input("You are going to rewrite filemax !!! if you arent sure and want to (q)uit, do so now: ") == "q":
        return
    
    filedictionary = {}
    
    guten = input("Are you using one or more project gutenberg books? (1) yes, (0) no : ")
    zz = x =  1
    data = ""
    print("You can print your list by writing *p !!")
    print("MERGE TIME")

    while x <= zz:
        fn = input(f"File({x}) name: ")
        if fn != "":
            if fn == "*p":
                print(f"your files:")
                for elem in filedictionary.values():
                    print(f"|| {elem} ", end="")
                    
                print("||")
                zz-=1
                x-=1

            else:
                filedictionary[f"file{x}"] = fn
            zz += 1
                
        x +=1
    
    print("\nAny names you wanna edit (enter to skip)? : \n")
    editf = "x"
    while (editf != ""):
        x = 1
        for elem in filedictionary.values():
            print(f"|| {x}: {elem} ", end="")
            x +=1              
        print("||")
        editf = input("\nEnter number (or enter to skip): ")
        if editf != "":
            filedictionary[f"file{int(editf)}"] = input("new name: ")
        


    for elem in filedictionary:
        with open(f'{txtslocation}{filedictionary[elem]}.txt', "r") as fp:
            tempdata = ""
            tempdata += fp.read()
            substring = "***"
            xid = 0 
            indx = 0
            
            if (guten == "1") and (tempdata.find(substring)!= -1):
                while xid <=2:
                    if xid != 2:
                        indx = tempdata.find(substring, indx+2)
                    else:
                        endx = tempdata.find(substring, indx+2)
                    xid += 1
                data += f"{tempdata[indx+3:endx]}\n\n"
            else:
                data += f"{tempdata}\n\n"


    f = open(f'{txtslocation}..filemax.txt', 'w')
    f.write(data)
    f.close()
    print("All done !!!")

if __name__ == "__main__":
    merge("./txts/")
