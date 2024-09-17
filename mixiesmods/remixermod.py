from colorama import Fore, Style
def remixer(templocation, textslocation):
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}★ ★ This is the remixer !!! Deleting your special characters since 1995 ★ ★{Style.RESET_ALL}")

    if input(f"Press enter to start{Fore.LIGHTRED_EX}{Style.BRIGHT} ★ remixing ★ {Style.RESET_ALL}!!! Press 0 to cancel and go back : ") == "0":
        return
    while (1):
        def askforinput(txloc):
            x = input("Write your filename please (no.txt) or use filemax with 0 !!!: ")
            if x == "0":
                x = "..filemax"
            y = f"{txloc}{x}.txt"
            z = input("and the encoding !!! Choose Latin-1 (1), UTF-8 (2), or custom (3) !!!: ")
            return y, z

        filemane, enco = askforinput(textslocation)

        match enco:
            case "1":
                enco = "latin1"
            case "2":
                enco = "utf8"
            case _:
                enco = input("Please specify: ")

        try:
            open(filemane, encoding=enco)
        except FileNotFoundError:
            print("oops wrong file name or encoding! Try again !!!")
            continue
        else:
            text = open(filemane, encoding=enco).read()
            break

    match input("please specify if you want line breaks (1), no line breaks (2), or spaces AND linebreaks (3): "):
        case "2":
            meganewtxt = ""
            for char in text.upper():
                if ('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('À' <= char <= 'ỿ'):
                    meganewtxt += char

        case "3":
            newnewtxt = ""
            for char in text.upper():
                if ('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('À' <= char <= 'ỿ') or (char == ".") or (char == "?") or (char == "!") or (char == " "):
                    newnewtxt += char

            meganewtxt = newnewtxt.replace(".", "\n").replace("?", "\n").replace("!", "\n").replace("\n\n", "\n")

        case _:
            newnewtxt = ""
            for char in text.upper():
                if ('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('À' <= char <= 'ỿ') or (char == ".") or (char == "?") or (char == "!"):
                    newnewtxt += char

            meganewtxt = newnewtxt.replace(".", "\n").replace("?", "\n").replace("!", "\n")

    f = open(templocation, "w")
    f.write(meganewtxt)
    f.close()
    
    if input("0 to print: ") == "0":
        f = open(templocation, "r")
        print(f.read())
        f.close()
    
    
    

    print("\n------------------------------------\nthank you !!!")


if __name__ == "__main__":
    def main():
        remixer("/home/mooky/PycharmProjects/megamega/temp.txt", "/home/mooky/PycharmProjects/megamega/txts/")
    main()
