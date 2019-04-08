# 반목문을 사용하여 0부터 n까지의 합 출력하기

def sum_0ton (n):
    i=0
    sum=0
    while (i <= n):
        sum +=i
        i += 1
    print("The total sum is {}".format(sum))

if __name__=='__main__':

    n=int(input("Input n : "))
    sum_0ton(n)
