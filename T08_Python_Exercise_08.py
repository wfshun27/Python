"""
Fibonacci and Golden Ratio in Nature
Fibonacci and Golden Ratio in Art and Architure
Golden Ration in Technical Analysis
"""
"""
Activity: Compute Fibonacci Seq and Golden Ratio Using While Loop
Fibonacci nymber is the sum of the previous 2 fibonacci numbers.
1,1,2,3,5,8,21,34,...

Use the while loop to 
* compute the fibonacci sequence up to 144 and 
* compute the golden ratio which is the ration of two subsequent Fibonacci numbers
"""

import os

def show_menu():
    print("\n=== Main Menu ===")
    print("a. Fibonacci Sequence Number")
    print("b. Fibonacci Sequence Number with Golden Ratio v1")
    print("c. Fibonacci Sequence Number with Golden Ratio v2")
    print("q. Quit")

def clear_screen():
    return os.system('clear')

while True:
    
    show_menu()
    selected_option = input("Please enter 'a', 'b', or 'c', or enter 'q' to quit: ")

    if selected_option == "a":
        
        clear_screen()
        print("Fibonacci Sequence Number")

        num1, num2 = 0, 1

        count = 0

        number = int(input('Enter a number: '))
        
        while count < number:
            print(num1)
            numt = num1 + num2
            num1 = num2
            num2 = numt
            count += 1   
        input('Press enter to continue')    

    elif selected_option == "b":

        clear_screen()
        print("Fibonacci Sequence Number with Golden Ratio v1")
        
        a, b = 0, 1
        count = 0
        fib = [a,b]
        theratio=[]

        number = int(input('Enter a number: '))
        
        while count < number:
             next_val = fib[-1] + fib[-2]
             fib.append(next_val)
             
             # Calculate golden ratio
             ratio = fib[-1] / fib[-2]
        
             theratio.append(round(ratio, 3))
             count += 1
               
        print(fib)
        print(theratio)
        input('Press enter to continue')    

    elif selected_option == "c":
    
        clear_screen()
        print("Fibonacci Sequence Number with Golden Ratio Simple version")

        num1=0
        num2=1
        fib=[]
        n=1

        fib.append(num1)
        fib.append(num2)

        count = int(input('Enter a number: '))

        while n <= count:
            nextNum = fib[n]+fib[n-1]
            fib.append(nextNum)
            n+=1    
        print(fib)

        n=2
        theratio=[]

        while n <= count:
            ratio= fib[n] / fib[n-1]
            theratio.append((round(ratio, 3)))
            n+=1
        print(theratio)
        input('Press enter to continue')   

    elif selected_option == "q":
        
        clear_screen()
        print("You selected option 'q'! Quitting the menu!")
        break

    else:
       
        clear_screen()
        print("You selected an invalid option.")