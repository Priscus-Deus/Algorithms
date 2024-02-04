"""Реализация односвязного списка на Python"""

class linked_list():
    
    def __init__(self,value=None) -> None:
        self.value = value
        self.next = None


def iterate(top):
    while top != None:
        print(top.value)
        top = top.next

def find_cell(top, value):
    while top != None:
        if top.value == value:
            return top.value
        top = top.next
    return None

def find_cell_before(top, value):
    
    if top == None:
        return None
    

    while top.next != None:

        if top.next.value == value:
            return top.value
        top = top.next
    return None
    
def add_at_beginning(top, new_cell):
    new_cell.next = top.next
    top.next = new_cell


def add_at_end(top, new_cell):

    while top.next != None:
        top = top.next

    new_cell.next = top.next
    top.next = new_cell


def insert_cell(after_me, new_cell):
    new_cell.next = after_me.next
    after_me.next = new_cell


def delete_after(after_me):

    after_me.next = after_me.next.next



limiter = linked_list()
a = linked_list(1)
limiter.next = a
b = linked_list(2)
a.next = b
c = linked_list(3)
b.next = c
d = linked_list(4)
c.next = d
e = linked_list(34)
f = linked_list(44)
g = linked_list(55)
#iterate(none)
#print(find_cell(a, 3))
#print(find_cell_before(a, 3))
#iterate(limiter)
add_at_beginning(limiter, e)
#iterate(limiter)
add_at_end(limiter, f)
#iterate(limiter)
insert_cell(d, g)
iterate(limiter)
delete_after(e)
iterate(limiter)