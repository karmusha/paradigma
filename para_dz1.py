def sort_list_imperative(numbers):
    for i in range(len(numbers) - 1):
        m = i
        j = i + 1
        while j < len(numbers):
            if numbers[j] < numbers[m]:
                m = j
            j = j + 1
        numbers[i], numbers[m] = numbers[m], numbers[i]
    return numbers

def sort_list_declarative(numbers):
    sorted(numbers)
    return numbers

if __name__ == '__main__':
    nums = [1, 4, 2, 3]
    print(nums)
    print(sort_list_imperative(nums))
    print(sort_list_declarative(nums))