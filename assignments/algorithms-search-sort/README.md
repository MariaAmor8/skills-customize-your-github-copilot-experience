# 📘 Assignment: Algorithms — Search and Sort Fundamentals

## 🎯 Objective

Practice fundamental algorithms: implement and compare linear and binary search, plus two sorting algorithms (bubble sort and merge sort). Students will reason about correctness and basic time complexity.

## 📝 Tasks

### 🛠️ Implement Search Algorithms

#### Description
Write functions for linear search and binary search that return the index of a target value or `-1` if not found.

#### Requirements
Completed program should:

- Implement `linear_search(arr, target)` that scans `arr` for `target`
- Implement `binary_search(arr, target)` that assumes `arr` is sorted
- Both functions should return the index of `target` or `-1` if missing
- Include brief examples showing usage and expected results


### 🛠️ Implement Sorting Algorithms

#### Description
Implement bubble sort and merge sort to sort lists of numbers.

#### Requirements
Completed program should:

- Implement `bubble_sort(arr)` and `merge_sort(arr)`
- `bubble_sort` should sort in-place or return a new sorted list
- `merge_sort` should return a new sorted list and use the divide-and-conquer approach
- Provide short examples demonstrating correctness


### 🛠️ Compare Performance and Write Simple Tests

#### Description
Measure and compare the runtime of the algorithms on small and medium-sized inputs and add simple correctness checks.

#### Requirements
Completed program should:

- Include a simple timing harness that measures execution time for each algorithm on the same inputs
- Include at least three unit-style checks verifying correctness on edge cases (empty list, single-element, duplicates)
- Document which algorithm is faster for which input sizes and why (short paragraph)

---

Students should implement their solutions in `starter-code.py`. To run quick checks, execute:

```bash
python assignments/algorithms-search-sort/starter-code.py
```
