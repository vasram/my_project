#program for loop dectect in Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinckedList:
    def __init__(self,):
        self.head=None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def traversal(self):
        temp=self.head
        temp1 = temp
        while temp:
            print(temp.data)
            temp1=temp
            temp=temp.next

        temp1.next = self.head

    def detectLoop(self):
        slow_p = self.head
        fast_p = self.head
        while (slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                print("Found Loop")
                return




    def CreateLoop(self, n):

        # LoopNode is the connecting node to
        # the last node of linked list
        LoopNode = self.head
        for _ in range(1, n):
            LoopNode = LoopNode.next

        # end is the last node of the Linked List
        end = self.head
        while (end.next):
            end = end.next

        # Creating the loop
        end.next = LoopNode
l1=LinckedList()
for i in range(1,10):
    l1.push(i)

l1.push(7)
l1.traversal()

l1.detectLoop()
l1.CreateLoop(11)
l1.detectLoop()