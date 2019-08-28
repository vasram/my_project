class Node:
    def __init__(self,data):
        self.data= data;
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def Traversal(self):
        temp = self.head
        if not temp:
            print("Empty linkedList")
        while temp:
            print(temp.data)
            temp=temp.next
    def Push(self,new_data):
        new_node= Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def Append(self, new_data):

        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)

        # 4. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next

        # 6. Change the next of last node
        last.next = new_node
    def insert(self,new_data,prev_node):
        new_node = Node(new_data)
        new_node.next , prev_node.next=prev_node.next,new_node
    def insertAfterkey(self,new_data,key) :
        new_node = Node(new_data)
        temp = self.head
        while temp:
            if temp.data==key:
                new_node.next,temp.next =temp.next,new_node
                return
            else:
                temp=temp.next
        print(" {} not present in list ".format(key))
    def search(self,value):
       temp = self.head
       while temp:
           if value == temp.data:
               print(" {}  present in list ".format(value))
               return
           temp=temp.next
       print(" {} not present in list ".format(value))
    def deleteNode(self,key):
        temp = self.head
        if (temp is not None):
            if(temp.data==key):
                self.head=temp.next
        while (temp is not None):
            if temp.data==key:
                break
            prev = temp
            temp = temp.next
        if(temp==None):
            return
        prev.next=temp.next
    def deleteByPostion(self,postion):
        temp = self.head
        if(temp is not None):
            if (postion==0):
                self.head=temp.next
                temp=None;
                return
        for i in range(postion-1):
            temp=temp.next
            if temp is None:
                return
        if (temp is None):
           return
        if(temp.next is None):
            return
        nexTonext=temp.next.next
        temp.next=None
        temp.next=nexTonext


if __name__=='__main__':
    llist = LinkedList()
    #llist.head=Node(1)
    # second = Node(2)
    # third = Node(3)
    # llist.head.next=second
    # second.next=third
    # for i in range(1,10):
    #     llist.Push(i)
    llist.Traversal()
    for i in range(1,10):
        llist.Append(i)
    llist.insert(8,llist.head.next)
    llist.search(111)
    llist.insertAfterkey(2222,7)
    llist.deleteNode(8)
    llist.deleteByPostion(0)
    llist.Traversal()

