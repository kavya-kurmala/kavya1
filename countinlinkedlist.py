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
def printcount(head):
    current=head
    count=0
    while current is not None:
        current=current.next
        count+=1
    print(f'count of nodes is {count}')
if __name__=="__main__":
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4) 
    printelement(head)
    printcount(head)
