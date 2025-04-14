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
   print("Fibonacci sequence upto",nfb1,":")
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
    print("a. Option A")
    print("b. Option B")
    print("c. Option C")
    print("q. Quit")

num1, num2 = 0, 1
count = 0

while True:
    show_menu()
    selected_option = input("Please enter 'a', 'b', or 'c', or enter 'q' to quit: ")

    if selected_option == "a":
        print("You selected option 'a'!")
        number = int(input('Enter a number: '))
        while count < number:
            print(num1)
            numt = num1 + num2
            num1 = num2
            print(num1)
            num2 = numt
            count += 1   
        
    elif selected_option == "b":
        print("You selected option 'b'!")
        a, b = 0, 1
        count = 0
        list_a=[]
        list_b=[]
        number = int(input('Enter a number: '))
        while count < number:
            list_a.append(a)
            a, b = b, a + b
            count += 1
        print(list_a)

    elif selected_option == "c":
        print("You selected option 'c'!")
        a, b = 0, 1
        count = 0
        fib = [a, b]
        theratio = []

        number = int(input('Enter how many golden ratios to compute: '))

# We need (number + 2) Fibonacci numbers to compute `number` golden ratios
        while count < number:
                next_val = fib[-1] + fib[-2]
                fib.append(next_val)

                # Calculate golden ratio
                ratio = fib[-1] / fib[-2]
                theratio.append(round(ratio, 3))

                count += 1

                print("\nFibonacci sequence:", fib)
                print("Golden ratio approximations:")
                for i, r in enumerate(theratio, start=2):  # start at 2nd ratio (F2/F1)
                    print(f"Term {i + 1}: {r}")

        
    elif selected_option == "q":
        print("You selected option 'q'! Quitting the menu!")
        break
    else:
        print("You selected an invalid option.")


