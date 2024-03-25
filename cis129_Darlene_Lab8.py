# Lab 8 Palindrome tester
# Darlene Lopez
# 3/20/2024
# This program tests for palindrome words or phrases

def is_palindrome(s):
    # Convert the string to lowercase and remove spaces and punctuation
    s = ''.join(char.lower() for char in s if char.isalnum())

    # Initialize an empty stack
    stack = []

    # Push half of the characters onto the stack
    for char in s[:len(s) // 2]:
        stack.append(char)

    # Comparing with the remaining characters
    for char in s[len(s) // 2 + len(s) % 2:]:
        if char != stack.pop():
            return False

    return True

    # Test cases


print(is_palindrome("level"))
print(is_palindrome("civic"))
print(is_palindrome("honey"))
