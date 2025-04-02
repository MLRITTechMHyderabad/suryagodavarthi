import random
d1 = [1, 2, 3, 4, 5, 6]
d2 = [1, 2, 3, 4, 5, 6]
li = []
di = {}
for i in d1:
    for j in d2:
        li.append((i, j))
print(li)
d = {}
for i in range(2,13):
    c = 0
    for j in li:
        s = j[0]+j[1]
        if s == i:
            c += 1
    d[str(i)] = round(c/len(li)*100,2)
print(d)
for i in range(10):
    player1_value = random.randint(1,7)
    player2_value = random.randint(1,7)
    print("player 1 rolled:", player1_value)
    print("player 2 rolled:", player2_value)
    if player1_value > player2_value:
        print("player1  is winner")
        player1_value += 1
    elif player2_value > player1_value:
        print("player2 is winner")
        player2_value += 1
    else:
        print("draw")

