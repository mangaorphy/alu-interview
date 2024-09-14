# Minimum Operations to Achieve H Characters

## Project Overview

This project provides a Python implementation for calculating the minimum number of operations needed to produce exactly `n` `H` characters in a text file using two operations: **Copy All** and **Paste**.

## Functionality

The main function, `minOperations(n)`, calculates the fewest number of operations required to get exactly `n` `H` characters. The function returns an integer representing the number of operations, or `0` if it is impossible to achieve `n`.

### Operations

1. **Copy All**: Duplicates the current content of the file.
2. **Paste**: Adds the copied content to the current file.