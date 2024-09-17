from stack import Stack

stack1 = Stack()
stack2 = Stack()

stack1.push(1)
stack1.push(2)  # [1, 2]

print(f"Peek: {stack1.peek()} ")

stack1.push(3)
stack1.push(4)
stack1.push(5)
print(f"Pilha original {stack1.items}")

while not stack1.is_empty():
    stack2.push(stack1.pop())

print(f"Pilha invertida {stack2.items}")
