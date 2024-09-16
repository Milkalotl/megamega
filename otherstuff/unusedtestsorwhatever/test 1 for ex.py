def main():
    print ( "it's a wonderful day !!! Please input your desired measurement to convert !!! (only length ples)")

    lenval = float(input("length: "))
    typeval = input("Do you mean (M)eters or (F)eet heheheehehehe?? ").upper()

    if typeval == "M":
        print (round(lenval * 3.281,4))
    elif typeval == "F":
        print (round(lenval * 0.3048,4))
    elif typeval != "M" or "F":
        print ( "oopsies  !!! do it right next timeszz !!")

if __name__=="__main__":
    main()