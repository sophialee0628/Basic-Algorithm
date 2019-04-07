#!/usr/bin/python

import random

# 가장 작은 것 선택해서 정렬
def selected_sort(random_list):
    for sel in range (len(random_list)-1):
        min =random_list[sel] #최소값이라 가정
        minindex =sel
        #find min value
        for step in range(sel+1,len(random_list)):
            if min > random_list[step]:
                min =random_list[step]
                minindex=step
        #swap: 두개의 값을 서로 바꾸는 것
        random_list[minindex] =random_list[sel]
        random_list[sel] =min

if __name__ =='__main__':
    list=[]
    for i in range(10):
        list.append(random.randint(1,10))
    print("<Before Sort>")
    print(list)
    selected_sort(list) # new sorting
    print("<After sort>")
    print(list)
