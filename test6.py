## 별 1개~5개~1개 증가,감소 출력 ##
for i in range(1, 6, 1):
    for j in range(1, i+1, 1):
        print("*",end="")
    print("")

for i in range(1, 5, 1):
    for j in range(4,i-1,-1):
        print("*",end="")
    print("")