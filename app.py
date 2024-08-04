print("Welcome to the word thingy !!! Please follow the instructionszzz")


#declaring variables and opening temp
texsamp = open("temp.txt", encoding="utf8").read()
texval = texsamp.upper()
val_mega = len(texval)

#all the custom shit
if input("Write 0 to input custom letters (up to 3): ") == "0":
    textemp1 = input("letter: ")
    textemp2 = input("letter: ")
    textemp3 = input("letter: ")

    texcus1 = str(textemp1.upper())
    texcus2 = str(textemp2.upper())
    texcus3 = str(textemp3.upper())

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

else:
    print("Ok! Startinnnnnnnnng")

#creating a new list for the individual values
lisy = []
newlist = []

with open("temp.txt") as file:
    while line := file.readline():
        lisy.append(line)

f = lambda x: x.replace("\n", "")
newlist = list(map(f, lisy))



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

val_val_val = [val_a, val_b, val_c, val_d, val_e, val_f, val_g, val_h, val_j, val_k, val_l, val_m, val_n, val_o, val_p, val_q, val_r, val_s, val_t, val_u, val_v, val_w, val_x, val_y, val_z]




val_val_aw = []
for i in val_val_val:
    val_val_aw.append(str(val_val_val.index(i)) + ": " + str(round((i / val_mega * 100), 6)))


#just printin
print("---------------------------------------------")

print(val_val_val)

for elem in val_val_aw:
    print(elem + "%")

print("")
print("Thank you so much !!!")

print(newlist)
