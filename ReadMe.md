# [Day 1](./day1)

This script processes an input file containing pairs of numbers, calculates the total distance between two lists of numbers,
and computes a similarity score based on the frequency of numbers in one list.
Functions:

- Reads and processes the input file "day1/input.txt" to extract pairs of numbers.
- Splits each line into two numbers and appends them to `left_numbers` and `right_numbers` lists.
- Sorts the `left_numbers` and `right_numbers` lists.
- Calculates the absolute difference between corresponding elements of the sorted lists.
- Sums the differences to get the total distance between the lists.
- Creates a dictionary to store the counts of each number in the `right_numbers` list.
- Calculates a similarity score by multiplying each number in the `left_numbers` list by its occurrence count in the `right_numbers` list.
  Variables:
- left_numbers (list): List to store the first number of each pair from the input file.
- right_numbers (list): List to store the second number of each pair from the input file.
- diff (list): List to store the absolute differences between corresponding elements of `left_numbers` and `right_numbers`.
- sum_diff (int): Sum of the absolute differences in the `diff` list.
- right_counts (dict): Dictionary to store the counts of each number in the `right_numbers` list.
- similarity_score (int): Total similarity score based on the frequency of numbers in the `right_numbers` list.
  Output:
- Prints the total distance between the lists.
- Prints the total similarity score.
