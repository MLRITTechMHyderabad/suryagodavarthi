dice_1 = [1,2,3,4,5,6]
dice_2 = [1,2,3,4,5,6]
lis = []
for i in dice_1:
    for j in dice_2:
        c = i,j
        lis.append(c)
print(lis)
d = {}
for i in range(2,13):
    c = 0
    for k in lis:
        s = k[0]+k[1]
        if s == i:
            c += 1
    d[str(i)] = round(c/len(lis)*100,2)
print(d)



