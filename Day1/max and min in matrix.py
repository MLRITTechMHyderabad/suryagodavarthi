a = [[1,2,3], [5,7,8], [9,2,4]]
min_element = a[0][0]
max_element = a[0][0]
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] < min_element:
            min_element = a[i][j]
        if a[i][j] > max_element:
            max_element = a[i][j]
    print("min element", min_element)
    print("max element", max_element)
