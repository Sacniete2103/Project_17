# Project_17

A Fundamental of Optimization school project about Bin packing with lower bound, upper bound.

## Overview

### `src` folder
`src` folder contains different modules, all written in Python. 

`Project_17_Solver.py` module contains functions that allow you input data then solve it using different methods.

`Project_17_CollectData.py` module contains functions that solve the test cases, record the time taken and store them in a `.csv` file.

### `dataset` folder

Contains the datasets used to test run the program.

`Project_17_GenerateData.py` module contains functions that allow you to generate test cases.

### `collected_data` folder

Contains all the data collected by the program.

### `presentation` folder

Contains the slide used for presentation.

### `report` folder

Contains the report file.

## Usage

First, create a new python script in the same directory as the modules.

### The `Project_17_Solver` module

To use, import the module.

```python
import Project_17_Solver as sol
```

We use five different methods to solve the problem:
+ Backtracking
+ Hill climbing
+ Iterated local search
+ MIP model
+ CP model

The number of items N and cars K are integers, and the items' weight and value, the cars' lower bound and upper bound for capacity will be stored as a list of lists. You can input them by hand:
```
N, K = [8, 3] #number of customers and cars
items = [[3, 5], [6, 3], [2, 5], [5, 5], [3, 4], [4, 3], [4, 6], [2, 1]] #list of items
cars = [[10, 14], [6, 7], [7, 8]] #list of capacities
```

`Solve_Backtracking` solves using backtracking.
```python
best_value, best_sol = sol.Solve_Backtracking(N, K, items, cars)
```

`Solve_Local_Search` solves using hill climbing.
```python
best_value, best_sol = sol.Solve_Local_Search(N, K, items, cars)
```

`Solve_Iterated_Local_Search` solves using iterated local search. This function has an additional optional parameter `iterations` to determine the number of iterations.
```python
best_value, best_sol = sol.Solve_Iterated_Local_Search(N, K, items, cars, iterations)
```

`Solve_MIP` solves using MIP model. This function has an additional optional parameter `time_limit` to determine the time limitation.
```python
best_value, best_sol = sol.Solve_MIP(N, K, items, cars, time_limit)
```

`Solve_CP` solves using CP model. This function has an additional optional parameter `time_limit` to determine the time limitation.
```python
best_value, best_sol = sol.Solve_CP(N, K, items, cars, time_limit)
```

All the functions return the best value and the best solution in the form of a list with N elements showing which item is appointed to which car.

There is also a ultility function to print the result:
```python
sol.Print_Result(best_value, best_sol, N, K)
```

An example program:

```python
import Project_17_Solver as sol
N, K = [8, 3]
items = [[3, 5], [6, 3], [2, 5], [5, 5], [3, 4], [4, 3], [4, 6], [2, 1]]
cars = [[10, 14], [6, 7], [7, 8]]
best_value, best_sol = sol.Solve_Backtracking(N, K, items, cars)
sol.Print_Result(best_value, best_sol, N, K)
```

Output:

```python
Total packed value is: 32
Car 1:
Item 1
Item 2
Item 5
Item 8
Car 2:
Item 3
Item 4
Car 3:
Item 6
Item 7
```

### The `Project_17_CollectData` module

To use, import the module
```python
import Project_17_CollectData
```

`Collect_Backtracking`, `Collect_Local_Search`, `Collect_Iterated_Local_Search`, `Collect_MIP` and `Collect_CP` collect runtime for backtracking, hill climbing, iterated local search, MIP model and CP model respectively.

The collected data is written in a `.csv` file in the `collected_data` folder.



