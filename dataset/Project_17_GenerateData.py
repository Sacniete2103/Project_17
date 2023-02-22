import random

def write_test_case_to_file(file_num, N, K, items, cars):
    filename = "{:03d}.txt".format(file_num)
    with open(filename, "w") as f:
        f.write("{} {}\n".format(N, K))
        for item in items:
            f.write("{} {}\n".format(item[0], item[1]))
        for car in cars:
            f.write("{} {}\n".format(car[0], car[1]))

def is_valid_test_case(items, cars):
    total_weight = 0
    for item in items:
        total_weight += item[0]
    for car in cars:
        if total_weight < 1.1 * car[0]:
            return False
    return True

def generate_N(K):
    if K == 2:
        N = random.randint(4, 6)
    else:
        N = random.randint(K ** 2 - K, K ** 2 + K)
    return N
        
def generate_test_case(N, K):    
    items = []
    for i in range(N):
        weight = random.randint(1, 10)
        value = random.randint(1, 10)
        items.append((weight, value))
    cars = []
    for i in range(K):
        lower = random.randint(3 * K, 5 * K)
        upper = random.randint(lower + 3, 7 * K)
        cars.append((lower, upper))
    return items, cars

if __name__ == "__main__":
    #Easy cases
    for i in range(20):
        K = i // 5 + 2
        N = generate_N(K)
        items, cars = generate_test_case(N, K)
        while not is_valid_test_case(items, cars):
            items, cars = generate_test_case(N, K)
        write_test_case_to_file(i + 1, N, K, items, cars)
    
    #Medium cases
    for i in range(6, 16):
        K = i
        N = generate_N(K)
        items, cars = generate_test_case(N, K)
        while not is_valid_test_case(items, cars):
            items, cars = generate_test_case(N, K)
        write_test_case_to_file(15 + i, N, K, items, cars)
    
    #Hard cases
    for i in range (4, 9):
        K = 5 * i
        N = generate_N(K)
        items, cars = generate_test_case(N, K)
        while not is_valid_test_case(items, cars):
            items, cars = generate_test_case(N, K)
        write_test_case_to_file(27+ i, N, K, items, cars)
    
    #Limit_testing
    K = 50
    N = generate_N(K)
    items, cars = generate_test_case(N, K)
    while not is_valid_test_case(items, cars):
        items, cars = generate_test_case(N, K)
    write_test_case_to_file(36, N, K, items, cars)
        
