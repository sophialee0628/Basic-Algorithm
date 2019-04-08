#약수 구하기
#!/bin/usr/python

def getDivisor(n):
    i=1
    l=[]
    while i<=n:
        if n%i==0:
            l.append(i)
        i +=1
    print ("The divisors of the {} are {}".format(n,l))



if __name__=='__main__':
    n=int(input("Enter the number :"))
    getDivisor(n)