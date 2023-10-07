import numpy as np

def find_missing_numbers(numbers):
  """Finds the missing numbers in a list of numbers.

  Args:
    numbers: A list of numbers.

  Returns:
    A list of missing numbers.
  """

  # Get the minimum and maximum values in the list.
  min_value = min(numbers)
  max_value = max(numbers)

  # Create a range of values between the minimum and maximum values.
  expected_numbers = np.arange(min_value, max_value + 1)

  # Find the missing numbers by subtracting the list of expected numbers from the list of given numbers.
  missing_numbers = np.setdiff1d(expected_numbers, numbers)

  return missing_numbers
