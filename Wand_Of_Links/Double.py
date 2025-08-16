class Double():
    def __init__(self):
        self.next=None
        self.prev=None
        self.data=[]
    
def insert_fornt(data,head):
    new_node=Double()
    new_node.data=data
    if head is None:
        return new_node
    new_node.next=head
    head.prev=new_node
    return new_node

def insert_back(head,data):
    new_node=Double()
    new_node.data=data
    if head is None:
        return new_node
    curr=head
    while curr.next  is not None:
        curr=curr.next
    curr.next=new_node
    new_node.prev=curr
    return head

def length(head):
    count=0
    curr=head
    while curr is not None:
        count+=1
        curr=curr.next
    return count

def delete_node(data, head):
    if head is None:
        return None
    if head.data == data:
        if head.next is not None:
            head.next.prev = None
        return head.next
    curr = head
    while curr is not None:
        if curr.data == data:
            if curr.next is not None:
                curr.next.prev = curr.prev
            if curr.prev is not None:
                curr.prev.next = curr.next
            return head
        curr = curr.next
    return head

def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" <-> ")
        curr = curr.next
    print("None")

# usage example
head = None
head = insert_fornt(1, head)
head = insert_back(head, 2)
head = insert_back(head, 3)
print_list(head)
head = delete_node(2, head)
print_list(head)
head = delete_node(1, head)
print_list(head)
head = delete_node(3, head)
print_list(head)