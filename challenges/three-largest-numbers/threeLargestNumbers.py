def findThreeLargestNumbers(array):
    x = [float("-inf")] * 3

    for i in array:
        # [previouslyMedian,previouslyLargest,newLargest]
        if i > x[2]:
            x[0] = x[1]
            x[1] = x[2]
            x[2] = i
        # [previouslyMedian,newMedian,Largest]
        elif i > x[1]:
            x[0] = x[1]
            x[1] = i
        # [newSmallest,Median,Largest]
        elif i > x[0]:
            x[0] = i
    return x
        


if __name__ == '__main__':
    a =  [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    answer = findThreeLargestNumbers(a)
    print(answer)
    # answer = [18, 141, 541]