# this is the faulty calculator made by SHEHZAD
print("Select the given operator: +,-,*,%,/,** :")
operator = input()
print("Please input the integer values:")
print("Enter the first number:")
n1 = int(input())
print("Enter the second number:")
n2 = int(input())
if operator == '*' and n1 == 45 and n2 == 3:
    print("Result = 555")
    print("Thank you! for using:\nHave a good day (._.)")
elif operator == '+' and n1 == 56 and n2 == 9:
    print("Result = 77")
    print("Thank you! for using:\nHave a good day (._.)")
elif operator == '/' and n1 == 56 and n2 == 6:
    print("Result = 4")
    print("Thank you! for using:\nHave a good day (._.)")
elif operator == '+':
    add = n1 + n2
    print("Result = ",add)
    print("Thank you! for using:\nHave a good day (._.)")
elif operator == '-':
    minus = n1 - n2
    print("Result = ",minus)
    print("Thank you! for using:\nHave a good day (._.)")
elif operator == '*':
    mult = n1 * n2
    print("Result = ",mult)
    print("Thank you! for using:\nHave a good day (._.)")
elif operator == '/':
    div = n1 / n2
    print("Result = ",div)
    print("Thank you! for using:\nHave a good day (._.)")
elif operator == '**':
    square = n1 ** n2
    print("Result = ",square)
    print("Thank you! for using:\nHave a good day (._.)")
elif operator == '%':
    modulus = n1 % n2
    print("Result = ",modulus)
    print("Thank you! for using:\nHave a good day (._.)")
else:
    print("Error:\nPlease check your inputs")
