class Node():
    def __init__(self,key=None) -> None:
        self.key = key
        self.head = None
        self.size = 0
        
    
    def __str__(self) -> str:
        return str(self.key)

    def next(self, x):
        self.next = x

    def prev(self,x):
        self.prev = x

    def pushFront(self,x):
        self.pushFront =    

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

print(node1.next.next.prev) 