def divisibleSumPairs(n, k, ar):
    count = 0
    for pointer, val in enumerate(ar):
        for i in ar[pointer+1:]:
            if (val + i) % k == 0:
                count += 1
    return count

def main():
    n = 6
    k = 3
    ar = [1,3,2,6,1,2]
    answer = divisibleSumPairs(n, k, ar)
    print(answer)

if __name__ == "__main__":
    main()