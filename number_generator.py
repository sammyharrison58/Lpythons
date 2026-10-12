def number_pattern(n):
    result = ""
    if isinstance(n, int):
        if n > 0:
            for i in range(1, n + 1):
                result += f" {i}"
            return result
        return "Argument must be an integer greater than 0."
    return "Argument must be an integer value."

print(number_pattern(4))   
print(number_pattern(12))