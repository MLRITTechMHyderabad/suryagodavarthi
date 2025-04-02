list1 = [ [1,2,3], [4,5,6],[7,8,9]]
list2 = [ [0,0,0],[0,0,0], [0,0,0]]

for i in range (len(list1)):
    for j in range (len(list1)):
        list2[j][i]=list1[i][j]
print(list2)
