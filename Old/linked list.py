class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

def create_linked_list(values):
    head = None
    current = None
    for value in values:
        new_node = Node(value)
        if head is None:
            head = new_node
            current = head
        else:
            current.next = new_node
            current = new_node
    return head

def print_linked_list(head):
    current = head
    while current is not None:
        print(f"Data: {current.data}, Next: {id(current.next) if current.next else None}")
        current = current.next

def insert(head, item):
    new_node = Node(item)
    if head is None:
        return new_node
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    return head

# Initial list
values = [27, 19, 36, 42, 16, 0, 0, 0, 0, 0, 0, 0]
myLinkedList = create_linked_list(values)

print("Linked List BEFORE adding 25:")
print_linked_list(myLinkedList)

# Trace Table for adding 25
print("\nTrace Table for Adding 25:")
print("Step | Current Node Data | Current Node Next")
step = 1
current = myLinkedList
while current.next is not None:
    print(f"{step}    | {current.data}               | {id(current.next)}")
    current = current.next
    step += 1
print(f"{step}    | {current.data}               | {id(current.next)} (last node)")

# Insert 25
myLinkedList = insert(myLinkedList, 25)

print("\nLinked List AFTER adding 25:")
print_linked_list(myLinkedList)

# Input from user and add to the list
item = int(input("\nEnter an item to add to the linked list: "))
print("\nLinked List BEFORE adding your item:")
print_linked_list(myLinkedList)
myLinkedList = insert(myLinkedList, item)
print("\nLinked List AFTER adding your item:")
print_linked_list(myLinkedList)

# Add 25 to myLinkedList
myLinkedList = insert(myLinkedList, 25)
print("\nLinked List AFTER adding another 25:")
print_linked_list(myLinkedList)

