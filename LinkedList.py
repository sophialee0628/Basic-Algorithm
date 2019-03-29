#!/usr/bin python

class Node :
    def __init__(self,data,next=None):
        self.data=data #데이터 저장
        self.next=next #링크저장

def init_list():
    global node_A
    node_A=Node("A")
    node_B=Node("B")
    node_C=Node("D")
    node_D=Node("E")
    node_A.next=node_B
    node_B.next=node_C
    node_C.next=node_D

def delete_node(del_data):
    global node_A
    pre_node =node_A
    next_node=pre_node.next

    if pre_node.data==del_data:
        node_A=next_node
        del pre_node
        return
    while next_node:
        if next_node.data==del_data:
            pre_node.next=next_node.next
            del next_node
            break
        pre_node=next_node
        next_node=next_node.next

def insert_node(data):
    global node_A
    new_node=Node(data)
    node_P=node_A
    node_T=node_A
    while node_T.data <=data:
        node_P=node_T
        node_T=node_T.next
    new_node.next=node_T
    node_P.next=new_node


def print_list():
    global node_A
    node=node_A
    while node:
        print(node.data)
        node=node.next
    print

if __name__=='__main__':
    print("After initializing the Linked List")
    init_list()
    print_list()
    print("After inserting node C")
    insert_node("C")
    print_list()
    print("Deleting the node D")
    delete_node("D")
    print_list()