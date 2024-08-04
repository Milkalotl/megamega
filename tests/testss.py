print ("trying to fix shit -_-")

from colorama import Fore,Back,Style

#global variables

def wordthing():
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT +"Welcome to the word thingy !!! Please follow the instructionszzz")
    print(Style.RESET_ALL)

    # declaring variables and opening temp
    def openzies(x:str):
        global texval
        with open(x, encoding="utf8") as f:
            texval = f.read()

    val_mega = len(texval)
    listval = []
    listpercent = []
    listnew = []
    meganewlist = []
    listmegaval = []
    listmegapercent = []

    def customs (x,y,z):

        texcus1 = str(x.upper())
        texcus2 = str(y.upper())
        texcus3 = str(z.upper())

        val_cus1 = texval.count(texcus1)
        val_cus2 = texval.count(texcus2)
        val_cus3 = texval.count(texcus3)

        val_final1 = (int(val_cus1) / val_mega * 100)
        val_final2 = (int(val_cus2) / val_mega * 100)
        val_final3 = (int(val_cus3) / val_mega * 100)

        print("---------------------------------------------")

        print("number of characters: " + str(val_mega))
        print(texcus1 + ": " + str(val_cus1))
        print("Percent: " + str(round((val_final1), 6)) + "%")
        print(texcus2 + ": " + str(val_cus2))
        print("Percent: " + str(round((val_final2), 6)) + "%")
        print(texcus3 + ": " + str(val_cus3))
        print("Percent: " + str(round((val_final3), 6)) + "%")

    #creates listnew (which is a list with every sentence as an element
    def listem():
        with open("../temp.txt") as file:
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
            listpercent.append(str(listval.index(i)) + ": " + str(round((i / val_mega * 100), 6)))
    def printw():
        print("---------------------------------------------")

        print(listval)

        for elem in listpercent:
            print(elem + "%")
    def megalist(x):
        global megatxt
        megatxt = listnew.pop(x)

    def percent_calc(txt):

        val_text_mega = len(txt) - 1
        print(str(val_text_mega) + "!!! characters!!!")

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
            listmegapercent.append(str(listmegaval.index(i)) + ": " + str(round((i / val_text_mega * 100), 6)))

    def inttest():
        listem()
        print(listnew)




        o = int(input(f"please select index of list (1-{len(listnew)}): ")) - 1
        megalist(o)
        print(megatxt)
        percent_calc(megatxt)
        print("---------------------------------------------")

        print(listmegaval)

        for elem in listmegapercent:
            print(elem + "%")

        if input("type 0 to do again") == "0":
            inttest()
        else:
            print("")
            print("Thank you so much !!!")
            main()


    #running wordthing
    if input("Press enter to start wording !!! Press 0 to cancel and go back : ") == "0":

        main()

    openziesvar = input("Use (T)emp or write your own!!")
    if openziesvar.upper() == "T":
        openzies("temp.txt")
    else:
        openzies(openziesvar)


    if input("Write 0 to input custom letters (up to 3): ") == "0":
        x = input("letter: ")
        y = input("letter: ")
        z = input("letter: ")
        customs(x,y,z)
    else:
        print("Ok! Startinnnnnnnnng")

    temp(texval, val_mega)

    printw()

    if input("0 for intensive test: ") == "0":

        inttest()
    else:
        print("")
        print("Thank you so much !!!")
        main()


def main():
        wordthing()
        print("-----------------------\nWelcome back !!!")
        main()
main()