class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def print_ll(self):
        ll_string = ""
        node = self.head
        while node:
            ll_string += f" {str(node.data)} -> "
            node = node.next_node

        ll_string += "None"
        print(ll_string)
    
    def to_list(self):
        l = []
        if self.head is None:
            return l
        
        node = self.head
        while node:
            l.append(node.data)
            node = node.next_node
        return l
        

    def insert_at_begin(self, data):
        new_node = Node(data, self.head)
        if self.head == None:
            self.tail = new_node
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data, None)
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
    
    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.data["id"] is int(user_id):
                return node.data
            node = node.next_node
        return None

        


# Example
ll = LinkedList()
ll.insert_at_end("estas3")
ll.insert_at_begin("hola")
ll.insert_at_begin("ekiane")
ll.insert_at_begin("como")
ll.insert_at_begin("estas")
ll.insert_at_end("estas2")
ll.insert_at_end("estas3")



ll.print_ll()