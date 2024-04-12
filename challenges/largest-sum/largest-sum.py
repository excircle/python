def largestRange(arr):
    arr = list(set(arr))
    arr.sort()
    s, p, e = 0, 0, 1
    stats = []
    while e < len(arr):
        end, previous = arr[e], arr[p]
        if  end == previous + 1:
            e += 1
            p += 1
            continue
        else:
            stats.append(arr[s:e])
            s = e
            p = e
            e = e+1
    else:
        stats.append(arr[s:e])
    stats = sorted(stats, key=len)[::-1][0]
    return [ stats[0], stats[-1] ]


def main():
    x = [19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]
    results = largestRange(x)
    print(results)

if __name__ == '__main__':
    main()