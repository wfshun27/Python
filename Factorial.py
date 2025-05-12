""""
import os

def clear_screen():
    return os.system('clear')

def factorial(num):
    if type(num) != int:
        return None

    if num < 0:
        return None

    return num * factorial(num - 1) if num > 0 else 1
"""

#    fact = 1
#    count = 1
#    while count <= num:
#        fact = fact * count
#        count += 1
#    return fact  # Moved outside the loop

#clear_screen()
""""
while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter a valid integer.")

print(f"The factorial of {num} is {factorial(num)}")
"""
#        fib.append(num1)
#        num1, num2 = num2, num1 + num2
#        print(fib)                             
#        input('Press enter to continue')
#    elif selected_option == "q":
#        clear_screen()
#        print("Goodbye!")
#        break
#    else:
#        clear_screen()
#        print("Invalid option. Please try again.")
# Test cases


#print(factorial(5))  # Output: 120
#print(factorial(0))  # Output: 1
#print(factorial("SPAM SPAM"))  # Output: None
import os

def clear_screen():
    return os.system('clear')  # 'cls' for Windows, use 'clear' for Unix/Linux

def factorial(num):
    #if type(num) != int:
    #    return None
    #if num < 0:
    #    return None
    return num * factorial(num - 1) if num > 0 else 1

while True:
    clear_screen()
    try:
        num_input = input("Enter a number (or type 'q' to quit): ")
        if num_input.lower() == 'q':
            break
        num = int(num_input)
        print(f"The factorial of {num} is {factorial(num)}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        input("Press Enter to try again...")
        continue

    again = input("\nDo you want to calculate another? (y/n): ").lower()
    if again != 'y':
        break
print("Goodbye!")

# Test cases   
# print(factorial(5))  # Output: 120
# print(factorial(0))  # Output: 1  
# print(factorial("SPAM SPAM"))  # Output: None
# print(factorial(-5))  # Output: None
# print(factorial(1.5))  # Output: None
# print(factorial(10))  # Output: 3628800
# print(factorial(100))  # Output: 93326215558789062164000000000000000000000000000000
# print(factorial(5.0))  # Output: None
# print(factorial(0.0))  # Output: None

