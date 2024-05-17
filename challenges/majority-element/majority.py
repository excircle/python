def majorityElement(ar):
    stats = {}
    for i in ar:
        if i not in stats:
            stats[i] = 1
        else:
            stats[i] += 1
    return sorted(stats.items(), key=lambda item: item[1], reverse=True)[0][0]

def main():
    input = [1, 2, 3, 2, 2, 1, 2]
    answer = majorityElement(input)
    print(answer)

if __name__ == '__main__':
    main()