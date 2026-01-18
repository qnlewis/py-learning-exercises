# fun-090-consolidation



# Project Description

In this assessment, you are required to complete the Python problems below. The focus of this assessment is on:

-

## Project Structure

```
fun-090-consolidation
|_tests/
|    |_test_consolidation.py #Sample tests
|
|_consolidation.py #Your solution goes here
|
|_README.md 
```

Run all sample tests:
```bash
python3 -m unittest tests/test_consolidation.py
```

Run sample tests individually:
```bash
python3 -m unittest tests.test_consolidation.TestConsolidation.fibonacci
```

NB: You can run (copy and paste) the following commands on your terminal to run our hidden tests against your implementation:

```bash
chmod +x .lms/run_hidden.sh  # Run this only once

```
```bash
.lms/run_hidden.sh   # You can run this every time you want to test against the hidden tests
```

## `consolidation.py`

Complete the following functionalities:

### 1. `fibonacci(n:int) -> list`
Generate the Fibonacci sequence up to the n-th term.

Parameters:

- **n (int)**: The number of terms in the Fibonacci sequence to generate. Must be a non-negative integer.

Returns:

- **list**: A list containing the Fibonacci sequence up to the n-th term.

**Fibonacci Sequence Example**:

The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two. For example, the first 10 Fibonacci numbers are:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

Example output (n = 5):
```
[0, 1, 1, 2, 3]
```
---

### 2. `factorial(n:int) -> int`

Generate the factorial of a number n.

Parameters:

- **n (int)**: A positive integer. If n is negative, return an empty string.

Returns:

- **int**: Returns the factorial of n.

**Factorial Example**:

The factorial of a number n is the product of all positive integers less than or equal to n. For example:

```py
5! = 5 * 4 * 3 * 2 * 1 = 120
```
Example output (n = 5):

```py
120

```
---

### 3. `count_letters_and_punctuation(sentence: str) -> dict`

Count the frequency of letters and punctuation marks in a given sentence.

Parameters:

- **sentence (str)**: The sentence to analyse.

Returns:

- **dict**: A dictionary where each key is a character (either a letter or a punctuation mark) from the sentence, and the value is the frequency of that character. The dictionary should be sorted in alphabetical order of the characters.

Example output (sentence = "Hello, World!"):

```python
{'!': 1, ',': 1, 'd': 1, 'e': 1, 'h': 1, 'l': 3, 'o': 2, 'r': 1, 'w': 1}
```

---

### 4. `count_perfect_squares_in_list(numbers: list) -> int`

Count the number of perfect square numbers in a given list.

Parameters:

- **numbers (list)**: A list of integers.

Returns:

- **int**: The total count of perfect square numbers in the list.

**Perfect Square Example**:

A perfect square is an integer that is the square of another integer. For example:

```py
4 is a perfect square because 2*2 = 4
9 is a perfect square because 3*3 = 9
16 is a perfect square because 4*4 = 16
```

Example output (numbers = [4, 9, 16, 17]):

```python
#4, 9 and 16 are perfect squares
3 
```

---
### 5. `draw_triangle_prime(height: int) -> None`

Generate a triangle of prime numbers.

Parameters:

- **height (int)**: The height of the triangle.

Returns:

- **None**: Prints a triangle of prime numbers with the given height.


A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. This means that a prime number can only be evenly divided by 1 and the number itself, and not by any other numbers.

**For example**:

2 is a prime number because it can only be divided evenly by 1 and 2.

3 is a prime number because it can only be divided evenly by 1 and 3.

The first few prime numbers are:

`
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ...
`

Example output (height = 4):

```python
2
3 5
7 11 13
17 19 23 29
```
---
### 6. `matrix_multiply(matrix1: list, matrix2: list) -> list`

This function multiplies two matrices (matrix1 and matrix2) and returns the resulting matrix. For matrix multiplication to work:

The number of columns in matrix1 must be equal to the number of rows in matrix2.

1. To multiply the matrices, follow these steps:

Multiply the rows of matrix1 by the columns of matrix2: For each position in the result matrix, compute the sum of products between corresponding elements of the row in matrix1 and the column in matrix2.

2. Store the result: Each sum becomes an element in the resulting matrix.

### Example:

Let’s say you have the following two matrices:

Matrix 1 (2x3):

```python
[ [1, 2, 3],
  [4, 5, 6] ]
```

Matrix 2 (3x2):

```python
[ [7, 8],
  [9, 10],
  [11, 12] ]

```

To compute the result, multiply the rows of matrix1 with the columns of matrix2. For instance:

The element at position (1,1) of the result is calculated as:

`(1 * 7) + (2 * 9) + (3 * 11) = 58`

The element at position (1,2) of the result is calculated as:

`(1 * 8) + (2 * 10) + (3 * 12) = 64`

Continue this process for the rest of the positions.


**Example Input**:

```python

matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

result = matrix_multiply(matrix1, matrix2)
```
Example Output:
```python
[[58, 64],
 [139, 154]]

```

### 7. `is_palindrome_iterative(word: str) -> bool` 

This function checks if a given word is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backward as forward, ignoring spaces, punctuation, and capitalisation.

Parameters:

- **word (str)**: The word to check.

Returns:

- **bool**: True if the word is a palindrome, False otherwise.

Palindrome Example:

```python
Civic is a palindrome #True

madAm is a palindrome # True
```