"""
Letter Case Counter Function

Objective:
Write a function named 'case_counter' that counts the number of uppercase and lowercase letters in a given string.

Function Parameter:
text (string): The string in which the letters need to be counted.

Instructions:
- The function should calculate and print two numbers: the count of uppercase letters and the count of lowercase letters in the string.
- If there are no letters of a particular case (uppercase or lowercase) in the string, the function should print 0 for that case.
- Non-alphabetic characters in the string should be ignored and not counted.

Example Test Cases:
1. case_counter("Hello World!") should print the counts of uppercase and lowercase letters.
2. case_counter("PYTHON") should print the counts of uppercase and lowercase letters.
3. case_counter("python") should print the counts of uppercase and lowercase letters.
4. case_counter("1234!@#$") should print 0 for both counts.
"""


def case_counter(text):
    # Your code goes here
    # Remember to count uppercase and lowercase letters and ignore non-alphabetic characters
    # pass  # Delete this after implementing some code inside this function.

    # 初始化大写和小写字母的计数
    uppercase_letters, lowercase_letters = 0, 0

    # 计算大写和小写字母的数量
    for char in text:
        if char.isupper():
            uppercase_letters += 1
        elif char.islower():
            lowercase_letters += 1

    # 打印计数结果
    print(f"Uppercase letters: {uppercase_letters}, Lowercase letters: {lowercase_letters}")


# Test cases
case_counter("Hello World!")  # Expected: Uppercase letters: 2, Lowercase letters: 8
case_counter("PYTHON")  # Expected: Uppercase letters: 6, Lowercase letters: 0
case_counter("python")  # Expected: Uppercase letters: 0, Lowercase letters: 6
case_counter("1234!@#$")  # Expected: Uppercase letters: 0, Lowercase letters: 0
