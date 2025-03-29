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

x=input("Enter x: ")
y=input("Enter y: ")
print(x + y)
#Resolve it
print(f"{x} + {y}")

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
print(f"The finance statements typically require {bs.capitalize()} and {income.upper()}")

#String Methods
a = "The GST is 7%"
b = a.replace("GST", "Good and Service Tax")
print(b)

#Strip Whitespace
a = ' Hello'.strip()
b = 'World'
print(a+b)

#remove whiespace
name = input("Enter your name: ").strip().upper()
print(f"Hello! {name}")

#Activity: Format String
email = "finance@company.com"
b = email.replace("@company.com", "/abc.com")
print(b)