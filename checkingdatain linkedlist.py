class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printkey(head,key):
    current=head
    while current is not None:
        if key==current.data:
            print("yes") 
        current=current.next
    return False
  
if __name__=="__main__":
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    printkey(head,3)
