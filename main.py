# stack is based on 'LIFO' - Last in first out
# stack can be implemented either through array or through linked list.
# here I'm implementing the abstract data type 'stack' using array(list) data structure


class Stack:

    def __init__(self):
        self.array = []

    # defining the push function to insert items into the array

    def push(self, data):
        self.array.append(data)

    # defining pop function to remove the last item

    def pop(self):
        if len(self.array) < 1:
            return "array is empty"
        removed_item = self.array[-1]
        del self.array[-1]
        return f"removed_item is {removed_item}"

    # defining the peek function to get the last item

    def peek(self):
        return self.array[-1]


stack = Stack()

stack.push("one")
stack.push(2)
stack.push(3)
stack.push("four")
stack.push(5)
stack.push(6)
print("the last item is ", stack.peek())
print(stack.pop())
print("the last item is ", stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("the last item is ", stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())






