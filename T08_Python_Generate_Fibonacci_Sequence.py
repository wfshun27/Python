a, b = 0, 1
list_a=[]
list_b=[]

while a <= 144:
    list_a.append(a)
    a, b = b, a + b
    list_b.append(b)
print(list_a)

n1, n2 = 0, 1
count = 0

# Get the number of terms from the user
nfb1 = int(input("How many terms? "))

# check if the number of terms is valid
if nfb1 <= 0:
   print("Please enter a positive integer")

# if there is only one term, return n1

elif nfb1 == 1:
   print("Fibonacci sequence up to",nfb1,":")
   print(n1)

# generate fibonacci sequence

else:
   print("Fibonacci sequence:")
   while count < nfb1:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

num1, num2 = 0, 1
count = 0
# Print numbers until the user enters 0
number = int(input('Enter a number: '))

# iterate until the user enters 0
while count < number:
    print(num1)
    numt = num1 + num2
     # update values
    num1 = num2
    num2 = numt
    count += 1   
print('The end.')

def show_menu():
    print("\n=== Main Menu ===")
    print("a. Fibonacci Sequence Number")
    print("b. Fibonacci Sequence Number with Golden Ratio")
    print("c. Option C")
    print("q. Quit")

while True:
    show_menu()
    selected_option = input("Please enter 'a', 'b', or 'c', or enter 'q' to quit: ")

    if selected_option == "a":
        
        print("Fibonacci Sequence Number")

        num1, num2 = 0, 1
        count = 0

        number = int(input('Enter a number: '))
        while count < number:
            print(num1)
            numt = num1 + num2
            num1 = num2
            print(num1)
            num2 = numt
            count += 1   
        
    elif selected_option == "b":
        
        print("Fibonacci Sequence Number with Golden Ratio")
        
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

    elif selected_option == "c":

        print("You selected option 'c'!")

        num1=0
        num2=1
        fib=[]
        n=1

        fib.append(num1)
        fib.append(num2)

        print(fib)

        while n <=11:
            nextNum = fib[n]+fib[n-1]
            fib.append(nextNum)
            n+=1    
        print(fib)

        n=2
        theratio=[]

        while n <=11:
            ratio= fib[n] / fib[n-1]
            theratio.append((round(ratio, 3)))
            n+=1
        print(theratio)


       
    elif selected_option == "q":
        print("You selected option 'q'! Quitting the menu!")
        break

    else:
        print("You selected an invalid option.")


