# Assignment-6
# Order Statistics and Elementary Data Structures

This repository contains the implementation of selection algorithms and elementary data structures as part of **Assignment 6**. The goal of this assignment is to implement and analyze the performance of various algorithms and data structures, and understand their practical applications.

## Assignment Overview

### Part 1: Selection Algorithms
In this part, we implement two algorithms for selecting the \(k^{th}\) smallest element (order statistics) from an unsorted array:
- **Deterministic Algorithm (Median of Medians)**: This algorithm guarantees worst-case O(n) time complexity by recursively finding the median of medians. It is an optimal selection algorithm in terms of worst-case performance.
- **Randomized Algorithm (Quickselect)**: This algorithm works by randomly selecting a pivot element, and partitioning the array around that pivot. The expected time complexity is O(n), but it is not guaranteed in the worst case.

### Part 2: Elementary Data Structures
This part of the assignment focuses on implementing the following elementary data structures:
- **Arrays**: Implement basic operations like insertion, deletion, and access.
- **Stacks**: Implement stack operations using arrays, providing LIFO (Last In, First Out) functionality.
- **Queues**: Implement queue operations using arrays, providing FIFO (First In, First Out) functionality.
- **Linked Lists**: Implement singly linked lists with basic operations like insertion, deletion, and traversal.

Files in this Repository
part1_selection_algorithms.py: Contains the Python implementation of the deterministic and randomized selection algorithms.
part2_data_structures.py: Contains the Python implementation of arrays, stacks, queues, and linked lists.
report.md: A detailed report discussing the implementation, performance analysis, and practical applications of the algorithms and data structures.
README.md: This file, which contains an overview of the repository and instructions for running the code.