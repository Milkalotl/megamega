deflist = []

def main():
    custom_setup()

deflocation = "/home/mooky/PycharmProjects/megamega/defaults.txt"

with open(deflocation, encoding="utf8") as file:
    while line := file.readline():
        deflist.append(line)



defaulttemp = deflist[0]
defaulttexts = deflist[1]
deflocation = deflist[2]


def custom_setup():

    deflocation = input("set deflocation: ")
    templocation = input("set templocation directory: ")
    textslocation = input("set textslocation directory: ")

    if input("Save to file? (y) (n)") == "y":
        with open(deflocation, encoding="utf8") as file:
            file.write(f"{templocation}\n{textslocation}\n{deflocation}")


    print(defaulttemp,defaulttexts,deflocation,templocation,textslocation)
    main()


main()