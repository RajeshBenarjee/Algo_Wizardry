class Linked_List():
    def __init__(self):
        self.next = None
        self.data = []
    
def insert_front(data,head):
    new_node = Linked_List()
    new_node.data = data
    if head is None:
        return new_node
    new_node.next = head
    return new_node

def insert_back(data, head):
    new_node = Linked_List()
    new_node.data = data
    if head is None:
        return new_node
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    return head

def length(head):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count

def delete_node(data, head):
    if head is None:
        return None
    if head.data == data:
        return head.next
    current = head
    while current.next is not None:
        if current.next.data == data:
            current.next = current.next.next
            return head
        current = current.next
    return head


def print_list(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# usage example
head = None
head = insert_front(1, head)
head = insert_back(2, head)
head = insert_back(3, head)
print_list(head)
head = delete_node(2, head)
print_list(head)
head = delete_node(1, head)
print_list(head)
head = delete_node(3, head)
print_list(head)  
head = insert_front(4, head)
print_list(head)
head = insert_back(5, head)
