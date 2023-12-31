def quickSort(a):
    length = len(a)

    if length <= 1:
        return a

    pivot = a.pop()

    lt, gt = [] , []

    for value in a:
        if value < pivot:
            lt.append(value)
        else:
            gt.append(value)

    return quickSort(lt) + [pivot] + quickSort(gt)
        
if __name__ == '__main__':
    input = [27, 7, 30, 19, 15, 16, 3, 26, 29, 2]
    answer = quickSort(input)
    print(answer)