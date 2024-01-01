def reverseDict(d):
    return { str(v): k for k, v in d.items() }

if __name__ == '__main__':
    x = {
        "a": 4,
        "b": 3,
        "m": 5
    }
    
    print(x)
    answer = reverseDict(x)
    print(answer)
