def max_customers(n, customers):
    arrivals = []
    departures = []

    for arrival, leaving in customers:
        arrivals.append(arrival)
        departures.append(leaving)

    arrivals.sort()
    departures.sort()

    max_customers = 0
    current_customers = 0
    i = 0
    j = 0


    while i < n and j < n:
        if arrivals[i] < departures[j]:
            current_customers += 1
            max_customers = max(max_customers, current_customers)
            i += 1
        else:
            current_customers -= 1
            j += 1

    return max_customers


import sys

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
customers = [tuple(map(int, line.split())) for line in data[1:n + 1]]


result = max_customers(n, customers)
print(result)
