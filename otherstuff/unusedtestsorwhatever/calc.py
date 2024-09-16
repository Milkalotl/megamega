print("! ! C A L C U L A T O R ! !")
print("Please input 2 numbers in their respective places!!")

a =input("first number !! : ")
b = input("second number !! : ")

value = float(a) + float(b)
newval = round(value, 6)
print( str(newval) + " is your sum !!!" )