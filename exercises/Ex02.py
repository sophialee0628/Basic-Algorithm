#재귀호출을 사용하여 1부터 n까지 출력하기

def f(n):
    if n > 0:
        f(n-1)
    print(n)

if __name__=='__main__':

    n=int(input("Enter the number :"))
    f(n)