"""
Fibonacci Sequence Calculator Function

Objective:
Write a function named 'fibonacci_sequence' to generate the Fibonacci sequence up to a given number using a while loop.

Function Parameter:
1. max_value (integer): Maximum value for the Fibonacci sequence.

Instructions:
- Use a while loop to generate the Fibonacci sequence up to 'max_value'.
- Return the sequence as a list.
- Handle edge cases for 0 and negative inputs.

Example Test Cases:
1. fibonacci_sequence(10) should return the Fibonacci sequence up to 10.
2. fibonacci_sequence(1) should return the Fibonacci sequence up to 1.
3. fibonacci_sequence(0) should return a sequence with 0.
4. fibonacci_sequence(-5) should handle negative input.
"""


def fibonacci_sequence(max_value):
    # Your code goes here
    # Implement the Fibonacci sequence calculation using a while loop
    # pass  # Delete this after implementing some code inside this function

    # 处理 0 和负数输入的边缘情况
    if max_value <= 0:
        return []

    # 初始化斐波那契数列的前两个值
    fib_sequence = [0, 1]

    # 使用 while 循环生成不超过 max_value 的斐波那契数列
    while True:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        if next_value <= max_value:
            fib_sequence.append(next_value)
        else:
            break

    return fib_sequence

# Test cases
print(fibonacci_sequence(10))  # Expected output: [0, 1, 1, 2, 3, 5, 8]
print(fibonacci_sequence(1))  # Expected output: [0, 1, 1]
print(fibonacci_sequence(0))  # Expected output: [0]
print(fibonacci_sequence(-5))  # Expected: Empty list or error message
