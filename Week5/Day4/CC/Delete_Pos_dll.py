# Video: [29:00] https://drive.google.com/open?id=1BBJlXXAPPSJlAY3TdSJRjnPIs5JPxK0o
def del_pos_dll(head,pos):
    temp=head
    while pos>1 :
        if temp.next:
            temp=temp.next
            pos-=1
        else:
            print('invalid input')
            return

    prev_node=temp.prev
    next_node=temp.next
    if prev_node:
        prev_node.next=next_node
    else:
        head=next_node
    if next_node:
        next_node.prev=prev_node
    return head