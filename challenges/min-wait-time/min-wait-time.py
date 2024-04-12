def minimumWaitingTime(queries):
    # [1,2,2,3,6]
    queries.sort()
    total = 0
    for k, v in enumerate(queries):
        total += v * len(queries[k+1:])
    return total

def main():
    x = [3, 2, 1, 2, 6]
    results = minimumWaitingTime(x)
    print(results)

if __name__ == '__main__':
    main()
