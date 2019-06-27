##i, dan = 0, 0
i, k, guguline = 0, 0, ""
for i in range(2, 10):
    guguline = guguline + ("# %d단 #" %i)

print(guguline)
##dan = int(input("단을 입력하세요:"))

##for dan in range(2, 10, 1):
for i in range(1, 10):
    guguline=""
    for k in range(2, 10):
         guguline = guguline + str("%2dX %2d=%2d"%(k,i,k*i))
    print(guguline)
        ##print("%d x %d = %d" % (dan, i , dan * i))
