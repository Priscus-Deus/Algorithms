"""Двунаправленный связный список"""

class doubly_linked_list():
    
    def __init__(self,value=None) -> None:
        self.value = value
        self.next = None
        self.prev = None


    def insert_cell(self, after_me, new_cell):
        new_cell.next = after_me.next
        after_me.next = new_cell

        new_cell.next.prev = new_cell
        new_cell.prev = after_me
        




limiter_top = doubly_linked_list()
limiter_bottom = doubly_linked_list()
a = doubly_linked_list(1)
limiter_top.next = a
b = doubly_linked_list(2)
a.next = b
a.prev = limiter_top
c = doubly_linked_list(3)
b.next = c
b.prev = a
d = doubly_linked_list(4)
c.next = d
c.prev = b
d.next = limiter_bottom
d.prev = c
e = doubly_linked_list(34)
f = doubly_linked_list(44)
g = doubly_linked_list(55)

