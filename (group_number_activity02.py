


import random
import time

""" Phase 1 """
def generated_sort_data(size):
    """In this step,
    the function would generate an array of random integers from 1 to 100 in a size inputted by the user."""
    element = []
    for i in range(size):
        element.append(random.randint(1,100))
    print("Generated Array:",element)
    """In this step, the function will start insertionally sorting the values within the generated array"""
    length_data = len(element)
    for i in range(1,length_data):
        point = element[i]
        x = i
        """Stating the condition needed for the value, and moving values greater than 'point' to 1 step ahead"""
        while x > 0 and element[x - 1] > point:
            x = x - 1
        """The new idea introduced for insertion sorting here is slicing, which arranges 'point' to the correct position"""
        element = element[:x] + [point] + element[x:i] + element[i + 1:]
    return element

""" Phase 2 """
def binary_search(result,target):
    """Determining the starting and stopping points"""
    start = 0
    stop = len(result) -1
    while start <= stop:
        """Declaring to the function, how to calculate the middle point after every movement"""
        middle = (start + stop) // 2

        """"Providing the conditions in order to find the target"""

        """Terminating the halfs, depending on the conditions"""
        if result[middle] == target:
            return middle
        elif result[middle] < target:
            """Stating the function to move the starting point the right side of the middle point"""
            start = middle + 1
        elif result[middle] > target:
            """Stating the function to move the stoping point the left side of the middle point"""
            stop = middle - 1
    """If loop was ended and target is not found, False will be returned with following conditions on the main"""
    return False

#Zayed Mohammad's part
""" Phase 3 """
def generate_sorted_data():
    ''' Generate the dataset with a fixed set and add additional random numbers'''
    large_data = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44] + [random.randint(1, 100) for _ in range(990)]
    print('generated data:',large_data)
    
    ''' Sort the dataset using merge sort'''
    return merge_sort(large_data)

def merge_sort(arr):
    ''' If the array is a single element, return it '''
    if len(arr) <= 1:
        return arr
    
    ''' Find the middle point and divide the array into two halves'''
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    ''' Merge the sorted halves'''
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = 0
    j = 0
    
    ''' Use a for loop to merge elements from both halves'''
    for _ in range(len(left) + len(right)):
        if i < len(left) and (j >= len(right) or left[i] <= right[j]):
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    return sorted_array

#Aaron's part
'''Phase 4'''

'''This phase we will implement both binary and linear search'''
'''Also learning which of the searches is more efficient'''
'''Using the sorted large array formed at phase 3 '''

'''Linear search'''
def linear_search(sorted_array,expected):
    '''We have added star and stop value which indicate the total time taken for excecuting the entire function'''
    start = time.perf_counter()
    for o in range(len(sorted_array)):
        if sorted_array[o] == expected:
            print(expected,"Is found in the array")
            break
    else:
        print(expected,"Doesnt exist in the array")
    end = time.perf_counter()
    timetaken = end - start
    print(timetaken)

'''Binary search'''
def binary_search(sorted_array,expected):
    '''We have added star and stop value which indicate the total time taken for excecuting the entire function'''
    start = time.perf_counter()
    left = 0
    right=len(sorted_array)-1
    while left <= right:
        mid = (left+right) // 2
        if sorted_array[mid]==expected:
            print(expected,"Exists in the array  ")
            end = time.perf_counter()
            print("time taken",end-start)
            break
        elif sorted_array[mid]<expected:
            left = mid + 1
        else:
            right = mid-1
    
    print(expected,"Doesn't exist in the array.")
    end = time.perf_counter()
    timetaken = end - start
    print(timetaken)

def main():
    result = generated_sort_data(10)
    print("Sorting...")
    print("New Array:",result)
    target = int(input("Enter your target number: "))
    result_1 = binary_search(result,target)
    if result_1 is False:
        print("The Target number",target,"was not found:")
    else:
        print("The Target number",target,"was found on index",result.index(target))
    ''' Generate and sort a dataset of 1,000 elements'''
    sorted_data = generate_sorted_data()
    print("sorted data using merge sort:",sorted_data)
    B = int(input("Enter the value to be searched: "))
    linear_search(sorted_data,B)
    binary_search(sorted_data,B)
    
main()

