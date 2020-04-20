#hace current start with head
#check current's next node
#if the same remove it and reset current next tp the node next next
#if not the same move current to next
#repeat



def remove_duplicates(self):
    current = self.head
    while current.next != None:
        if current.data == current.next.data: #found a duplicate
            next_next = current.next.next
        else:
            current = current.next
