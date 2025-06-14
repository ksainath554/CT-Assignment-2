class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def print_list(self):
        if not self.head:
            print("List is Empty.")
            return
        current = self.head
        while current: 
            print(current.data, end="->")
            current = current.next
        print("None")
        
    def delete_nth_node(self, n):
        if not self.head:
            raise Exception("Cannot delete from empty list.")
        
        if n<=0:
            raise Exception("Invalid index. Must be 1 or higher.")
        
        if n==1:
            print(f"Deleting node at position {n}: {self.head.data}")
            self.head = self.head.next
            return
        
        current = self.head
        count = 1
        while current and count <n -1:
            current = current.next
            count += 1
            
        if not current or not current.next:
            raise Exception("Index out of range.")
        
        print(f"Deleting node at position {n}: {current.next.data}")
        current.next= current.next.next
        
if __name__ == "__main__":
    ll = LinkedList()
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)
    ll.add_node(50)
    
    print("Initial list:")
    ll.print_list()
    
    try:
        ll.delete_nth_node(3)
    except Exception as e:
        print("Error:", e)
        
    print("After deleting 3rd node:")
    ll.print_list()
        
    try:
        ll.delete_nth_node(10)
    except Exception as e:
        print("Error:", e)
        
    empty_ll = LinkedList()
    try:
        empty_ll.delete_nth_node(1)
    except Exception as e:
        print("Error:", e)