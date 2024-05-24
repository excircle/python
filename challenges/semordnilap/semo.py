def semordnilap(words):
    results = []
    if len(words) < 1:
        return results
    while len(words) > 0:
        check = words.pop()
        reverse = ''.join(list(check)[::-1])
        if reverse in words:
            results.append( [check, reverse] )
            words.remove(reverse)
    return results



def main():
    input = ["dog", "hello", "desserts", "test", "god", "stressed"]
    answer = semordnilap(input) # 
    print(answer)

if __name__ == '__main__':
    main()