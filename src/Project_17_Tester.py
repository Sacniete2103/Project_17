import Project_17_Solver as sol
#N, K = [8, 3] #number of customers and cars
#items = [[3, 5], [6, 3], [2, 5], [5, 5], [3, 4], [4, 3], [4, 6], [2, 1]] #list of items
#cars = [[10, 14], [6, 7], [7, 8]] #list of capacities
'''Solution: [[1 1 0 0 1 0 0 1] or [1,1,2,2,1,3,3,1]
             [0 0 1 1 0 0 0 0]
             [0 0 0 0 0 1 1 0]]'''

'''N, K = [3, 1]
items = [[1,5],[2,6],[5,7]]
cars = [[1,4]]'''
import numpy as np
import random
import copy

N, K, items, cars = sol.read_dataset(4)

def is_valid_state(N, K, state, items, cars):
    weight = [0]*len(cars)
    for i in range(len(items)):
        if state[i] != 0:
            weight[state[i]-1] += items[i][0]
    for j in range(len(cars)):
        if weight[j] < cars[j][0] or weight[j] > cars[j][1]:
            return False
    return True

def get_value(state, items):
    value = 0
    for i in range(len(items)):
        if state[i] != 0:
            value += items[i][1]
    return value

def generate_random_state(N, K):
    return [random.choice(range(K+1)) for j in range(N)]

def Solve_Local_Search(N, K, items, cars):
    current_state = generate_random_state(N, K)
    best_value = 0    
    best_state = [0] * N
    if is_valid_state(N, K, current_state, items, cars):
        best_value = get_value(current_state, items)
    while True:
        best_neighbor_value = 0
        best_neighbor_state = copy.deepcopy(current_state)
        for i in range(N): 
            neighbor_state = copy.deepcopy(current_state)        
            if neighbor_state[i] != K:
                neighbor_state[i] += 1
            else:
                neighbor_state[i] = 0
            if is_valid_state(N, K, neighbor_state, items, cars):
                if get_value(neighbor_state, items) > best_neighbor_value:
                    best_neighbor_value = get_value(neighbor_state, items)
                    best_neighbor_state = copy.deepcopy(neighbor_state)
        if best_neighbor_value > best_value:
            best_value = best_neighbor_value
            current_state = copy.deepcopy(best_neighbor_state)
            best_state = copy.deepcopy(best_neighbor_state)
        else:
          break
    return best_value, best_state

def Solve_Iterated_Local_Search(N, K, items, cars, iterations = 1000):
    current_state = generate_random_state(N, K)
    best_value = 0  
    best_state = [0] * N
    max_value = sum([i[1] for i in items])
    if is_valid_state(N, K, current_state, items, cars):
        best_value = get_value(current_state, items)
    for iteration in range(iterations):
        while True:
            best_neighbor_value = 0
            best_neighbor_state = copy.deepcopy(current_state)
            for i in range(N):        
                neighbor_state = copy.deepcopy(current_state)        
                if neighbor_state[i] != K:
                    neighbor_state[i] += 1
                else:
                    neighbor_state[i] = 0
                if is_valid_state(N, K, neighbor_state, items, cars):
                    if get_value(neighbor_state, items) > best_neighbor_value:
                        best_neighbor_value = get_value(neighbor_state, items)
                        best_neighbor_state = copy.deepcopy(neighbor_state)
            if best_neighbor_value > best_value:
                best_value = best_neighbor_value
                current_state = copy.deepcopy(best_neighbor_state)
                best_state = copy.deepcopy(best_neighbor_state)
            else:
                break
        if best_value == max_value:
            break
        current_state = generate_random_state(N, K)        
    print(iteration)
    return best_value, best_state
 
print(Solve_Iterated_Local_Search(N, K, items, cars, 100))