# OPTION 1 - FIND DUPLICATE
# DO NOT SHARE

from typing import List

# Implement a function to identify a duplicate integer in an unsorted array
# of integers. Talk about time/space complexity for each method you implement.

# `input` contains exactly N+1 numbers
# `input` elements are integers in the domain [1, N]
# `input` contains all integers in the domain [1, N] at least once
# `findDuplicate` returns an `int`: the duplicate integer
def findDuplicate(input: List[int]) -> int:
    input.sort()
    for a in range(len(input)):
        if input[a] == input[a+1]:
            return input[a]
        
print(findDuplicate([1,1,2]))
print(findDuplicate([5,8,9,2,3,4,1,7,8,6]))
print(findDuplicate([2,2,1,3]))
print(findDuplicate([1,4,2,4,3]))


#Sort has time complexity O(n log n), while running through the list
#has time complexity O(n)
def findDuplicate(input: List[int]) -> int:
    result = {}
    for item in input:
        if item not in result:
            result[item] = 0
        result[item] = result[item] + 1
    for key, value in result.items():
        if value == 2:
            return key    

print(findDuplicate([1,1,2]))
print(findDuplicate([5,8,9,2,3,4,1,7,8,6]))
print(findDuplicate([2,2,1,3]))
print(findDuplicate([1,4,2,4,3]))

#The initial dictionary creation has time complexity O(n) while sorting through
#the list has time complexity O(n) in the worst case. This is more effective
#than the first algorithm
