# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

from pdb import run
from unittest import result


def most_frequent(numbers):
    if not numbers:
        raise ValueError("most_frequent() requires a non-empty list")
    
    counts = {}
    best_value = numbers[0]
    best_count = 0

    for n in numbers:
        counts[n] = counts.get(n, 0) + 1
        if counts[n] > best_count:
            best_count = counts[n]
            best_value = n

    return best_value  

def run_tests():
    # Test cases for most_frequent
    assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3
    assert most_frequent([7]) == 7
    assert most_frequent([5, 5, 5, 5]) == 5
    assert most_frequent([1, 2, 3, 4]) in [1, 2, 3, 4] 
    assert most_frequent([1, 1, 2, 2]) in [1, 2]
    assert most_frequent([-1, -1, 0, 0, 0, -2]) == 0
    assert most_frequent([-3, -3, -3, -2, -2]) == -3
    assert most_frequent([10**12, 10**12, 5]) == 10**12
    assert most_frequent([1, 2, 2, 3, 3, 3]) == 3
    assert most_frequent([9, 9, 9, 1, 2, 3]) == 9
    big = [1] * 50_000 + [2] * 49_999
    assert most_frequent(big) == 1
    try:
        most_frequent([])
        assert False, "Expected ValueError for empty list"
    except ValueError:
        pass
    print("All tests passed!")

"""
Time and Space Analysis for problem 1:
- Best-case: O(n) time, O(1) space if all elements are unique
- Worst-case: O(n) time, O(n) space if all elements are the same
- Average-case: O(n) time, O(n) space
- Space complexity: O(n) for the counts dictionary
- Why this approach?
  - We need to count occurrences, so a hash map dictonary is suitable.
  - This approach is efficient for both time and space in practice.
- Could it be optimized?
-Speed could not be optimized further without additional constraints, as we need to examine each element at least once. You could sort the list first so equal numbers sit next to each other which needs less memory but takes longer time.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []
    for n in nums:
        if n not in seen:
            seen.add(n)
            result.append(n)
    return result

def run_tests():
    assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
    assert remove_duplicates([]) == []
    assert remove_duplicates([1]) == [1]
    assert remove_duplicates([3, 1, 2]) == [3, 1, 2]
    assert remove_duplicates([8, 8, 8, 8]) == [8]
    assert remove_duplicates([1, 1, 2, 2, 3, 3]) == [1, 2, 3]
    assert remove_duplicates([1, 2, 3, 1, 2, 3]) == [1, 2, 3]
    assert remove_duplicates([0, -1, 0, -1, 2]) == [0, -1, 2]
    assert remove_duplicates([10**12, 5, 10**12]) == [10**12, 5]
    assert remove_duplicates([9,3,9,1,3]) == [9, 3, 1]

    orginal = [1, 2, 1]
    remove_duplicates(orginal)
    assert orginal == [1, 2, 1]

    big = list(range(50_000)) * 2
    assert remove_duplicates(big) == list(range(50_000))
    print("All tests passed!")

    if __name__ == "__main__":
        run_tests()
"""
Time and Space Analysis for problem 2:
- Best-case: O(n) time, O(1) space if all elements are unique
- Worst-case: O(n) time, O(n) space if all elements are the same
- Average-case: O(n) time, O(n) space
- Space complexity: O(n) for the seen set
- Why this approach?
  - We need to track seen elements and their complements, so a hash set is suitable.
  - This approach is efficient for both time and space in practice.
- Could it be optimized?
    - Speed could not be optimized further without additional constraints, as we need to examine each element at least once. If the list is already sorted, you only need to compare each number to the one before it which uses no additional memory but takes longer time.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []
    for n in nums:
        complement = target - n
        if complement in seen:
            pairs.append((min(n, complement), max(n, complement)))
        seen.add(n)
    return pairs

def normalize(pairs):
    return sorted(pairs)

def run_tests():
    assert normalize(find_pairs([1, 2, 3, 4], 5)) == [(1, 4), (2, 3)]
    assert find_pairs([], 5) == []
    assert find_pairs([5], 10) == []
    assert find_pairs([1, 2, 3], 100) == []
    assert find_pairs([5, 1, 2], 10) == []
    assert normalize(find_pairs([3, 7], 10)) == [(3, 7)]
    assert normalize(find_pairs([-3, -1, 1, 3, 5], 0)) == [(-3, 3), (-1, 1)]
    assert normalize(find_pairs([0, 5, -5, 10], 5)) == [(0, 5)] or \
           normalize(find_pairs([0, 5, -5, 10], 5)) == [(-5, 10), (0, 5)]

    assert find_pairs([0, 1, 2], 0) == []
    assert normalize(find_pairs([1, 2, 3, 4, 5, 6], 7)) == [(1, 6), (2, 5), (3, 4)]
    assert normalize(find_pairs([9, 2, 7, 4, 5], 11)) == [(2, 9), (4, 7)]
    result = find_pairs([4, 1, 3, 2], 5)
    assert len(result) == len(set(result)) == 2

    original = [1, 2, 3, 4]
    find_pairs(original, 5)
    assert original == [1, 2, 3, 4]

    big = list(range(100_000))
    result = find_pairs(big, 99_999)
    assert len(result) == 50_000

    print("All tests passed!")

if __name__ == "__main__":
    run_tests()


