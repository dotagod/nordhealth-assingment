# Find Pairs with Equal Sum

This program finds all unique pairs in an unsorted array that have the same sum. Given an array of integers, it identifies and groups pairs of numbers that add up to the same value.

## Problem Statement

The problem is to find all unique pairs in a given array of integers such that the sum of each pair is the same.

For example:
- Input: `[6, 4, 12, 10, 22, 54, 32, 42, 21, 11]`
- Output: Multiple sets of pairs with equal sums, like:
  - Pairs (6, 10) and (4, 12) have sum 16
  - Pairs (10, 22) and (11, 21) have sum 32

## Solution Approach

The solution implements an optimized Two-Sum based algorithm with single-threaded processing to find pairs with equal sums efficiently. Performance testing showed this approach consistently outperformed multi-threaded implementations for this specific problem.

### Key Features

1. **Object-Oriented Design**: Uses clear class organization with separation of concerns
2. **Optimized Single-Threaded Algorithm**: Based on performance testing, a single-threaded approach outperformed multi-threading for this specific problem
3. **Smart Optimization**: Pre-sorts the array and uses efficient data structures to improve performance
4. **Comprehensive Error Handling**: Validates inputs and gracefully handles edge cases
5. **Extensive Testing**: Includes unit tests for various scenarios

### Algorithm

The solution uses a Two-Sum based approach with these steps:

1. Sort the input array for better performance
2. Efficiently generate all possible pairs in a single pass:
   - Calculate the sum of each pair
   - Store pairs directly into a dictionary grouped by their sum
   - Use different strategies for arrays with/without duplicates
   - Track seen pairs to avoid duplicates
3. Filter to only keep sums with at least two different pairs

The time complexity is O(n²) in the worst case, but the actual performance is significantly improved through:
- Pre-sorting for better locality and cache performance
- Direct sum calculation without redundant comparisons
- Optimized data structures with O(1) lookups

## Requirements

- Python 3.6+
- No external dependencies required (uses only standard library)

## Usage

### Command Line Interface

The program provides a flexible command-line interface with multiple options:

#### Process Example Data

```bash
python3 main.py --example 1    # Run the first example from the problem statement
python3 main.py --example 2    # Run the second example from the problem statement
```

#### Process Custom Array

```bash
python3 main.py --array 6 4 12 10 22 54 32 42 21 11
```

#### Process Array from File

```bash
python3 main.py --file path/to/file.txt
```
Each number in the file should be on a separate line.

#### Run Unit Tests

```bash
python3 main.py --test
```

#### Enable Verbose Logging

Add the `--verbose` flag to any command for detailed logging:

```bash
python3 main.py --array 6 4 12 10 22 54 32 42 21 11 --verbose
```

### Testing with Large Arrays

For performance testing with large arrays, you can use Python directly:

```bash
python3 -c "import main; import random; import time; large_array = [random.randint(-1000, 1000) for _ in range(2000)]; start = time.time(); main.process_array(large_array, verbose=True); print(f'Total execution time for 2000 elements: {time.time() - start:.4f} seconds')"
```

This command creates a random array of 2000 integers between -1000 and 1000, and measures the processing time.

You can adjust the array size and range to test different scenarios:

```bash
# Test with 5000 elements
python3 -c "import main; import random; import time; large_array = [random.randint(-1000, 1000) for _ in range(5000)]; start = time.time(); main.process_array(large_array, verbose=True); print(f'Total execution time for 5000 elements: {time.time() - start:.4f} seconds')"
```

## Performance Optimization

The solution includes several optimizations:

1. **Two-Sum Based Approach**: Implements an optimized algorithm inspired by the classic "Two-Sum" problem, creating all pairs and grouping them directly by sum.

2. **Pre-Sorting**: The array is sorted first to improve cache locality and duplicate handling.

3. **Optimized Data Structures**: Uses hash maps and sets for O(1) lookups of previously seen pairs.

4. **Specialized Duplicate Handling**: Different strategies for arrays with and without duplicates to optimize performance in both cases.

## Code Structure

- `PairSum`: Class for storing and formatting pairs with their sum
- `EqualSumPairFinder`: Main class implementing the pair-finding algorithm
- `TestEqualSumPairFinder`: Unit tests covering various scenarios
- Command line interface with argument parsing

## Edge Cases Handled

- Empty arrays
- Arrays with fewer than 4 elements (cannot form two distinct pairs)
- Arrays with duplicate elements
- Arrays with both positive and negative numbers

## Testing Approach

The solution includes comprehensive unit tests that verify the algorithm works correctly for different scenarios:

1. Example cases from the problem statement
2. Edge cases (empty arrays, too few elements)
3. Arrays with positive and negative numbers
4. Arrays with multiple different sums
5. Arrays where all elements are the same
6. Arrays with multiple pairs having the same sum

Run all tests with:
```bash
python3 main.py --test
```

## Performance Results

Performance varies depending on the input size:

- Small arrays (<100 elements): Processes in milliseconds
- Medium arrays (1000-5000 elements): Processes in seconds
- Large arrays (>10000 elements): Processing time scales with the square of the input size

The parallel implementation significantly improves performance on multi-core systems, especially for larger inputs.
