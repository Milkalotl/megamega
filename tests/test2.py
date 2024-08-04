def openzies(x: str):
    global texval
    with open(x, encoding="utf8") as f:
        texval = f.read()


openzies()