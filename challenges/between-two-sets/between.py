def getTotalX(a, b):
    lcm_val = a[0]
    for i in a[1:]:
        d = min(lcm_val, i)
        while i % d != 0 or lcm_val % d != 0:
            d -= 1
        lcm_val = (lcm_val * i) // d

    gcd_val = b[0]
    for num in b[1:]:
        while num:
            gcd_val, num = num, gcd_val % num

    count = 0
    multiple = lcm_val
    while multiple <= gcd_val:
        if gcd_val % multiple == 0:
            count += 1
        multiple += lcm_val

    return count

if __name__ == "__main__":

    a = [100,99,98,97,96,95,94,93,92,91]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    answer = getTotalX(a, b)
    print(answer)
