import sys

def count_distinct_values():
    input = sys.stdin.read
    data = input().split()[1:]
    distinct_values = set(data)
    print(len(distinct_values))

count_distinct_values()