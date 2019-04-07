#!/usr/bin/python
import random
import time

compare_counter=0
swap_counter=0

#구간별로 쪼개서 정렬한 다음 다시 구간을 합쳐서 정렬

def shell_sort(random_list):
    h=1
    while h <len(random_list):
        h=h*3+1
    h=h//3

    while h >0:
        for i in range(h):
            start_index = i+h

            while start_index <len(random_list):
                temp=random_list[start_index]
                insert_index=start_index

                while insert_index > h-1 and random_list[insert_index-h] >temp:
                    random_list[insert_index]=random_list[insert_index-h]
                    insert_index=insert_index-h

                random_list[insert_index] =temp
                start_index=start_index+h
        h=h//3 #몫을 다시 h에 저장



if __name__ =='__main__':
    list=[]
    input_n=input("The number of data to be arranged : ")
    for i in range(int(input_n)):
        list.append(random.randint(1,int(input_n)))

    print("<Before the arrangement>")
    print(list)

    start_time= time.time()
    shell_sort(list)
    running_time=time.time() - start_time

    print("<After arrangement>")
    print(list)

    print("Size of data: {}".format(int(input_n)))
    print("Running time: {}".format(running_time))