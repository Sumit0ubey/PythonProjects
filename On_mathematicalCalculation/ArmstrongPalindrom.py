def is_armstrong_number(number):
    num_digits = len(str(number))
    sum_digits = sum(int(digit) ** num_digits for digit in str(number))
    return sum_digits == number

def is_palindrome(number):
    return str(number) == str(number)[::-1]


num = int(input("Enter a number: "))

if is_armstrong_number(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

if is_palindrome(num):
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")
