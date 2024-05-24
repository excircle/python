'''
Write a function which scans the integers in multiple arrays using a 'spiral' method
Correct Answer: [19, 32, 33, 34, 25, 8, 11, 9, 6, 7, 10, 27, 28, 29, 30, 17, 20, 1, 18, 16, 15, 14, 13, 12, 26, 5, 24, 23, 22, 21, 2, 31, 36, 35, 4, 3]
  "array": [
    [19, 32, 33, 34, 25, 8],
    [16, 15, 14, 13, 12, 11],
    [18, 31, 36, 35, 26, 9],
    [1, 2, 3, 4, 5, 6],
    [20, 21, 22, 23, 24, 7],
    [17, 30, 29, 28, 27, 10]
  ]
'''
def spiralTraverse(ar):
    results = []
    modes = ['a', 'b', 'c', 'd']
    while len(ar) > 0:
        for mode in modes:
            # Mode A
            if mode == 'a':
                results += ar.pop(0)
                continue
            
            # Mode B
            if mode == 'b':
                for l in ar:
                    results.append(l.pop(-1))
                continue

            # Mode C
            if mode == 'c':
                results += ar.pop(-1)[::-1]
                continue

            # Mode D
            if mode == 'd':
                a = [x for x in range(1, len(ar))]
                for l in a[::-1]:
                    results.append(ar[l].pop(0))
    return results


def main():
    # array = [
    #     [19, 32, 33, 34, 25, 8],
    #     [16, 15, 14, 13, 12, 11],
    #     [18, 31, 36, 35, 26, 9],
    #     [1, 2, 3, 4, 5, 6],
    #     [20, 21, 22, 23, 24, 7],
    #     [17, 30, 29, 28, 27, 10]
    # ]
    array = [
      [1, 2, 3],
      [8, 9, 4],
      [7, 6, 5]
    ]
    answer = spiralTraverse(array)
    print(answer)
    return None

if __name__ == '__main__':
    main()