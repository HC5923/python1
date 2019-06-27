# *을 5부터 1까지 출력
for i in range(1, 6, 1):
    for j in range(5, i-1, -1):
        print("*",end="")
    print("")