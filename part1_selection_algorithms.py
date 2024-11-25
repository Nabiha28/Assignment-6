import random

# Part 1: Deterministic Median of Medians Algorithm
def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[len(arr) // 2]

    # Step 1: Divide the array into groups of 5
    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    
    # Step 2: Find the median of each group
    medians = [sorted(group)[len(group) // 2] for group in groups]
    
    # Step 3: Recursively find the median of the medians
    pivot = median_of_medians(medians, len(medians) // 2)
    
    # Partition the array
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]
    
    # Step 4: Recurse into the appropriate partition
    if len(less_than_pivot) >= k:
        return median_of_medians(less_than_pivot, k)
    elif len(less_than_pivot) + len(equal_to_pivot) >= k:
        return pivot
    else:
        return median_of_medians(greater_than_pivot, k - len(less_than_pivot) - len(equal_to_pivot))

# Part 2: Randomized Quickselect Algorithm
def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    # Randomly pick a pivot
    pivot = random.choice(arr)
    
    # Partition the array around the pivot
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]
    
    if len(less_than_pivot) >= k:
        return quickselect(less_than_pivot, k)
    elif len(less_than_pivot) + len(equal_to_pivot) >= k:
        return pivot
    else:
        return quickselect(greater_than_pivot, k - len(less_than_pivot) - len(equal_to_pivot))

# Example usage:
if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    k = 5
    print(f"The {k}-th smallest element (Median of Medians):", median_of_medians(arr, k))
    print(f"The {k}-th smallest element (Randomized Quickselect):", quickselect(arr, k))
