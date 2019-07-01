list1 = []
list2 = []
list3 = []

value = 3
result=''

for i in range(0, 5):
    for j in range(0, 4):
        list1.append(value)
        value +=3
        for k in range(1, 10):
            result = result + str("%2dx%d=%2d"% (value, k, value * k))
            list1.append(result)
        list2.append(list1)
        list1 = []
    list3.append(list2)
print(list3)
for i in range(0, 5):
    for j in range(0, 4):
        for k in range(1, 10):
            print("%5d" % list3[i][j][k],)
    print()