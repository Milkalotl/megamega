

def wordthing(templocation, txtslocation):
    print("Welcome to the word thingy !!! Please follow the instructionszzz")

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

    val_mega = len(txtval)
    listval = []
    listpercent = []
    listnew = []
    meganewlist = []
    listmegaval = []
    listmegapercent = []
    megatxt = []

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



    #running wordthing


    if input("Write 0 to input custom letters (up to 3): ") == "0":
        x = input("letter: ")
        y = input("letter: ")
        z = input("letter: ")
        if not ((x == "") and (y =="") and (z =="")):
            customs(x, y, z)

    else:
        print("Ok! Startinnnnnnnnng")

    charcounter(txtval, val_mega)

    if input("0 for intensive test: ") == "0":
        w = "0"
        while w == "0":
            listem(openziesvar)
            inttest()
            megatxt.clear
            w = input("0 to do it again: ")

            

    else:
        print("\nThank you so much !!!")

if __name__ == "__main__":
    def main():
        wordthing("/home/mooky/PycharmProjects/megamega/temp.txt", "/home/mooky/PycharmProjects/megamega/txts/")
    main()