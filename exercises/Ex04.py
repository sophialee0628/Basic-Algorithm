# 숫자 뒤집기
#!/bin/usr/python

def reverseStr(num):
    return (str(num)[::-1]) #스트링으로 인식했을 때

def reverseNum(num):
    rev=0
    while (num > 0):
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    return rev

if __name__=='__main__':
    num=int(input("Enter the number : "))

    print("This is reversed number (type str): {}".format(reverseStr(num)))
    print("This is also reversed number (type int): {}".format(reverseNum(num)))


