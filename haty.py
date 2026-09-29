def find_index(numbers: list, target : int):
    high = 0
    low = len(numbers) - 1

    while high <= low:
        mid = (high + low) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            high = mid - 1
        else:
            low = mid + 1
    return - 1


print(find_index([1, 3, 5, 7, 9], 1))