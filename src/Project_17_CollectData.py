import Project_17_Solver as sol
import time
import csv

def Collect_Backtracking():
    data = []
    for i in range(1, 16):
        N, K, items, cars = sol.read_dataset(i)
        start_time = time.perf_counter()
        best_value, best_solution = sol.Solve_Backtracking(N, K, items, cars)
        runtime = time.perf_counter() - start_time
        data.append([i, best_value, best_solution, runtime])

    with open('..\\collected_data\\backtracking_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['No.', 'Best value', 'Best solution', 'Runtime'])
        for row in data:
            writer.writerow(row)

def Collect_Local_Search():
    data = []
    for i in range (10):
        for j in range(1, 21):
            N, K, items, cars = sol.read_dataset(j)
            start_time = time.perf_counter()
            best_value, best_solution = sol.Solve_Local_Search(N, K, items, cars)
            runtime = time.perf_counter() - start_time
            if best_value == 0:
                best_solution = "NaN"
                runtime = "NaN"
            data.append([i * 20 + j, best_value, best_solution, runtime])

    with open('..\\collected_data\\local_search_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['No.', 'Best value', 'Best solution', 'Runtime'])
        for row in data:
            writer.writerow(row)

def Collect_Iterated_Local_Search():
    data = []
    for i in range(1, 37):
        N, K, items, cars = sol.read_dataset(i)
        start_time = time.perf_counter()
        best_value, best_solution = sol.Solve_Iterated_Local_Search(N, K, items, cars)
        runtime = time.perf_counter() - start_time
        if best_value == 0:
            best_solution = "NaN"
            runtime = "NaN"
        data.append([i, best_value, best_solution, runtime])

    with open('..\\collected_data\\iterated_local_search_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['No.', 'Best value', 'Best solution', 'Runtime'])
        for row in data:
            writer.writerow(row)

def Collect_MIP():
    data = []
    for i in range(1, 37):
        N, K, items, cars = sol.read_dataset(i)
        start_time = time.perf_counter()
        best_value, best_solution = sol.Solve_MIP(N, K, items, cars)
        runtime = time.perf_counter() - start_time
        if best_value == 0:
            best_solution = "NaN"
            runtime = "NaN"
        data.append([i, best_value, best_solution, runtime])

    with open('..\\collected_data\\MIP_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['No.', 'Best value', 'Best solution', 'Runtime'])
        for row in data:
            writer.writerow(row)

def Collect_CP():
    data = []
    for i in range(1, 37):
        N, K, items, cars = sol.read_dataset(i)
        if i == 36:
            time_limit = 3600
        else:
            time_limit = 300
        start_time = time.perf_counter()
        best_value, best_solution = sol.Solve_CP(N, K, items, cars, time_limit)
        runtime = time.perf_counter() - start_time
        if best_value == 0:
            best_solution = "NaN"
            runtime = "NaN"
        data.append([i, best_value, best_solution, runtime])

    with open('..\\collected_data\\CP_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['No.', 'Best value', 'Best solution', 'Runtime'])
        for row in data:
            writer.writerow(row)

Collect_Iterated_Local_Search()
