#!/usr/bin/python
import random
import time

compare_counter=0
swap_counter=0

#순차적으로 바로 옆에 있는 데이터와 비교하면서 위치 변경

def bubble_sort(random_list):
    for start_index in range(len(random_list)-1):
        for index in range(1,len(random_list)-start_index):
            if random_list[index-1]>random_list[index]:
                temp =random_list[index-1]
                random_list[index-1]=random_list[index]
                random_list[index]=temp

if __name__ =='__main__':
    list=[]
    input_n=input("The number of data to be arranged : ")
    for i in range(int(input_n)):
        list.append(random.randint(1,int(input_n)))

    print("<Before the arrangement>")
    print(list)

    start_time= time.time()
    bubble_sort(list)
    running_time=time.time() - start_time

    print("<After arrangement>")
    print(list)

    print("Size of data: {}".format(int(input_n)))
    print("Number of comparision: {}".format(compare_counter))
    print("Number of swap: {} ".format(swap_counter))
    print("Running time: {}".format(running_time))