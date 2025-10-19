'''
Execute a seguinte s ́erie de opera ̧c ̃oes de deque, assumindo uma deque inicialmente vazia:
add first(4), add last(8), add last(9), add first(5), back(), delete first( ), delete last( ), add
last(7), first( ), last( ), add last(6), delete first( ), delete first( ).
'''

from Ex_01_ArrayDeque import ArrayDeque

deque = ArrayDeque()

deque.add_first(4)
deque.add_last(8)
deque.add_last(9)
deque.add_first(5)
print(deque.peek_last())  # back()
deque.remove_first() 
deque.remove_last()
deque.add_last(7)
print(deque.peek_first())  # first()
print(deque.peek_last())   # last()
deque.add_last(6)
deque.remove_first()

print(deque)