#!/usr/bin/env python3
"""
Find Pairs with Equal Sum

This module provides functionality to find all unique pairs in an unsorted array that have the same sum.
Given an array of integers, it identifies and groups pairs of numbers that add up to the same value.

Example:
    $ python find_pairs_with_equal_sum.py --array 6 4 12 10 22 54 32 42 21 11
    Pairs : ( 6, 10) ( 4, 12) have sum : 16

Note: Assuming array can have duplicate values because in description it is not mentioned
"""

from typing import List, Dict, Tuple, Set
import argparse
import time
import sys
import os
import logging
import unittest
from collections import defaultdict
from dataclasses import dataclass

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class PairSum:
    """Class for storing pairs with their sum value."""
    pairs: List[Tuple[int, int]]
    sum_value: int

    def __str__(self) -> str:
        """Format the pairs and their sum in the required output format."""
        pairs_str = " ".join(f"( {a}, {b})" for a, b in self.pairs)
        return f"Pairs : {pairs_str} have sum : {self.sum_value}"


class EqualSumPairFinder:
    """Class for finding pairs with equal sum in an array."""

    def __init__(self, array: List[int]):
        """Initialize with the input array.
        
        Args:
            array: List of integers to analyze
        """
        self.array = array
        self._validate_input()

    def _validate_input(self) -> None:
        """Validate the input array.
        
        Raises:
            ValueError: If the array is not valid for processing
        """
        if not isinstance(self.array, list):
            raise ValueError("Input must be a list")
        
        if not all(isinstance(item, int) for item in self.array):
            raise ValueError("All elements in the array must be integers")
    
    def find_pairs_two_sum(self) -> Dict[int, List[Tuple[int, int]]]:
        """Find all unique pairs with equal sum using a Two-Sum based approach.
        
        This implementation first creates all possible pairs and directly stores them
        by their sum value, which can be more efficient by avoiding redundant sum calculations
        and reducing branch logic.
        
        Returns:
            Dictionary mapping sum values to lists of pairs that have that sum
        """
        if len(self.array) < 4:
            logger.debug("Array has fewer than 4 elements, cannot form two pairs")
            return {}
        
        start_time = time.time()
        
        # Sort the array for better performance with duplicates
        sorted_array = sorted(self.array)
        has_duplicates = len(sorted_array) != len(set(sorted_array))
        
        sum_pairs = defaultdict(list)
        seen_pairs = set()
        
        for i in range(len(sorted_array)):
            for j in range(i + 1, len(sorted_array)):
                a, b = sorted_array[i], sorted_array[j]
                current_sum = a + b
                
                if has_duplicates:
                    # Track pairs by index when handling duplicates
                    pair_id = (i, j)
                    if pair_id in seen_pairs:
                        continue
                    seen_pairs.add(pair_id)
                    sum_pairs[current_sum].append((a, b))
                else:
                    pair = (min(a, b), max(a, b))
                    if pair in seen_pairs:
                        continue
                    seen_pairs.add(pair)
                    sum_pairs[current_sum].append(pair)
        
        result = {s: pairs for s, pairs in sum_pairs.items() if len(pairs) >= 2}
        
        end_time = time.time()
        logger.debug(f"Processing completed in {end_time - start_time:.6f} seconds")
        return result
        
    def find_pairs_optimized(self) -> Dict[int, List[Tuple[int, int]]]:
        """Find all unique pairs with equal sum.
        
        Delegates to the Two-Sum based implementation, which has proven to be efficient.
        
        Returns:
            Dictionary mapping sum values to lists of pairs that have that sum
        """
        return self.find_pairs_two_sum()
    
    def get_formatted_results(self) -> List[PairSum]:
        """Get the results formatted as PairSum objects.
        
        Returns:
            List of PairSum objects sorted by sum value
        """
        results = self.find_pairs_optimized()
        return [
            PairSum(pairs=pairs, sum_value=sum_val)
            for sum_val, pairs in sorted(results.items())
        ]


def print_results(results: List[PairSum]) -> None:
    """Print the PairSum results.
    
    Args:
        results: List of PairSum objects to print
    """
    if not results:
        print("No pairs with equal sum found.")
        return
    
    for pair_sum in results:
        print(str(pair_sum))


