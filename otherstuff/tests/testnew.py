dict = {0: 25993, 1: 1910, 2: 158, 3: 11, 4: 1, 7:2}
x = buff = w = 0
y = list(dict.keys())
y = y[-1]
while x <= y-1:
    try:
        w = dict.get(y-x+buff)
        dict[y-(x+1)] += w
    except (KeyError, TypeError):
        buff+=1
        pass
    else:
        buff = 0
    w = 0
    x+=1

print(dict)

#while x > (y*-1):
 #   dict.values()