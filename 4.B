class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
front=None
rear=None
def enqueue(value):
    global front, rear
    newNode = Node(value)
    if rear is None:    
        front = newNode
        rear = newNode
    else:
        rear.next = newNode
        rear = newNode
    print(value, "inserted successfully")
def dequeue():
    global front,rear
    if front is None:
        print("Queue is Empty")
    else:
        temp=front
        print(temp.data,"deleted from the queue")
        front=front.next
        if front is None:
            rear=None
def display():
    if front is None:
        print("Queue is Empty!!!")
    else:
        temp=front
        print("Queue Elements:")
        while temp is not None:
            print(temp.data,end="-->")
            temp=temp.next
        print("NULL")
while True:
    print("/n QUEUE USING LINKED LIST")
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        value=input("Enter car Number:")
        enqueue(value)
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        print("program Ended")
        break
    else:
        print("Invalid choice")
