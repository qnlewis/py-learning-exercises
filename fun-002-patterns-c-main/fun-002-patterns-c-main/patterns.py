def draw_square(height: int) -> str:
    if height <= 0:
        return ""
    return "\n".join(["*" * height for _ in range(height)])
    
def draw_pyramid(height: int) -> str:
    if height <= 0:
        return ""
    result = []
    for i in range(1, height + 1):
        stars = "*" * (2 * i - 1)
        spaces = " " * (height - i)
        result.append(spaces + stars )
    return "\n".join(result)

def draw_triangle(height: int) -> str:
    if height <= 0:
        return ""
    result = []
    for i in range(1, height + 1):
        row = "".join(str(num) for num in range(1, i + 1))
        result.append(row)
    return "\n".join(result)

def draw_triangle_reversed(height: int) -> str:
    if height <= 0:
        return ""
    result = []
    for i in range(height, 0, -1):
        row = "".join(str(num) for num in range(i, 0, -1))
        result.append(row)
    return "\n".join(result)

def is_prime(n: int):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def draw_triangle_prime(height: int) -> str:
    if height <= 0:
        return ""
    
    primes = []
    num = 2
    while len(primes) < height * (height + 1) // 2:
        if is_prime(num):
            primes.append(num)
        num += 1
    
    result = []
    index = 0
    for i in range(1, height + 1):
        row = " ".join(map(str, primes[index:index + i]))
        result.append(row)
        index += i
    return "\n".join(result)


print(draw_square(3))
print(draw_pyramid(3))
print(draw_triangle(8))
print(draw_triangle_reversed(8))
print(draw_triangle_prime(6))