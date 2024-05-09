def zeroSumSubarray(nums):
    for k, _ in enumerate(nums):
        mysum = 0
        for v in nums[k:]:
            mysum += v
            if mysum == 0:
                return True
    return False

def main():
    input = [-1, 2, 3, 4, -5, -3, 1, 2]
    answer = zeroSumSubarray(input)
    print(answer)

if __name__ == '__main__':
    main()