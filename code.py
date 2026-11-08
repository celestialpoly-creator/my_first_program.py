n = input("Enter anything: ")
if n.isdigit():
    print("You entered a number.")
elif n.isalpha():
    print("You entered a string.")
elif n.isalnum():
    print("You entered an alphanumeric value.")
elif n.isnumeric():
    print("You entered a numeric value.")
elif n.isdecimal():
    print("You entered a decimal value.")
elif n.isspace():
    print("You entered a space ")    
elif n.islower():
    print("You entered a lowercase letter.")
elif n.isupper():
    print("You entered an uppercase letter.")
elif n.istitle():
    print("You entered a title case letter.")
elif n.isidentifier():
    print("You entered an identifier.")
elif n == "":
    print("You entered an empty string.")
elif n.startswith("-") and n[1:].isdigit():
    print("You entered a negative number.")        

else:
    try:
        value = float(n)
        print("You entered a floating point number.")
    except ValueError:
      print("You entered a special character.")
