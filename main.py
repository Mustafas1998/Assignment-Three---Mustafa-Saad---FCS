#Stacks and Queues -1:
# O(n) where n is the length of the string.
class Stack:
    def __init__(self):
        self.elements = []
    def append(self, data):
        self.elements.append(data)
    def empty(self):
        return len(self.elements) == 0
    def pop(self):
        return self.elements.pop()

string = Stack()
text = input("Enter a text: ")
for character in text:
    string.append(character)
text_reversed = ""
while not string.empty():
    text_reversed = text_reversed + string.pop()

if text == text_reversed:
    print("Palindrome")
else:
    print("Not Palindrome")



#Stack and Queues -2:
# O(n) where n is the length of string of formula, including the non expressions, like numbers.
from collections import deque
def balanced(formula):
    stack = deque()
    for char in formula:
        if char in ('(', '{' , '['):
            stack.append(char)
        else:
            if stack:
                if stack[0] == '(' and char == ')':
                    stack.pop()
                elif stack[0] == '{' and char == '}':
                    stack.pop()
                elif stack[0] == '[' and char == ']':
                    stack.pop()
            else:
                return False
    return not stack
String = input("Enter expression: ")
result = balanced(formula=String)
print(result)


#Carwash exercise using queues:
#O(n) where n is the number of cars in the queue.
# class Queue:
#     def __init__(self):
#         self.elements = []
#     def enqueue(self,car):
#         self.elements.append(car)
#     def dequeue(self):
#         if self.empty():
#             return None
#         return self.elements.pop(0)
#     def front(self):
#         if self.empty():
#             return None
#         return self.elements[0]
#     def empty(self):
#         return len(self.elements) == 0
#     def size(self):
#         return len(self.elements)
#
# class Car:
#     def __init__(self,brand,color,plate):
#         self.brand = brand
#         self.color = color
#         self.plate = int(plate)
#
#     def __str__(self):
#         return f"{self.color} {self.brand} car of {self.plate} plate number was washed. "
#
# def menu():
#     print("1. Add car to queue.")
#     print("2. Remove car from queue.")
#     print("3. Check for cars in the queue.")
#     print("4. Check if queue is empty or not(True for empty, False for not empty).")
#     print("5. Returns the first car in the queue before it is being washed.")
#
# def Car_washing_system():
#     System = Queue()
#     while True:
#         menu()
#         Enter = input("Enter choice: ")
#         if Enter == '1':
#             brand = input("Enter brand: ")
#             color = input("Enter color: ")
#             plate = input("Enter plate: ")
#             car = Car(brand,color,plate)
#             System.enqueue(car)
#             print("Car added to queue!")
#
#         elif Enter == "2":
#             while not System.empty():
#                 car = System.dequeue()
#                 print(car)
#             if System.empty():
#                 print("No cars in the queue!")
#         elif Enter == '3':
#             print(f"{System.size()} cars in the queue!")
#         elif Enter == '4':
#             print(System.empty())
#         elif Enter == '5':
#             print(System.front())
#         else:
#             print("Bye")
#             break
# Car_washing_system()


#MIB exercise using stacks:
#O(n), where n is the length of the text to be decoded.
# class Stack:
#         def __init__(self):
#             self.elements = []
#
#         def push(self,data):
#             self.elements.append(data)
#
#         def pop(self, index=-1):
#             return self.elements.pop(index)
# message= Stack()
# text = input("Enter a text to decode: ")
# decrypted = ""
# for characters in text:
#     if characters.isalpha() or characters.isdigit() or characters == " ":
#         message.push(characters)
#     elif characters == "*":
#         if message.elements:
#             decrypted += message.pop()
# while message.elements:
#     decrypted += message.pop()
# print(decrypted)