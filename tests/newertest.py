uni = 40
while uni < 1000:
    x = chr(uni)
    try:
        freq.get(x)
    except:
        count = freq.get(x)
        print(f"{x}: {count}, {round((count / lengthoftxt * 100), 6)}%")
    uni += 1