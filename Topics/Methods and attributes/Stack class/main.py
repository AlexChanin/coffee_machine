class Stack:
    def __init__(self):
        self.stack = []
        self.last_item = None

    def is_empty(self):
        return not self.stack

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            self.last_item = self.stack[-1]
            self.stack = self.stack[:-1]
            return self.last_item
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None
