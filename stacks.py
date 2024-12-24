#implementing stack using a python list as underlying storage

class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class ArrayStack:
    def __init__(self):
        """Create an empty stack"""
        self._data = []

    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self._data)
    
    def is_empty(self):
        """Return true if stack is empty"""
        return len(self._data) == 0
    
    def push(self, e):
        """Add e to the top of the stack"""
        self._data.append(e);

    def top(self):
        """Return(but don't remove) element at the top of the stack"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        """Remove and return the element from the top of the stack"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()