"""
Time and Space Analysis for problem 3:
- Best-case: O(n) time, O(1) space if all elements are unique. One pass with instant lookups. The answer can hold up to n/2 pairs, but the space for the seen set is O(n).
- Worst-case: The seen set can grow as large as the list and a bit more for the answer.
- Average-case: O(n) time, O(n) space
- Space complexity: O(n) for the seen set
- Why this approach?
Have I seen the partner? replaces that whole search with on check. Because you only look backward at earlier number each pair is found exactyl once and no cleanup is needed. The answer can hold up to n/2 pairs, but the space for the seen set is O(n).. 
- Could it be optimized?
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n, initial_capacity=2):
    if n < 0:
        raise ValueError("n must be non-negative")
    if initial_capacity <1:
        raise ValueError("initial_capacity must be at least 1")
    
    capacity = initial_capacity
    storage = [None] * capacity
    size = 0
    resizes = 0 
    total_copies = 0

    for item in range(n):
        if size == capacity:
            new_capacity = capacity * 2
            print(f"Resizing from {capacity} -> {new_capacity}"
                  f"(copying {size} elements)")
            new_storage = [None] * new_capacity
            for i in range(size):
                new_storage[i] = storage[i]
            storage = new_storage
            capacity = new_capacity
            resizes += 1
            total_copies += size
        storage[size] = item
        size += 1

        return {
            "items": storage[:size],
            "capacity": capacity,
            "resizes": resizes,
            "copies": total_copies,
        }
    
    import io
    from contextlib import redirect_stdout

    def run (n, cap=2):
        buf = io.StringIO()
        with redirect_stdout(buf):
            result = add_n_items(n, cap)
        return result, buf.getvalue()
    
    def run_tests():
        result, out = run(6)
        assert result["items"] == [0, 1, 2, 3, 4, 5]
        assert result["resizes"] == 2
        assert result["copies"] == 2 + 4
        assert result["capacity"] == 8
        assert out.count("Resizing") == 2
        assert "capacity 2 -> 4" in out and "capacity 4 -> 8" in out

        result, out = run(0)
    assert result["items"] == [] and result["resizes"] == 0 and out == ""

    result, out = run(1)
    assert result["resizes"] == 0 and out == ""

    result, out = run(2)
    assert result["resizes"] == 0 and result["capacity"] == 2

    result, out = run(3)
    assert result["resizes"] == 1 and result["copies"] == 2
    assert result["capacity"] == 4

    result, out = run(8, cap=1)
    assert result["resizes"] == 3          # 1->2, 2->4, 4->8
    assert result["copies"] == 1 + 2 + 4
    assert result["capacity"] == 8
    assert result["items"] == list(range(8))

    result, out = run(5, cap=10)
    assert result["resizes"] == 0 and result["capacity"] == 10

    result, _ = run(20)
    assert result["items"] == list(range(20))

    n = 100_000
    result, _ = run(n)
    assert result["copies"] < 2 * n
    assert result["resizes"] == 16          
    assert result["capacity"] == 131072

    for bad_args in [(-1, 2), (5, 0), (5, -3)]:
        try:
            add_n_items(*bad_args)
            assert False, f"Expected ValueError for {bad_args}"
        except ValueError:
            pass

    print("All tests passed!")


if __name__ == "__main__":
    print("--- Demo: add_n_items(6) ---")
    add_n_items(6)
    print()
    run_tests()

    

"""
Time and Space Analysis for problem 4:
- When do resizes happen? A resize happens when the number of items equals the current capacity.
- What is the worst-case for a single append? The worst-case is O(n) when a resize occurs.If the list is full, that one append must create a new list and copy
  every existing element into it before adding the new item.
- What is the amortized time per append overall? The amortized time is O(1) because most appends are O(1) and resizes happen infrequently.
- Space complexity: O(n) for the storage list.
- Why does doubling reduce the cost overall? Doubling the capacity means that each resize can accommodate many more elements, spreading the cost of copying over many appends.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

 #Problem 5 (Refactored): Compute Running Totals

from itertools import accumulate

def running_total_original(nums):
    result = []
    total = 0
    for n in nums:
        total += n
        result.append(total)
    return result


# REFACTORED SOLUTION 
def running_total(nums, in_place=False):
    """Return running totals of `nums`.

    If in_place=True, overwrite `nums` with the totals and return it.
    Otherwise return a new list and leave `nums` unchanged.
    """

    if in_place:
        total = 0
        for i, n in enumerate(nums):
            total += n
            nums[i] = total
        return nums
    return list(accumulate(nums))


# ---------- Tests ----------
def run_tests():
    for fn in (running_total_original, running_total):
        assert fn([1, 2, 3, 4]) == [1, 3, 6, 10]
        assert fn([]) == []
        assert fn([5]) == [5]
        assert fn([-1, -2, -3]) == [-1, -3, -6]
        assert fn([5, -5, 3, -3]) == [5, 0, 3, 0]

    original = [1, 2, 3]
    running_total(original)
    assert original == [1, 2, 3]         

    data = [1, 2, 3, 4]
    assert running_total(data, in_place=True) is data
    assert data == [1, 3, 6, 10]         

    big = list(range(1, 100_001))
    assert running_total(big) == running_total_original(big)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()


"""
Time and Space Analysis for problem 5:
- Best-case: One pass, one additional per item.
- Worst-case: One pass with a constant-time addition and append per element (appends are amortized O(1)
- Average-case: O(n) time, O(n) space
- Space complexity: O(n) for the result list
- Why this approach? The slow alternative is to sum each slice of the list, which is O(n^2). This approach is O(n).
- Could it be optimized? Every number has to be read, pythons itertools.accumulate() is a built-in that does this in C, but the time complexity is still O(n).

"""
#The original solution loops through the list in python, adding each number to a running total and appending it to a new list. The refactored solution uses itertools.accumulate() for the same effect, and also allows for in-place modification of the input list if desired. Both versions are O(n) time and O(n) space, but the refactored version is more concise and leverages built-in functionality. There is also an optional in place mode that overwrites the input list instead. Overall the refactored solution improves speed by a small constant factor and reduces code complexity, while maintaining the same time and space complexity.