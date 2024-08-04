from colorama import Fore, Back, Style
templocation = "/home/mooky/PycharmProjects/megamega/temp.txt"
textslocation = "/home/mooky/PycharmProjects/megamega/texts/"

def remixer():
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}★ ★ This is the remixer !!! Deleting your special characters since 1995 ★ ★")
    print(Style.RESET_ALL)

    if input("Press enter to start "+ f"{Fore.LIGHTRED_EX}{Style.BRIGHT}remixing"+ Style.RESET_ALL +"!!! Press 0 to cancel and go back : ") == "0":
        main()

    fileinput = input("Write your filename please (no.txt) !!! :")
    filemane = f"{textslocation}{fileinput}.txt"

    try:
        open(filemane)
    except:
        print("oops wrong file name")
        remixer()
    else:
        enco = input("and the encoding !!! Choose Latin-1 (1), UTF-8 (2), or custom (3) !!!: ")


        if enco == "1":
            realenco = "latin1"
        elif enco == "2":
            realenco = "utf8"
        else:
            realenco = input("Please specify: ")

    text = open(filemane, encoding=realenco).read()


    question = input("please specify if you want line breaks (1), no line breaks (2), or spaces AND linebreaks (3): ")

    if question == "2":
        newtxt = text.upper()
        newnewtxt = ""
        for char in newtxt:
            if ('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('À' <= char <= 'ỿ'):
                newnewtxt += char

        meganewtxt = newnewtxt

    elif question == "3":
        newtxt = text.upper()
        newnewtxt = ""
        for char in newtxt:
            if ('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('À' <= char <= 'ỿ') or (char == ".") or (char == "?") or (char == "!") or (char == " "):
                newnewtxt += char

        meganewtxt = newnewtxt.replace(".", "\n").replace("?", "\n").replace("!", "\n")


    else:
        newtxt = text.upper()
        newnewtxt = ""
        for char in newtxt:
            if ('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('À' <= char <= 'ỿ') or (char == ".") or (char == "?") or ( char == "!"):
                newnewtxt += char

        meganewtxt = newnewtxt.replace(".", "\n").replace("?", "\n").replace("!", "\n")



    temp = open(templocation, "w", encoding="utf8").write(meganewtxt)

    if input("0 to print: ") == "0":
        print(meganewtxt)
    else:
        print("thank you !!!")

def main():
    remixer()
    print("---------------------------------------\ntests")
    main()




main()