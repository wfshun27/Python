#String
a = 'Hello'
b = 'World'
print(a + " " + b, "\n")

"""
String Methods
- c.upper()
- c.lower()
- c.capitalize()
- c.replace()
- c.strip()
- c.split()
"""

a = "The GST is 7%"
b = a.replace("GST", "Good and Service Tax")
print({b}, "\n")


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
#Method 1: Format
b="budget"
print("A {} is a quantiative plan for a acquiring and using resources over a specified period".format(b))

#Method 2: String Literals
b="budget"
print(f"A {b} is a quantitative plan for acquiring and using resources over a specified period.")

#Exercise: Format String

"""
bs="balance sheet"
income="income statement"
Print the following output using string literals method
"The finance statements typically require Balance sheet and INCOME STATEMENT."
"""

bs ="balance sheet"
income = "income statement"
print(f"The finance statements typically require {bs.capitalize()} and {income.upper()} {"\n"}")