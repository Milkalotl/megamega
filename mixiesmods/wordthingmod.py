

def wordthing(templocation,textslocation):
    print("Welcome to the word thingy !!! Please follow the instructionszzz")

    # declaring variables and opening temp
    def openzies(x:str):
        global texval
        with open(x, encoding="utf8") as f:
            texval = f.read()

    if input("Press enter to start wording !!! Press 0 to cancel and go back : ") == "0":
        return

    openziesvar = input("Use temp (enter) or write your own!! (no-txt) !!! : ")

    if openziesvar.upper() == "":
        openzies(templocation)
        openziesvar = templocation
    else:
        try:
            openzies(f"{textslocation}{openziesvar}.txt")
        except:
            print("No file found !!! Try again !!!")
            wordthing(templocation,textslocation)
        else:
            openzies(f"{textslocation}{openziesvar}.txt")

    val_mega = len(texval)
    listval = []
    listpercent = []
    listnew = []
    meganewlist = []
    listmegaval = []
    listmegapercent = []

    def customs (x="",y="",z=""):
        print("---------------------------------------------")
        print(f"number of characters:{str(val_mega)}")
        if x != "":
            print(f"{x.upper()}:{texval.count(x.upper())}")
            print(f"Percent:{str(round(((int(texval.count(x.upper())) / val_mega * 100)), 6))} %")
        if y != "":
            print(f"{y.upper()}:{texval.count(y.upper())}")
            print(f"Percent:{str(round(((int(texval.count(y.upper())) / val_mega * 100)), 6))} %")
        if z != "":
            print(f"{z.upper()}:{texval.count(z.upper())}")
            print(f"Percent:{str(round(((int(texval.count(z.upper())) / val_mega * 100)), 6))} %")

    #creates listnew (which is a list with every sentence as an element
    def listem(x:str):
        with open(x) as file:
            while line := file.readline():
                listnew.append(line)
    def temp (texval, val_mega):
        # letter values !!!
        val_a = texval.count("A")
        val_b = texval.count("B")
        val_c = texval.count("C")
        val_d = texval.count("D")
        val_e = texval.count("E")
        val_f = texval.count("F")
        val_g = texval.count("G")
        val_h = texval.count("H")
        val_i = texval.count("I")
        val_j = texval.count("J")
        val_k = texval.count("K")
        val_l = texval.count("L")
        val_m = texval.count("M")
        val_n = texval.count("N")
        val_o = texval.count("O")
        val_p = texval.count("P")
        val_q = texval.count("Q")
        val_r = texval.count("R")
        val_s = texval.count("S")
        val_t = texval.count("T")
        val_u = texval.count("U")
        val_v = texval.count("V")
        val_w = texval.count("W")
        val_x = texval.count("X")
        val_y = texval.count("Y")
        val_z = texval.count("Z")

        listval.extend([val_a, val_b, val_c, val_d, val_e, val_f, val_g, val_h, val_j, val_k, val_l, val_m, val_n, val_o, val_p, val_q, val_r, val_s, val_t, val_u, val_v, val_w, val_x, val_y, val_z])

        for i in listval:
            listpercent.append(f": {round((i / val_mega * 100), 6)}")
    def printw():
        print("---------------------------------------------")

        print(listval)

        for number, letter in enumerate(listpercent):
            print(chr(number + 65), letter)
    def megalist(x):
        global megatxt
        megatxt = listnew.pop(x)
    def percent_calc(txt):

        val_text_mega = len(txt) - 1
        if val_text_mega == 0:
            val_text_mega = 1

        print("!! characters!!!")

        val_a = txt.count("A")
        val_b = txt.count("B")
        val_c = txt.count("C")
        val_d = txt.count("D")
        val_e = txt.count("E")
        val_f = txt.count("F")
        val_g = txt.count("G")
        val_h = txt.count("H")
        val_i = txt.count("I")
        val_j = txt.count("J")
        val_k = txt.count("K")
        val_l = txt.count("L")
        val_m = txt.count("M")
        val_n = txt.count("N")
        val_o = txt.count("O")
        val_p = txt.count("P")
        val_q = txt.count("Q")
        val_r = txt.count("R")
        val_s = txt.count("S")
        val_t = txt.count("T")
        val_u = txt.count("U")
        val_v = txt.count("V")
        val_w = txt.count("W")
        val_x = txt.count("X")
        val_y = txt.count("Y")
        val_z = txt.count("Z")

        listmegaval.extend([val_a, val_b, val_c, val_d, val_e, val_f, val_g, val_h, val_j, val_k, val_l, val_m, val_n, val_o, val_p, val_q, val_r, val_s, val_t, val_u, val_v, val_w, val_x, val_y, val_z])

        for i in listmegaval:
            listmegapercent.append(f": {round((i / val_text_mega * 100), 6)}")

    def inttest():

        o = int(input(f"please select index of list (1-{len(listnew)}): ")) - 1
        if 1 > o > len(listnew):
            print("oops!! too long !!!")
            inttest()

        megalist(o)
        print(megatxt)
        percent_calc(megatxt)
        print("---------------------------------------------")

        print(listmegaval)

        for number, letter in enumerate(listmegapercent):
            print(number + 1, letter)



    #running wordthing


    if input("Write 0 to input custom letters (up to 3): ") == "0":
        x = input("letter: ")
        y = input("letter: ")
        z = input("letter: ")
        if not ((x== "") and (y=="") and (z=="")):
            customs(x,y,z)

    else:
        print("Ok! Startinnnnnnnnng")

    temp(texval, val_mega)

    printw()

    if input("0 for intensive test: ") == "0":
        listem(openziesvar)
        inttest()
        if input("type 0 to do again: ") == "0":
            inttest()
        else:
            print("")
            print("Thank you so much !!!")

    else:
        print("")
        print("Thank you so much !!!")

if __name__ == "__main__":
    def main():
        wordthing("/home/mooky/PycharmProjects/megamega/temp.txt", "/home/mooky/PycharmProjects/megamega/texts/")
    main()