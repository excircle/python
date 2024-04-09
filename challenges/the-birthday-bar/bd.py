def birthday(s, d, m):
    count = 0
    for i in range(len(s) - m + 1):
        if sum(s[i:i+m]) == d:
            count += 1
    return count

def main():
    s = [1,2,1,3,2]
    d = 3 # adds up to
    m = 2 # using two numbers
    print(birthday(s, d, m))

if __name__ == "__main__":
    main()