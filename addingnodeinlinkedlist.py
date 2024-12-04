class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def addnode(head,data):
    current=head
    current.head=head.next
    newnode=Node(data)
    current=newnode
    print(current.data)
    
    
  
if __name__=="__main__":
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    
    addnode(head,0)
