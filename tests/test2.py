
texval = "babadoey"
val_mega = len(texval)

def customs(x, y, z):
    print("number of characters: " + str(val_mega))
    print(f"{x.upper()}:{texval.count(x.upper())}")
    print("Percent: " + str(round(((int(texval.count(x.upper() )) / val_mega * 100)), 6)) + "%")
    p
