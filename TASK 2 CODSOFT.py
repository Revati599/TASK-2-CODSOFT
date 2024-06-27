#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!Invalid input"
    return x / y

def user_input():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            break 
        else:
            print("Invalid input")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    return (choice, num1, num2)

while True:
    choice, num1, num2 = user_input()
    
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        result = divide(num1, num2)
        if isinstance(result, str):
            print(result)
        else:
            print(f"{num1} / {num2} = {result}")
    
    again = input("Do you want to perform another calculation? (yes/no): ").lower()
    if again != 'yes':
        break


# In[ ]:




