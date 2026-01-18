

def to_roman_numeral(nums):
    if not isinstance(nums, int) or nums <= 0:
        raise ValueError("Input must be a positive number")

    roman_numerals = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    

    result = []
    for (number, roman) in roman_numerals:
        while nums >= number:
            result.append(roman)
            nums -= number

    return ''.join(result)


