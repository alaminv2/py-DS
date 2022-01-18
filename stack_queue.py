from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, val):
        self.stack.appendleft(val)

    def pop(self):
        self.stack.popleft()

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def top(self):
        return self.stack[0]


st = Stack()
st.push('alamnin')
st.push(2652)
st.push(315)
print(st.top())
print(st.pop())
print(st.top())
