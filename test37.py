## 함수 선언 부분 ##
def hostinfo(ip) :
    Host = []
    Host['name'] = findHost(ip)
    Host['Company'] = findHost()
    global a  # 이 함수 안에서 a는 전역 변수
    a = 10
    b = 20
    print("func1()에서 a값 %d"%a)
    print("func1()에서 a값 %d"%b)

def func2():
    print("func2()에서 a값 %d"%a)
    print("func1()에서 a값 %d"%b)

if __name__=="__main__":

## 함수 변수 선언 부분 ##
#a = 20        # 전역 변수

## 메인 코드 부분 ##
#print(a)
# func1()
# func2()
