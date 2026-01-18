# How to Answer the Test and Understand the Skeleton Code
```
This document provides a detailed explanation of how to answer the test and understand the skeleton code provided for the Hangman game. The code is written in Python and uses the unittest framework along with unittest.mock to test the functionality of the Hangman game.
```
# 1.Understanding the Code Structure
```
The code is divided into two main parts:
```
* ```repeating_instruc.py```: This is the module where the actual Hangman game logic is implemented. It contains functions like ```get_guess```, ```is_correct_guess```, ```update_display```, ```is_not_correct_guess```, ```fully_guessed```, ```is_winner```, and ```play_game```.

* ```test_repeating_instruc,py```: This is the test file that uses the unittest framework and unittest.mock to test the functions in ```repeating_instruc.py```.

# 2. Functions to Implement in repeating_instruc.py
```
You need to implement the following functions in ```repeating_instruc.py```:
```
``get_guess()``:

* Purpose: This function prompts the player to input a guess.

```is_correct_guess(word, guess)```:

* Purpose: This function checks if the guessed letter is in the word.

```update_display(word, guess, display)```:

* Purpose: This function updates the display of the word based on the guessed letter.

```is_not_correct_guess(attempts)```:

* Purpose: This function handles an incorrect guess by decrementing the number of attempts and printing a message.

```fully_guessed(display)```:

* Purpose: This function checks if the word has been fully guessed.

```is_winner(display, word)```:

* Purpose: This function determines if the player has won or lost the game.

```play_game()```:

* Purpose: This function runs the Hangman game, integrating all the above functions.

# 3.How to Run the Tests
To run the tests, follow these steps:

Implement the Functions: First, implement the functions in ```repeating_instruc.py```.

Run the Test File: Use the following command to run the test file:

```

python3 -m unittest test_hangman_game.py
python3 .hiddenTest/run_tests.py

```
    
Check the Results: The test runner will execute the test cases and report the results. If all tests pass, your implementation is correct. If any test fails, review the implementation and fix any issues. 