#You are given a circular linked list, write the code for:
#Inserting an element at the end of the list
# Video: [12:00]https://drive.google.com/open?id=1BBJlXXAPPSJlAY3TdSJRjnPIs5JPxK0o
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def ins_end_cll(head,data):
    if not head:
        new=Node(data)
        new.next=new
        return new
    temp=head
    while temp.next is not head:
        temp=temp.next
    new=Node(data)
    new.next=head
    temp.next=new
    return head
