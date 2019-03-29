#!/usr/bin/env python

def push(item):
    stack.append(item)

def pop():
    return stack.pop()

if __name__=='__main__':
    stack=[]
    push(1)
    push(2)
    push(3)
    push(4)
    print("Stack의 현재모습")
    print(stack)

    while stack:
        print("POP > {}".format(pop()))