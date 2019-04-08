#소수 판별하기

#!/usr/bin/python

def check_prime(n):
    i=2
    while i < n:
        if n%i==0:
            break
        i +=1
    if i==n:
        print("{} is prime number".format(n))
    else:
        print("{} is not a prime number".format(n))


if __name__=='__main__':
    check_prime(2)
    check_prime(39)
    check_prime(13)
    n=int(input("Enter the number:"))
    check_prime(n)