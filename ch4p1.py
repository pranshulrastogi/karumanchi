# checking balancing of symbols parenthisis

# will be implementing stack using list

class Stack:
    def __init__(self):
        self.top = -1
        self.stack = []
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, item):
        self.stack.append(item)
        self.top += 1

    def pop(self):
        if self.isEmpty():
            return False
        self.top -= 1
        return self.stack[self.top+1]

def isBalanced(expression):
    stack = Stack()
    for i in range(len(expression)):
        if expression[i] == '(':
            stack.push('(')
        elif expression[i] == ')':
            if not stack.pop():
                return False
    return True if stack.isEmpty() else False


if __name__ == "__main__":
    expression = input("Enter the expression: ").strip()
    if isBalanced(expression):
        print("It is balanced")
    else:
        print("its not balanced")