def process_array(array: List[int], verbose: bool = False) -> None:
    """Process an array and print pairs with equal sum.
    
    Args:
        array: List of integers to process
        verbose: Whether to enable verbose logging
    """
    if verbose:
        logger.setLevel(logging.DEBUG)
    
    try:
        finder = EqualSumPairFinder(array)
        results = finder.get_formatted_results()
        print_results(results)
    except ValueError as e:
        logger.error(f"Error processing array: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        sys.exit(1)


class TestEqualSumPairFinder(unittest.TestCase):
    """Unit tests for the EqualSumPairFinder class."""

    def test_example_1(self):
        """Test with the first example from the problem statement."""
        array = [6, 4, 12, 10, 22, 54, 32, 42, 21, 11]
        finder = EqualSumPairFinder(array)
        results = finder.find_pairs_optimized()
        
        self.assertIn(16, results)
        self.assertEqual(len(results[16]), 2)
        
        pairs_with_sum_16 = results[16]
        self.assertIn((4, 12), pairs_with_sum_16)
        self.assertIn((6, 10), pairs_with_sum_16)

    def test_example_2(self):
        """Test with the second example from the problem statement."""
        array = [4, 23, 65, 67, 24, 12, 86]
        finder = EqualSumPairFinder(array)
        results = finder.find_pairs_optimized()
        
        self.assertIn(90, results)
        pairs_with_sum_90 = results[90]
        self.assertIn((4, 86), pairs_with_sum_90)
        self.assertIn((23, 67), pairs_with_sum_90)

    def test_empty_array(self):
        """Test with an empty array."""
        finder = EqualSumPairFinder([])
        results = finder.find_pairs_optimized()
        self.assertEqual(results, {})

    def test_too_few_elements(self):
        """Test with an array having fewer than 4 elements."""
        finder = EqualSumPairFinder([1, 2, 3])
        results = finder.find_pairs_optimized()
        self.assertEqual(results, {})
        
    def test_positive_and_negative_numbers(self):
        """Test with an array containing both positive and negative numbers."""
        array = [10, -8, 6, -4, 2, 5, 3, -5]
        finder = EqualSumPairFinder(array)
        results = finder.find_pairs_optimized()
        
        self.assertIn(2, results)
        self.assertEqual(len(results[2]), 2)
        self.assertIn((-8, 10), results[2])
        self.assertIn((-4, 6), results[2])
        
        self.assertIn(8, results)
        self.assertGreaterEqual(len(results[8]), 2)
        
    def test_multiple_different_sums(self):
        """Test with an array having multiple pairs with different equal sums."""
        array = [3, 5, 7, 8, 9, 10, 12, 14]
        finder = EqualSumPairFinder(array)
        results = finder.find_pairs_optimized()
        
        self.assertIn(15, results)
        self.assertGreaterEqual(len(results[15]), 2)
        self.assertIn((3, 12), results[15])
        self.assertIn((5, 10), results[15])
        
        self.assertIn(17, results)
        self.assertGreaterEqual(len(results[17]), 2)
        self.assertIn((3, 14), results[17])
        self.assertIn((8, 9), results[17])
        
        self.assertGreaterEqual(len(results), 2)

    def test_all_same_elements(self):
        """Test with an array where all elements are the same."""
        finder = EqualSumPairFinder([5, 5, 5, 5])
        results = finder.find_pairs_optimized()
        self.assertIn(10, results)

    def test_multiple_pairs_same_sum(self):
        """Test with multiple pairs having the same sum."""
        finder = EqualSumPairFinder([1, 2, 3, 4, 5, 6, 7, 8])
        results = finder.find_pairs_optimized()
        self.assertIn(9, results)
        self.assertEqual(len(results[9]), 4)


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments.
    
    Returns:
        Parsed command line arguments
    """
    parser = argparse.ArgumentParser(
        description='Find pairs with equal sum in an array',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '--array', '-a', 
        nargs='+', 
        type=int,
        help='Array of integers (space-separated)'
    )
    parser.add_argument(
        '--file', '-f',
        type=str,
        help='Path to a file containing integers (one per line)'
    )
    parser.add_argument(
        '--test', '-t',
        action='store_true',
        help='Run unit tests instead of processing input'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging'
    )
    parser.add_argument(
        '--example', '-e',
        type=int,
        choices=[1, 2],
        help='Run with example 1 or 2 from the problem statement'
    )
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    if args.test:
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
        return
    
    example_arrays = {
        1: [6, 4, 12, 10, 22, 54, 32, 42, 21, 11],
        2: [4, 23, 65, 67, 24, 12, 86]
    }
    
    array = None
    already_processed = False
    
    if args.example is not None:
        array = example_arrays[args.example]
        print(f"\nRunning Example {args.example}:")
        print(f"Input: A[] = {array}")
        print("Output:")
        process_array(array, args.verbose)
        already_processed = True
        
    elif args.array:
        array = args.array
    
    elif args.file:
        try:
            with open(args.file, 'r') as f:
                array = [int(line.strip()) for line in f if line.strip()]
        except (IOError, ValueError) as e:
            logger.error(f"Error reading from file: {e}")
            sys.exit(1)
    
    else:
        print("\n--- Examples from Problem Statement ---")
        
        for idx, example_array in example_arrays.items():
            print(f"\nExample {idx}:")
            print(f"Input: A[] = {example_array}")
            print("Output:")
            process_array(example_array, args.verbose)
        
        print("\n--- Additional Test Cases ---")
        additional_tests = [
            [],
            [1, 2, 3],
            [5, 5, 5, 5],
            [1, 2, 3, 4, 5, 6, 7, 8]
        ]
        
        for i, test_array in enumerate(additional_tests):
            print(f"\nTest Case {i+1}: {test_array}")
            process_array(test_array, args.verbose)
        
        return
    
    # Only process if we haven't already done so
    if array is not None and not already_processed:
        process_array(array, args.verbose)


if __name__ == "__main__":
    main()
