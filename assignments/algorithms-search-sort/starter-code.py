import time
import random


def linear_search(arr, target):
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1


def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def _time_fn(fn, *args, repeats=3):
    start = time.perf_counter()
    for _ in range(repeats):
        fn(*args)
    end = time.perf_counter()
    return (end - start) / repeats


def _run_basic_checks():
    # correctness checks
    assert linear_search([], 1) == -1
    assert linear_search([5], 5) == 0
    assert binary_search([1,2,3], 2) == 1
    assert bubble_sort([3,2,1]) == [1,2,3]
    assert merge_sort([3,2,1]) == [1,2,3]
    print("Basic checks passed")


def _demo_timing():
    small = random.sample(range(1000), 100)
    medium = random.sample(range(5000), 1000)

    print("Timing on small input (100)")
    print("linear_search:", _time_fn(linear_search, small, small[-1]))
    print("binary_search:", _time_fn(binary_search, sorted(small), small[-1]))

    print("bubble_sort:", _time_fn(bubble_sort, small))
    print("merge_sort:", _time_fn(merge_sort, small))

    print("Timing on medium input (1000)")
    print("bubble_sort:", _time_fn(bubble_sort, medium))
    print("merge_sort:", _time_fn(merge_sort, medium))


if __name__ == "__main__":
    _run_basic_checks()
    _demo_timing()
