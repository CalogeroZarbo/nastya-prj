#!/usr/bin/env python3
"""
Sample application to demonstrate code review standards.
"""

import os
import sys

# Global variable - bad practice
GLOBAL_VAR = "some_value"

def bad_function(input_data):
    """This function has multiple code quality issues."""
    # No docstring
    # No type hints
    # Inefficient approach
    result = []
    for i in range(len(input_data)):
        if input_data[i] > 0:
            result.append(input_data[i] * 2)
    return result

def another_bad_function(a, b):
    # No comments
    # Hardcoded values
    # No error handling
    if a > b:
        return a + b
    else:
        return a - b

class BadClass:
    def __init__(self):
        self.data = []
        
    def add_item(self, item):
        # Inconsistent naming
        self.data.append(item)
        
    def get_items(self):
        return self.data

def main():
    # Magic numbers
    numbers = [1, -2, 3, -4, 5]
    result = bad_function(numbers)
    print(result)
    
    # Using global variable
    print(GLOBAL_VAR)
    
if __name__ == "__main__":
    main()