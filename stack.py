class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def stack_pop(self):
        if self.is_empty():
            return None
        return self.__items.pop()

    def peek(self):
        if not self.__items:
            return None
        return self.__items[-1]

    def is_empty(self) -> bool:
        if not self.__items:
            return True
        return False

    def size(self) -> int:
        return len(self.__items)

    def __str__(self):
        return str(self.__items)

my_stack = Stack()

my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
print(my_stack.peek())
print(my_stack.size())
my_stack.push(6)
print(my_stack.peek())
print(my_stack.size())
print(my_stack.stack_pop())

print(my_stack)


def are_parenthesis_valid(string: str) -> bool:
    pass

input = "())" #False
input0 = "()" #True
input1 = "({({}[])[]})" #True
input2 = "({({}[])[})" #False
input3 = "(8*5{8({3+8}-[5-8])+[9*0]})" #True
input4 = "(8*5{8({3+8-[5-8])+[9*0]})" #False
input5 = "(8*5{8(3+8}-[5-8])+[9*0]})" #False