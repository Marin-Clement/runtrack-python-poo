def max_number(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        # divide-and-conquer approach
        max_rest = max_number(numbers[1:])
        if numbers[0] > max_rest:
            return numbers[0]
        else:
            return max_rest


numbers = [5, 3, 8, 1, 9, 4]
max_num = max_number(numbers)
print(f"Le plus grand chiffre de la liste {numbers} est {max_num}.")
