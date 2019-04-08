#반복문 사용하여 n까지 출력하기

def f(n):
    for x in range (1,n+1):
        print(x)

if __name__=='__main__':
    n=int(input("Enter the Number: "))
    f(n)