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

The solution implements an optimized algorithm using parallel processing to find pairs with equal sums efficiently.

### Key Features

1. **Object-Oriented Design**: Uses clear class organization with separation of concerns
2. **Parallel Processing**: Leverages multithreading for better performance on large arrays
3. **Adaptive Optimization**: Automatically switches between single-threaded and parallel processing based on input size
4. **Comprehensive Error Handling**: Validates inputs and gracefully handles edge cases
5. **Extensive Testing**: Includes unit tests for various scenarios

### Algorithm

The core algorithm follows these steps:

1. Sort the input array for better performance
2. For arrays with less than 1000 elements:
   - Process using a simple, efficient single-threaded approach
3. For larger arrays:
   - Split the array into chunks and process them in parallel using multiple threads
   - Each thread creates pairs for its assigned portion of the array
   - Results are combined using synchronized data structures

The time complexity is O(n²) in the worst case, but the actual performance is significantly improved through:
- Parallelization
- Early duplicate detection
- Optimized data structures

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

1. **Multithreaded Processing**: For large arrays, the work is distributed across multiple CPU cores using Python's `ThreadPoolExecutor`.

2. **Adaptive Thread Count**: The number of threads is based on the available CPU cores and input size.

3. **Pre-Sorting**: The array is sorted first to improve cache locality and duplicate handling.

4. **Chunk-Based Processing**: Work is divided into optimal-sized chunks to balance thread creation overhead and workload distribution.

5. **Thread Synchronization**: Uses proper locking mechanisms to safely combine results from different threads.

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
