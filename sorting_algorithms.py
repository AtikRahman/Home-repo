def is_sorted(numbers):
    is_sorted = True
    for i in range(len(numbers)-1):
        if numbers[i]>numbers[i+1]:
            is_sorted = False
            break
    return is_sorted

#bubbles up towards the first place
def bubble_sort(numbers):
    length = len(numbers)
    while not is_sorted(numbers):
        for i in range(length-1):
            if numbers[i]>numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    return numbers

#inserting a key before larger values
def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        if numbers[i]<numbers[i-1]:
            temp = numbers[i]
            left = i-1
            while temp<numbers[left]:
                numbers[left+1] = numbers[left]
                left -= 1
                if left < 0:
                    break               
            numbers[left+1] = temp
    return numbers

#select smallest and swap it
def selection_sort(numbers):
    length = len(numbers)
    for i in range(length):
        s_index = i
        for j in range(i+1, length):
            if numbers[s_index]>numbers[j]:
                s_index = j
        numbers[i], numbers[s_index] = numbers[s_index], numbers[i]
    return numbers

def partition(numbers, low, high):
    pivot = numbers[high]
    pivot_index = high
    high -= 1
    while 1:
        while numbers[low]<pivot and low<high:
            low += 1
        while numbers[high]>pivot and low<high:
            high -= 1
        if low >= high:
            break
        else:
            numbers[low], numbers[high] = numbers[high], numbers[low]
    if low == high and numbers[low] > numbers[pivot_index]:
        numbers[low], numbers[pivot_index] = numbers[pivot_index], numbers[low]
    return low


# it utilize divide and conquer approach
def quick_sort(numbers, low, high):
    if any([low<0, high<0, low>=high]):
        return
    pivot_index = partition(numbers, low, high)
    
    quick_sort(numbers, low, pivot_index-1)
    quick_sort(numbers, pivot_index+1, high)

def merge(left_list, right_list):
    sorted_numbers = []
    while left_list and right_list:
        if left_list[0] < right_list[0]:
            sorted_numbers.append(left_list[0])
            left_list.pop(0)
        else:
            sorted_numbers.append(right_list[0])
            right_list.pop(0)
    while left_list:
        sorted_numbers.append(left_list[0])
        left_list.pop(0)
    while right_list:
        sorted_numbers.append(right_list[0])
        right_list.pop(0)
    return sorted_numbers

def merge_sort(new_list):
    length = len(new_list)
    if length == 1:
        return new_list
    middle = int(1+(length-1)/2)
    left = merge_sort(new_list[:middle])
    right = merge_sort(new_list[middle:])
    return merge(left, right)

with open("hello.txt", "r") as file:
    unsorted_numbers = file.read()

unsorted_numbers = list(map(int, unsorted_numbers.split()))
print("\nunsorted numbers: ")
print(unsorted_numbers, "\n")

sorting_algorithms = ["bubble_sort", "insertion_sort", "selection_sort", "quick_sort", "merge_sort"]
for algorithm in sorting_algorithms:
    if algorithm == "quick_sort":
        sorted_list = unsorted_numbers[:]
        expression = algorithm + "(" + "sorted_list," + "0," + "len(sorted_list)-1" + ")"
        eval(expression)
    else:
        numbers = unsorted_numbers[:]
        expression = algorithm + "(" + "numbers" + ")"
        sorted_list = eval(expression)

    print("after ", algorithm)
    print(sorted_list, "\n")

