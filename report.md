# Report on Order Statistics and Elementary Data Structures

Introduction

As part of Assignment 6, this report discusses the application and evaluation of the Selection Algorithms and Elementary Data Structures. In addition to the basic data structure - array, stack, queue and linked list, this project is to provide students an opportunity to actually engage in the implementation and practice of an algorithm that selects the \\(k^{th}\\) smallest element among an array.

 Part 1: Selection Algorithms

1.1 Deterministic Algorithm: Median of Medians

The Median of Medians algorithm selects the \\(k^{th}\\) smallest element in an unsorted array in worst-case O(n) time by recursively selecting the median of medians and using that as a pivot to partition the array.

Algorithm:
1. Divide the array into groups of 5 elements.
2. Find the median of each group by sorting the group and picking the middle element.
3. Recursively find the median of the medians from the medians of all groups.
4. Partition the array based on the median of medians (as pivot).
5. Recurse into the appropriate partition (left, middle, or right).

Time Complexity:
- Best-case: O(n)
-Worst-case: O(n)
- Space Complexity: O(n) due to the recursive nature and storage of subarrays.

Example:

arr = [3, 1, 4, 1, 5, 9, 2, 5,6, 3, 5]
k = 5
result = median_of_medians(arr, k)
print(result)

This algorithm guarantees O(n) time complexity even in the worst-case scenario, unlike other sorting-based algorithms that may take O(n log n) time.

1.2 Randomized Algorithm: Quickselect
The Randomized Quickselect algorithm is a variation of QuickSort that is used to find the kthk^{th}kth smallest element. It selects a random pivot, partitions the array around that pivot, and recursively selects from the partition that contains the kthk^{th}kth smallest element.

Algorithm:
Randomly pick a pivot element from the array.
Partition the array into elements less than, equal to, and greater than the pivot.
Recurse into the partition containing the kthk^{th}kth smallest element.
If the pivot is the kthk^{th}kth element, return it.
Time Complexity:
Best-case: O(n)
Expected time: O(n) due to the randomness of the pivot selection.
Worst-case: O(n^2), but this is highly unlikely.
Space Complexity: O(log n) due to the recursive stack.
Example:

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k = 5
result = quickselect(arr, k)
print(result)  
While the worst-case time complexity of Quickselect is O(n^2), the expected time complexity is O(n), making it much faster than other selection algorithms in practice

Part 2: Elementary Data Structures

2.1 Arrays
Arrays are a fundamental data structure used for storing elements of the same type. Operations like insertion, deletion, and access can be performed on arrays.
Insertion: O(1) for inserting at the end (if space allows).
Deletion: O(n) for deleting an element from the middle (requires shifting elements).
Access: O(1) for accessing an element by index.
Example:

arr = Array(5)
arr.insert(0, 10)
arr.insert(1, 20)
print(arr.access(1))  

2.2 Stacks
A stack follows the Last In, First Out (LIFO) principle. Operations include push (insert an element) and pop (remove the top element).
Push: O(1)
Pop: O(1)
Peek: O(1)
Stacks are used in scenarios like function calls (recursion) and undo mechanisms.
Example:

stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())  

2.3 Queues
A queue follows the First In, First Out (FIFO) principle. Operations include enqueue (insert an element) and dequeue (remove the front element).
Enqueue: O(1)
Dequeue: O(1)
Peek: O(1)
Queues are used in scenarios like task scheduling and data streaming.
Example:
python
Copy code
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue())  

2.4 Linked Lists
A linked list is a linear data structure where each element (node) contains data and a reference (link) to the next node. Linked lists are flexible because they allow efficient insertions and deletions compared to arrays.
Insertion at head: O(1)
Insertion at tail: O(n)
Deletion: O(n) (unless directly referencing the node)
Traversal: O(n)
Example:

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.delete(10)

2.5 Comparison of Data Structures
Data StructureInsertion ComplexityDeletion ComplexityAccess Complexity
Array	O(1) (at end), O(n) (at middle)	O(n)	O(1)
Stack	O(1)	O(1)	O(1)
Queue	O(1)	O(1)	O(1)
Linked List	O(1) (at head)	O(n) (general)	O(n)
In scenarios where memory is tightly managed, or when elements are frequently added and removed, linked lists are ideal. However, arrays are better when access speed is crucial.
Practical Applications of Data Structures
Arrays: Used when you need fast access to elements by index. Commonly used in sorting, searching, and matrix manipulations.
Stacks: Useful in function calls, backtracking algorithms, and undo operations (e.g., in text editors).
Queues: Widely used in task scheduling, print spooling, and data pipelines where tasks need to be processed in the order they arrive.
Linked Lists: Ideal when you frequently insert or delete elements from the middle or beginning of the list, such as in dynamic memory allocation or implementing databases.

Conclusion
This assignment helped reinforce key algorithmic concepts related to selection algorithms and elementary data structures. The Median of Medians and Quickselect algorithms are both effective for order statistics, with each having its own strengths in terms of time complexity and practical use cases. The basic data structures — arrays, stacks, queues, and linked lists — serve as the building blocks for many more advanced algorithms and systems in computer science.