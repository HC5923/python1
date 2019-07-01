ss = "파이썬최고"
print(ss[0])
print(ss[1:3])
print(ss[3:])

s1=ss.replace('파이썬','클라우드') #파이썬 없애고 클라우드 단어 넣고
print(s1) # ss 출력

ip = '192.168.0.15'
newip = ip.replace('.','')  # ip의 (.)을 없애고 출력
print(newip)