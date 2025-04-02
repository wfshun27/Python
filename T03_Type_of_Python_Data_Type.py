#Formatting Using String Literals
#Add a "f" before the string quote

#To print in a formatted way
a = 1
b = 2
print(f"{a} + {b} = {a+b} \n")

#To format the decimal places
a = 1.222
b = 2.333
print("{1:0.1f} + {0:0.1f} = {2:0.1f} \n".format(a,b,a+b))

#To arrange the location
a = 1.222
b = 2.333
print(f"{a:0.1f}+{b:0.1f}={a+b:0.1f} \n")

#Activity: Format Numbers
a = 4.444
b = 5.555
c = 6.666

print("{} + {} + {} = {}".format(a,b,c,a+b+c))
print(f"{b:0.2f} + {c:0.2f} + {a:0.1f} = {a+b+c:0.0f}")
print("{1:0.2f} + {2:0.2f} + {0:0.1f} = {3:0.0f}".format(a,b,c,a+b+c))
print("\n")

# Multiline Statements
total_marks = "biology_marks + \
physics_marks + \
maths_marks + \
chemistry_marks"

print(total_marks)

#String
a = 'Hello'
b = 'World'
print(a + " " + b)

#Input()
name=input("What's your name?")
#print(f"Hello, {name}")
print("Hello", name)
print("\n")
                  
x=input("Enter x: ")
y=input("Enter y: ")
print(x + y)
#Resolve it
print(f"{x} + {y}" "\n")

#Format String
#Method 1:Format
b="budget"
print("A {} is a quantiative plan for a acquiring and using resources over a specified period".format(b))

#Method 2: String Literals
b="budget"
print(f"A {b} is a quantitative plan for acquiring and using resources over a specified period.")

#Activity: Format String
bs ="balance sheet"
income = "income statement"
print(f"The finance statements typically require {bs.capitalize()} and {income.upper()} {"\n"}")

#String Methods
a = "The GST is 7%"
b = a.replace("GST", "Good and Service Tax")
print(b)

#Strip Whitespace
a = ' Hello'.strip()
b = 'World'
print(a + " " + b + "\n")

#remove whiespace
name = input("Enter your name: ").strip().upper()
print(f"Hello! {name}\n")

#Activity: Format String
email = "finance@company.com"
b = email.replace("@company.com", "/abc.com")
print(b)