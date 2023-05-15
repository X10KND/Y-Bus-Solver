# Y Bus Solver

## Project Details

This project is made to solve Y Bus Matrix for a given power system.

## Instructions

`input.txt` format:
Number of buses  
Number of rows of data

For each row, specify
(From bus) (To bus) (R in pu) (X in pu) (B in pu)

Example math problem:

![Math](https://raw.githubusercontent.com/X10KND/Y-Bus-Solver/main/Example%20Math.png)

```
5
7
1 2 0.02 0.06 0.06
1 3 0.08 0.24 0.05
2 3 0.06 0.18 0.04
2 4 0.08 0.24 0.05
2 5 0.02 0.06 0.02
3 4 0.01 0.04 0.01
4 5 0.03 0.10 0.04
```

Change the maximum number of decimal points if required.

```python
DECIMAL = 2
```

## Requirements

`pip install pandas`