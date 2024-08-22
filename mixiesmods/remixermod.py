def remixer(templocation,textslocation):
    print("★ ★ This is the remixer !!! Deleting your special characters since 1995 ★ ★")


    if input("Press enter to start ★ remixing ★ !!! Press 0 to cancel and go back : ") == "0":
        return

    def askforinput(textslocation, ):
        x = input("Write your filename please (no.txt) !!!: ")
        y = f"{textslocation}{x}.txt"
        z = input("and the encoding !!! Choose Latin-1 (1), UTF-8 (2), or custom (3) !!!: ")
        return y,z
    filemane, enco = askforinput(textslocation)
    
    

    if enco == "1":
        enco = "latin1"
    elif enco == "2":
        enco = "utf8"
    else:
        enco = input("Please specify: ")

    try:
        open(filemane, encoding=enco)
    except:
        print("oops wrong file name or encoding! Try again !!!")
        remixer(templocation,textslocation)
    else:
        text = open(filemane, encoding=enco).read()

    question = input("please specify if you want line breaks (1), no line breaks (2), or spaces AND linebreaks (3): ")

    if question == "2":
        meganewtxt = ""
        for char in text.upper():
            if ('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('À' <= char <= 'ỿ'):
                meganewtxt += char

    elif question == "3":
        newnewtxt = ""
        for char in text.upper():
            if ('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('À' <= char <= 'ỿ') or (char == ".") or (char == "?") or (char == "!") or (char == " "):
                newnewtxt += char

        meganewtxt = newnewtxt.replace(".", "\n").replace("?", "\n").replace("!", "\n")


    else:
        newnewtxt = ""
        for char in text.upper():
            if ('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('À' <= char <= 'ỿ') or (char == ".") or (char == "?") or ( char == "!"):
                newnewtxt += char

        meganewtxt = newnewtxt.replace(".", "\n").replace("?", "\n").replace("!", "\n")



    temp = open(templocation, "w", encoding="utf8").write(meganewtxt)
    if input("0 to print: ") == "0":
        print(meganewtxt)
    print("thank you !!!")

if __name__ == "__main__":
    def main():
        remixer("/home/mooky/PycharmProjects/megamega/temp.txt", "/home/mooky/PycharmProjects/megamega/texts/")
    main()