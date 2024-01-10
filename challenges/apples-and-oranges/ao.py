def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count, orange_count = 0, 0

    for apple in apples:
        location = a + apple
        if s <= location <= t:
            apple_count += 1
    for orange in oranges:
        location = b + orange
        if s <= location <= t:
            orange_count += 1
    return apple_count, orange_count

if __name__ == '__main__':
    s = 7   # starting point of Sam's house location.
    t = 11  # ending location of Sam's house location.

    a = 5   # location of the Apple tree (left).
    b = 15  # location of the Orange tree (right).

    apples = [-2, 2, 1] # integer array, distances at which each apple falls from the tree.
    oranges = [5, -6]    # integer array, distances at which each orange falls from the tree.

    answer = countApplesAndOranges(s, t, a, b, apples, oranges)

    print(answer)

