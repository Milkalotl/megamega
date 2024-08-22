import json

def charcounter(txt, lengthoftxt):
    # letter values !!!
    print("Characters !!!\n")

    mySet = set(txt)
    for element in mySet:
        countOfChar = 0
        for char in txt:
            if char == element:
                if ('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('À' <= char <= 'ỿ') or (char == ".") or (
                        char == "?") or (char == "!") or (char == " "):
                    countOfChar += 1

        print("{}: {} p: {}% ".format(element, countOfChar, f"{round((countOfChar / lengthoftxt * 100), 6)}"))
#########################################
def supercharcounter(txt, lengthoftxt):
    # letter values !!!





with open("/home/mooky/PycharmProjects/megamega/temp.txt", encoding="utf8") as f:
            txt = f.read()

lengtext = len(txt)
#charcounter(txt,lengtext)
supercharcounter(txt,lengtext)