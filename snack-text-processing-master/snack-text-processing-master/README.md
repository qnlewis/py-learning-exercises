# Text Processing Assessment

## Project Description
In this assessment, you will be required to complete the Python functions below. The assessment focuses on:

- String Manipulation
- Loops
- Mathematical Operations
- Pattern Recognition
- Unit Testing
- Conditionals
- Algorithmic Thinking

## Project Structure
```
snack-text-processing/
├── text_processor.py #Your implementation goes here
└── tests/
    └── test_text_processor.py  #Corresponding unittests go here
```

----

## `text_processor.py`

### Complete the following functions:

### `count_vowels(text: str) -> dict`

Count the frequency of each vowel (a, e, i, o, u) in the given text, case-insensitive.

**Parameters:**

- *text (str)*: The input text to analyze. Can contain any characters.

**Returns:**
- *dict*: A dictionary with vowels as keys and their frequencies as values.

**Example output (text = "Hello World"):**
```
{'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0}
```
---
### `reverse_sentence(text: str) -> str`

Reverse the order of words in a sentence while maintaining the order of characters in each word.

**Parameters:**

- *text (str)*: The input sentence to reverse.

**Returns:**

- *str*: The sentence with words in reverse order.

**Example output (text = "Python is amazing"):**
```
"amazing is Python"
```

---

### `generate_fibonacci_string(n: int) -> str`

Generate a string representation of the first n Fibonacci numbers, separated by commas.

**Parameters:**

- *n (int)*: The number of Fibonacci numbers to generate. Must be a positive integer.

**Returns:**

- *str*: A comma-separated string of Fibonacci numbers.

**Example output (n = 8):**
```
"0,1,1,2,3,5,8,13"
```
---
### `encode_caesar(text: str, shift: int) -> str`

Implement a Caesar cipher encryption by shifting each letter in the text by the specified amount.

**Parameters:**

- *text (str)*: The input text to encrypt.
- *shift (int)*: The number of positions to shift each letter.

**Returns:**

- *str*: The encrypted text.

**Example output (text = "abc", shift = 1):**
```
"bcd"
```
---

### `find_anagrams(word: str, word_list: list) -> list`

Find all anagrams of the given word in the provided word list.

An anagram is a word formed by rearranging the letters of another word, using all the original letters exactly once.

**Parameters:**

- *word (str)*: The word to find anagrams for.
- *word_list (list)*: A list of words to search for anagrams.

**Returns:**

- *list*: A list of anagrams found in the word_list.

**Example output (word = "listen", word_list = ["enlist", "silent", "inlets", "banana"]):**
```
["enlist", "silent", "inlets"]
```

---
---

## `test_text_processor.py`

For this assessment, you must follow Test-Driven Development (TDD) principles:

- Write test cases before implementing functions.
- Use the tests to guide your function implementations.

**Note: In addition to the provided test cases, hidden tests will be run to verify the correctness of your implementation. These hidden tests will check edge cases and ensure your functions behave exactly as specified in the requirements.**

---
---

## Definition(s)

- The **Fibonacci sequence** is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.

Example:
```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```

- An **anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

Example:
```
"listen" and "silent" are anagrams of each other.
```

- A **Caesar cipher** is a simple substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. For example, with a shift of 1, 'A' would be replaced by 'B', 'B' would become 'C', and so on.

Example (shift = 3):
```
"abc" becomes "def"
"xyz" becomes "abc" (wrapping around the alphabet)
```

## Testing Your Implementation

To run the tests, navigate to the project directory and run:

```bash
# On most systems, use:
python -m unittest tests/test_text_processor.py

# If you're using a system where Python 3 is not the default, use:
python3 -m unittest tests/test_text_processor.py
```

Make sure all tests pass before submitting your solution.

## Submission Guidelines

1. Complete all functions in `text_processor.py`
2. Ensure all tests pass
3. Do not modify the function signatures or test files
4. Submit your solution by the deadline
