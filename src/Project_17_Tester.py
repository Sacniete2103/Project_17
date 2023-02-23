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

'''N, K = [int(x) for x in input().split()] #number of customers and cars
items = [] #list of items
cars = [] #list of capacities

#read input
for i in range(N):
    d, c = input().split()
    items.append([int(d), int(c)])
for k in range(int(K)):
    c1, c2 = input().split()
    cars.append([int(c1), int(c2)])'''