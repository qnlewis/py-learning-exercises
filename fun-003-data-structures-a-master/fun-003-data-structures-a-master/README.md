# Project Description
In this assessment, you will be required to complete the python problems below. The assessment focuses on:

- List Manipulation
- Mathematical Operations
- Data Analysis
- Statistical Calculations
- Algorithmic Thinking
- Conditionals
- Data Structures

## Project Structure

```
fun-003-data-structures/
├── data_structures.py    # Your implementation goes here
└── tests/
    └── test_data_structures.py  # Corresponding unittests go here(optional)
```

## test_data_structures.py

For this assessment, you can follow Test-Driven Development (TDD) principles i.e is not a must to do this:

Write test cases before/alongside implementing the functionalities.

To check if your code passes your own test cases, run:

```bash
python3 -m unittest tests/test_data_structures.py
```

**NB:** You can run (copy and paste) the following commands on your terminal to run our hidden tests against your implementation

```bash
chmod +x .lms/run_hidden.sh  # Run this only once
```

```bash
.lms/run_hidden.sh   # You can run this every time you want to test against the hidden tests
```

## data_structures.py

Complete the following functions:

## 1. generate_random_list(length: int) -> list

  Generate a list of random numbers of a given length.

  **Parameters:**
  - `length` (int): The length of the list to generate. Must be a positive integer.

  **Returns:**
  - `list`: Returns a list of random numbers with the specified length.

  **Example:**
  ```python
  generate_random_list(5)  # Returns something like [42, 17, 89, 3, 56]
  ```

## 2. find_max(numbers: list) -> int/float

Find the largest (maximum) number in a list of numbers.

**Parameters:**
- `numbers` (list): A list of numbers.

**Returns:**
- `int/float`: Returns the maximum number in the list.

**Example:**
```python
find_max([1, 2, 3, 4, 5])  # Returns 5
find_max([-1, 2, -3, 4, -5, 6, -9, 10])  # Returns 10
```

## 3. find_min(numbers: list) -> int/float

Find the smallest (minimum) number in a list of numbers.

**Parameters:**
- `numbers` (list): A list of numbers.

**Returns:**
- `int/float`: Returns the minimum number in the list.

**Example:**
```python
find_min([1, 2, 3, 4, 5])  # Returns 1
find_min([-1, 2, -3, 4, -5, 6, -9, 10])  # Returns -9
```

## 4. find_average(numbers: list) -> float

Find the average of a list of numbers and return it as a float to one decimal point.

**Parameters:**
- `numbers` (list): A list of numbers.

**Returns:**
- `float`: Returns the average of the numbers in the list.

**Example:**
```python
find_average([1, 2, 3, 4, 5])  # Returns 3.0
find_average([-1, 2, -3, 4, -5, 6, -9, 10])  # Returns 0.5
```

## 5. find_even_pairs(numbers: list) -> list

Find the neighboring pairs of numbers that sum up to an even number and return a list of tuples with the pairs' index numbers.

**Parameters:**
- `numbers` (list): A list of numbers.

**Returns:**
- `list`: Returns a list of tuples containing index pairs that sum to even numbers.

**Example:**
```python
find_even_pairs([1, 3, 5])  # Returns [(0, 1)]
find_even_pairs([6, 2, 3, 5, 9, 4, 1, 11])  # Returns [(0, 1), (2, 3), (3, 4), (6, 7)]
```

## 6. find_odd_pairs(numbers: list) -> list

Find the neighboring pairs of numbers that sum up to an odd number and return a list of tuples with the pairs' index numbers.

**Parameters:**
- `numbers` (list): A list of numbers.

**Returns:**
- `list`: Returns a list of tuples containing index pairs that sum to odd numbers.

**Example:**
```python
find_odd_pairs([1, 3, 5])  # Returns [(1, 2)]
find_odd_pairs([1, 2, 3, 4, 5])  # Returns [(0, 1), (1, 2), (2, 3), (3, 4)]
```

## 7. find_number_of_even_numbers(numbers: list) -> int

Find the total number of even numbers in the list and return the count as an integer.

**Parameters:**
- `numbers` (list): A list of numbers.

**Returns:**
- `int`: Returns the count of even numbers in the list.

**Example:**
```python
find_number_of_even_numbers([1, 2, 3, 4, 5])  # Returns 2
find_number_of_even_numbers([1, 2, 3, 4, 5, 6])  # Returns 3
```

## 8. find_number_of_odd_numbers(numbers: list) -> int

Find the total number of odd numbers in the list and return the count as an integer.

**Parameters:**
- `numbers` (list): A list of numbers.

**Returns:**
- `int`: Returns the count of odd numbers in the list.

**Example:**
```python
find_number_of_odd_numbers([1, 2, 3, 4, 5])  # Returns 3
find_number_of_odd_numbers([1, 2, 3, 4, 5, 6])  # Returns 3
```

## 9. find_even_numbers(numbers: list) -> tuple

Find the even numbers in the list and return them in a tuple.

**Parameters:**
- `numbers` (list): A list of numbers.

**Returns:**
- `tuple`: Returns a tuple containing all even numbers from the list.

**Example:**
```python
find_even_numbers([1, 2, 3, 4, 5])  # Returns (2, 4)
find_even_numbers([1, 2, 3, 4, 5, 6])  # Returns (2, 4, 6)
```

## 10. find_odd_numbers(numbers: list) -> tuple

Find the odd numbers in the list and return them in a tuple.

**Parameters:**
- `numbers` (list): A list of numbers.

**Returns:**
- `tuple`: Returns a tuple containing all odd numbers from the list.

**Example:**
```python
find_odd_numbers([1, 2, 3, 4, 5])  # Returns (1, 3, 5)
find_odd_numbers([1, 2, 3, 4, 5, 6])  # Returns (1, 3, 5)
```

## 11. return_list_stats(numbers: list) -> dict

Given the list 'numbers', use the relevant functions to return a dictionary of statistics for the list. This dictionary must have the following keys:

**Parameters:**
- `numbers` (list): A list of numbers.

**Returns:**
- `dict`: Returns a dictionary with the following keys:
  - `unique_numbers`: a set containing unique numbers from the list
  - `max`: largest number in the list
  - `min`: smallest number in the list
  - `average`: average of the numbers in the list
  - `even_pairs`: a list of tuples that have neighboring pairs that sum up to an even number
  - `odd_pairs`: a list of tuples that have neighboring pairs that sum up to an odd number
  - `even_numbers`: a tuple of all the even numbers in the list
  - `odd_numbers`: a tuple of all the odd numbers in the list
  - `number_of_even_numbers`: the total number of even numbers in the list
  - `number_of_odd_numbers`: the total number of odd numbers in the list

**Example:**
```python
return_list_stats([1, 2, 3, 4, 5])
# Returns:
# {
#     "unique_numbers": {1, 2, 3, 4, 5},
#     "min": 1,
#     "max": 5,
#     "average": 3.0,
#     "even_pairs": [],
#     "odd_pairs": [(0, 1), (1, 2), (2, 3), (3, 4)],
#     "even_numbers": (2, 4),
#     "odd_numbers": (1, 3, 5),
#     "number_of_even_numbers": 2,
#     "number_of_odd_numbers": 3
# }
```