

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
    def temp (txtval, val_mega):
        # letter values !!!
        mySet = set(txtval)
        for element in mySet:
            countOfChar = 0
            for character in txtval:
                if character == element:
                    countOfChar += 1
            print("{}: c: {} p:{}% ".format(element, countOfChar, f": {round((countOfChar / val_mega * 100), 6)}"))

   #just printing

   #uhh i dont really know i could probably fix this


   #calculates percentages of each letter  (rework)
    def percent_calc(txt):
        val_txt_mega = len(txt) - 1
        if val_txt_mega <= 0:
            val_txt_mega = 1

        print("!! characters!!!")
        mySet = set(txt)
        for element in mySet:
            countOfChar = 0
            for character in txt:
                if character == element:
                    countOfChar += 1
            listmegaval.append(element, countOfChar)

        for i in listmegaval:
            listmegapercent.append(f": {round((i / val_txt_mega * 100), 6)}")




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
        percent_calc(megatxt)
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

    temp(txtval, val_mega)

    if input("0 for intensive test: ") == "0":
        w = 0
        while w == 0:
            listem(openziesvar)
            inttest()
            megatxt.clear
            w = int(input("0 to do it again: "))
            

    else:
        print("\nThank you so much !!!")

if __name__ == "__main__":
    def main():
        wordthing("/home/mooky/PycharmProjects/megamega/temp.txt", "/home/mooky/PycharmProjects/megamega/txts/")
    main()