# Sample digits to arrange into the largest number.
numbers = [2, 3, 9, 2, 2]


def largest_concatenate(numbers):
    result = ""

    # Selecting the largest value first works for individual digits.
    while len(numbers) > 0:
        max_number = max(numbers)
        result = result + str(max_number)
        # Remove one occurrence so each digit is used once.
        numbers.remove(max_number)
    return result


print(largest_concatenate(numbers))
