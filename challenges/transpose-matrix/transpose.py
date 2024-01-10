def transposeMatrix(matrix):
    x = [ [], [], [] ]

    for array in matrix:
        for k, value in enumerate(array):
            x[k].append(value)
    return x


if __name__ == '__main__':

    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    answer = transposeMatrix(matrix)
    print("[")
    for i in answer:
        print("  ", f'{i},')
    print("]")

'''
Expected Output:
[
  [1, 4],
  [2, 5],
  [3, 6]
]'''    