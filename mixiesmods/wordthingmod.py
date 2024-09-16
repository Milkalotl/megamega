from colorama import Fore, Style
from matplotlib import pyplot as plt

def wordthing(templocation, txtslocation):
    print(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}Welcome to the word thingy !!! Please follow the instructionszzz{Style.RESET_ALL}")

    # declaring variables and opening temp
    def openzies(x:str):
        global txtval
        with open(x, encoding="utf8") as f:
            txtval = f.read()

    if input("Press enter to start wording !!! Press 0 to cancel and go back : ") == "0":
        return
    openziesvar = input("Use temp (enter) or write your own!! (no-txt) !!! : ")+(".txt")

    if openziesvar == ".txt":
        openzies(templocation)
        openziesvar = templocation
    else:
        try:
            openzies(f"{txtslocation}{openziesvar}")
        except FileNotFoundError:
            print("No file found !!! Try again !!!")
            wordthing(templocation, txtslocation)
        else:
            print(f"{txtslocation}{openziesvar}")
            openzies(f"{txtslocation}{openziesvar}")
            openziesvar = f"{txtslocation}{openziesvar}"

    val_mega = len(txtval)
    listmegaval = []
    listmegapercent = []
    megatxt = []
    listnew = []

    #custom letters
    def customs (x ="", y ="", z =""):
        print("---------------------------------------------")
        print(f"number of characters:{str(val_mega)}")
        if x != "":
            print(f"{x.upper()}:{txtval.count(x.upper())}")
            print(f"Percent:{str(round(((int(txtval.count(x.upper())) / val_mega * 100)), 6))} %")
        if y != "":
            print(f"{y.upper()}:{txtval.count(y.upper())}")
            print(f"Percent:{str(round(((int(txtval.count(y.upper())) / val_mega * 100)), 6))} %")
        if z != "":
            print(f"{z.upper()}:{txtval.count(z.upper())}")
            print(f"Percent:{str(round(((int(txtval.count(z.upper())) / val_mega * 100)), 6))} %")

    #creates listnew (which is a list with every sentence as an element

   #appends each line to a list as a separate element.
    def listem(x:str):
        listnew.clear()
        with open(x) as file:
            while line := file.readline():
                listnew.append(line)

  #counts each individual letter
    def charcounter (txt, lengthoftxt):
        # letter values !!!
        print("Characters !!!\n")

        freq = {}

        for ele in txt:
            if ele in freq:
                freq[ele] += 1
            else:
                freq[ele] = 1

        uni = 65
        while uni < 592:
            """
            if uni == 73:
                uni += 11
            """
            x = chr(uni)
            try:
                count = freq.get(x)
                count / lengthoftxt
            except TypeError:
                uni += 1
            else:
                count = freq.get(x)
                print(f"{x}: {count}, {round((count / lengthoftxt * 100), 6)}%")
                uni += 1

        print("\n")
    #indepth analysis
    def inttest():
        o = int(input(f"please select index of list (1-{len(listnew)}): ")) - 1
        
        try:
            listnew[o]
        except IndexError:
            print("not in there, try again !")
            inttest()

        megatxt = str(listnew[o])
        print(megatxt)
        val_txt_mega = len(megatxt) - 1
        if val_txt_mega <= 0:
            val_txt_mega = 1
        charcounter(megatxt, val_txt_mega)
        print("---------------------------------------------")

        print(listmegaval)

        for number, letter in enumerate(listmegapercent):
            print(number + 1, letter)
        listmegaval.clear()
        listmegapercent.clear()

    def experi(x:str,charac):
        listexperi = []
        listem(x)

        l = len(listnew)
        freqexperi = {}
        y = 0
        if str(listnew).count(charac) != 0:
            while y < l:
                listexperi.append(listnew[y].count(charac))
                y += 1
            for ele in listexperi:
                if ele in freqexperi:
                    freqexperi[ele] += 1
                else:
                    freqexperi[ele] = 1
            w = sorted(freqexperi.items())
            sorted_dict = {}
            for key, value in w:
                sorted_dict[key] = value
            
            # prints out the letter, and then the dictionary !!!
            print(f"{charac}: {sorted_dict}\n")
            return sorted_dict, charac


    def initexperimental():

        uni = 65
        inp = input("1 for individual, 0 for big one !! : ")
        rtf = open("./results.txt","w")
        rtf.write("")
        rtf.close()
        rtf = open("./results.txt", "a")
        colortable = ["lightcoral", "sienna", "darkorange", "darkgoldenrod", "gold", "yellowgreen", "greenyellow", "turquoise", "darkslategray", "deepskyblue", "steelblue", "mediumblue", "mediumslateblue", "darkorchid", "plum", "fuchsia", "mediumvioletred", "crimson", "orange", "red", "dimgray", "lightgray", "chocolate", "indigo", "black", "peru"]
        while uni <= 90: #this is only for english
            try:
                sorted_dict,charac = experi(openziesvar, chr(uni))
            except TypeError as e:
                print(e)
            else:    
                rtf.write(f"{charac}: {sorted_dict}\n")
                k = uni-65
                plt.axis([0, 40, 0, 30000])
                plt.plot(range(len(sorted_dict)), list(sorted_dict.values()), label = charac, color = colortable[k], marker = "*")
                if inp == "1":
                    plt.title(f"Frequency of {charac} !!")
                    plt.grid(True)
                    plt.show()
            uni += 1
        rtf.close()
        leg = plt.legend(loc='upper center')
        plt.ylabel("frequency per sentence in text")
        plt.xlabel("number of times in a sentence")
        plt.grid(True)
        plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40])
        plt.show()
        print("\n------------------------------------\nthank you !!!")
        quit()

    # running wordthing
    def run():
        if input("Please select your mode: 0 for standard, 1 for experimental: ") == "1":
           initexperimental()

        else:
            if input("Write 0 to input custom letters (up to 3): ") == "0":
                x = input("letter: ")
                y = input("letter: ")
                z = input("letter: ")
                if not ((x == "") and (y =="") and (z =="")):
                    customs(x, y, z)

            else:
                print("Ok! Startinnnnnnnnng")

            charcounter(txtval, val_mega)
            www = input("0 for intensive test: \n1 for experimental test: ")
            if www == "0":
                w = "0"
                while w == "0":
                    listem(openziesvar)
                    inttest()
                    # megatxt.clear
                    w = input("0 to do it again: ")
            elif www == "1":
                initexperimental()

            print("\nThank you so much !!!")
            quit()

    def quit():
        if input(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}(q)uit ? {Fore.LIGHTWHITE_EX}or {Fore.LIGHTCYAN_EX}{Style.BRIGHT}(r)un?{Style.RESET_ALL} ") == "r":
            run()





    run()

if __name__ == "__main__":
    def main():
        wordthing("/home/mooky/PycharmProjects/megamega/temp.txt", "/home/mooky/PycharmProjects/megamega/txts/")
    main()