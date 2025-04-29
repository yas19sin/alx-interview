# 0x02. Minimum Operations

This project contains a Python function `minOperations(n)` that calculates the fewest number of operations needed to result in exactly `n` H characters in a text file, starting with a single H. The only allowed operations are "Copy All" and "Paste".

## Requirements

* Allowed editors: vi, vim, emacs
* Interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
* Files should end with a new line
* The first line of all files should be `#!/usr/bin/python3`
* A `README.md` file at the root of the folder is mandatory
* Code should be documented
* Code should use the PEP 8 style (version 1.7.x)
* All files must be executable

## Function Prototype

```python
def minOperations(n)
```

* Returns an integer representing the minimum number of operations.
* If `n` is impossible to achieve (e.g., `n <= 1`), it returns `0`.

## Example

```
n = 9
H -> Copy All -> Paste -> HH -> Paste -> HHH -> Copy All -> Paste -> HHHHHH -> Paste -> HHHHHHHHH
Number of operations: 6
```

## Usage

```bash
./0-main.py
```

## Files

* `0-minoperations.py`: Contains the implementation of the `minOperations` function.
* `0-main.py`: Main file used for testing the function.
* `README.md`: This file.
