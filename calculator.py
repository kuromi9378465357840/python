import operator
operations= {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}
while True:
    num1= float(input("Enter a number: "))
    num2= float(input("Enter another number: "))
    choice= input("Enter an operation (+,-,*/): ")
    if choice in operations:
        result= operations[choice](num1, num2)
        print(f"Result: {result}")
    else:
        print("Invalid operation")
    repeat = input("Do you want to perform another calculation? (yes/no):")
    if repeat.lower() == "no":
        break

print("Thank you for using the calculator!")
