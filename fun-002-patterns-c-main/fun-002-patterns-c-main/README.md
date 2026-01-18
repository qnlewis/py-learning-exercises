# Project Description
In this assessment, you will be required to complete the python problems below. The assessment focuses on:

- String Manipulation
- Loops
- Mathematical Operations
- Pattern Recognition
- Unit Testing
- Conditionals
- Algorithmic Thinking

## Project Structure
```
fun-002-patterns/
├──patterns.py #Your implementation goes here
└── tests/
    └── test_patterns.py  #Corresponding unittests go here
```

---

## `test_patterns.py`

For this assessment, you must follow Test-Driven Development (TDD) principles:

- Write test cases before/alongside implementing the functionilites.


To check if **your** code passes **your** own test cases, run:

```bash
python3 -m unittest tests/test_patterns.py
```

***NB: You can run(copy and paste) the following commands on your terminal to run our hidden tests against your implementation***

```bash
chmod +x .lms/run_hidden.sh  #Run this only once
```

```bash
.lms/run_hidden.sh   #You can run this every time you want to test against the hidden tests
```


----

## `patterns.py`

### Complete the following functions:

### `draw_square(height: int) -> str`


Generate a square pattern made of asterisks (*) based on the specified height.

Each row contains 'height' number of asterisks, and the number of rows
is equal to the height, forming a square.

**Parameters:**

- *height (int)*: The height (and width) of the square. Must be a positive integer.

**Returns:**
- *String*: Returns the square pattern.

**Example output (height = 3):**
```
***
***
***
```
---
### `draw_pyramid(height: int) -> str`

Generate a symmetrical pyramid made of asterisks (*) based on the specified height.

Each row contains an odd number of asterisks centered with spaces so that the
pyramid is symmetrical. The number of rows equals the height provided.

**Parameters:**

- *height (int)*: The height of the pyramid. Must be a positive integer.

**Returns:**

- *str*: Returns the pyramid pattern as a string.

**Example output (height = 4):**
```
   *
  ***
 *****
*******
```

---


### `draw_triangle(height: int) -> str`

Generate a number triangle where each row contains numbers
starting from 1 up to the row number in order.

Each row will display numbers starting from 1 and increasing up to the
number of the row, forming a left-aligned triangle.

**Parameters:**

- *height (int)*: The height of the triangle. Must be a positive integer.

**Returns:**

- *str*: Returns the triangle pattern.

**Example output (height = 8):**
```
1
12
123
1234
12345
123456
1234567
12345678
```
---
### `draw_triangle_reversed(height: int) -> str`

Generate a reversed number triangle where each row contains numbers
starting from max height down to 1 in order.

Each row will display numbers starting from the height and decreasing to
1, forming a left-aligned upside down triangle.

**Parameters:**

- *height (int)*: The height of the triangle. Must be a positive integer.

**Returns:**

- *str*: Returns the triangle pattern.

**Example output (height = 3):**
```
321
21
1
```
---

### `draw_triangle_prime(height: int) -> str`

Generate a triangle where row i contains the i-th consecutive prime numbers

Each row *i* should contain *i* consecutive prime numbers in ascending order, starting from the first prime number (2).


**Parameters:**

- *height (int)*: The height of the triangle. Must be a positive integer.

**Returns:**

- *str*: Returns the triangle pattern.

**Example output (height = 4):**

```
2
3 5
7 11 13
17 19 23 29
```

---



## Definition(s)

- A prime number is a natural number greater than 1 that has exactly two distinct positive divisors:
1 and itself.

    In other words, a prime number cannot be divided evenly by any other number except 1 and the number itself.

Example:

```
2, 3, 5, 7, 11, 13, 17, 19, ...
```