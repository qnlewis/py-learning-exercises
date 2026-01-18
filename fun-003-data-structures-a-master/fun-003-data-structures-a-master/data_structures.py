import random



def generate_random_list(length: int) -> list:
    return [random.randint(1, 100) for _ in range(length)]


def find_max(numbers: list) -> int:
    return max(numbers)


def find_min(numbers: list) -> int:
    return min(numbers)


def find_average(numbers: list) -> float:
    return round(sum(numbers) / len(numbers), 1)


def find_even_pairs(numbers: list) -> list:
    even_pairs = []
    for i in range(len(numbers) - 1):
        if (numbers[i] + numbers[i+1]) % 2 == 0:
            even_pairs.append((i, i+1))
    return even_pairs


def find_odd_pairs(numbers: list) -> list:
    odd_pairs = []
    for i in range(len(numbers) - 1):
        if (numbers[i] + numbers[i+1]) % 2 != 0:
            odd_pairs.append((i, i+1))
    return odd_pairs


def find_number_of_even_numbers(numbers: list) -> int:
    return sum(1 for num in numbers if num % 2 == 0)


def find_number_of_odd_numbers(numbers: list) -> int:
    return sum(1 for num in numbers if num % 2 != 0)


def find_even_numbers(numbers: list) -> tuple:
    return tuple(num for num in numbers if num % 2 == 0)


def find_odd_numbers(numbers: list) -> tuple:
    return tuple(num for num in numbers if num % 2 != 0)


def return_list_stats(numbers: list) -> dict:
    stats = {
        "unique_numbers": set(numbers),
        "max": find_max(numbers),
        "min": find_min(numbers),
        "average": find_average(numbers),
        "even_pairs": find_even_pairs(numbers),
        "odd_pairs": find_odd_pairs(numbers),
        "even_numbers": find_even_numbers(numbers),
        "odd_numbers": find_odd_numbers(numbers),
        "number_of_even_numbers": find_number_of_even_numbers(numbers),
        "number_of_odd_numbers": find_number_of_odd_numbers(numbers)
    }
    return stats
