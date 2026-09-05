# Simple Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Power") 

choice = input("Enter your choice (1-6): ")

if choice == "1":
    print("Result:", num1 + num2)

elif choice == "2":
    print("Result:", num1 - num2)

elif choice == "3":
    print("Result:", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero!")

elif choice == "5":
    print("Result:", num1 % num2)

elif choice == "6":
    print("Result:", num1 ** num2)

else:
    print("Invalid choice!")