import string
import math



def fibonacci(n: int) -> list:
    if n == 0:
        return []
    elif n == 1:
        return [0]
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]



def factorial(n: int) -> int:
    if n < 0:
        return ""
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result



def count_letters_and_punctuation(sentence: str) -> dict:
    frequency = {}
    for char in sentence:
        if char.isalpha():
            key = char.lower()
            frequency[key] = frequency.get(key, 0) + 1
        elif char in string.punctuation:
            frequency[char] = frequency.get(char, 0) + 1
    return dict(sorted(frequency.items()))



def count_perfect_squares_in_list(numbers: list) -> int:
    count = 0
    for num in numbers:
        if num >= 0:
            root = math.isqrt(num)
            if root * root == num:
                count += 1
    return count



def draw_triangle_prime(height: int) -> None:
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    total = height * (height + 1) // 2
    primes = []
    num = 2
    while len(primes) < total:
        if is_prime(num):
            primes.append(num)
        num += 1
    index = 0
    for row in range(1, height + 1):
        print(' '.join(str(primes[index + i]) for i in range(row)))
        index += row



def matrix_multiply(matrix1: list, matrix2: list) -> list:
    rows_m1 = len(matrix1)
    col_m1 = len(matrix1[0]) if matrix1 else 0
    rows_m2 = len(matrix2)
    col_m2 = len(matrix2[0]) if matrix2 else 0
    
    if col_m1 != rows_m2:
        raise ValueError("Number of columns in matrix1 must equal number of rows in matrix2.")

    result = [[0 for _ in range(col_m2)] for _ in range(rows_m1)]
    
    for i in range(rows_m1):
        for j in range(col_m2):
            for k in range(col_m1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result



def is_palindrome_iterative(word: str) -> bool:
    word = word.lower()
    word = ''.join(c for c in word if c.isalnum())
    return word == word[::-1]



# print(fibonacci(10))
# print(factorial(3))
print(count_letters_and_punctuation("Hello, world! 21"))
# print(count_perfect_squares_in_list([1, 5, 2, 7]))
# print(draw_triangle_prime(7))
# print(matrix_multiply([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]]))
# print(is_palindrome_iterative("racecar"))