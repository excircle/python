def missingNumbers(nums):
    not_missing = set(nums)
    missing = []
    for i in range(1, len(nums) + 3):
        if i not in not_missing:
            missing.append(i)
    return missing



def main():
    input = [1]
    answer = missingNumbers(input)
    print(answer)

if __name__ == '__main__':
    main()