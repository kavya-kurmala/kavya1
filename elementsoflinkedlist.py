class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printelement(head):
    current=head
    while current is not None:
        print(f'{current.data}')
        current=current.next
    print()
if __name__=="__main__":
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4) 
    printelement(head)
