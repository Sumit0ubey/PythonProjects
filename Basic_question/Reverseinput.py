def reverse_string(user_input):
    return user_input[::-1]

user_string = input("Enter a string: ")
reversed_string = reverse_string(user_string)
print("Reversed string:", reversed_string)
