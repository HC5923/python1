i, hap = 0, 0

for i in range(1,100):
   if i % 3 == 0:
       continue

   hap += i
   print("%d %d"%(i,hap))
# print('1~100의 합계(3의 배수 제외) : %d'%hap)
# 계산식 끝
