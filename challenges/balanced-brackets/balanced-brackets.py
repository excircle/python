# [ '{', '[', '(', ']', ']', '}' ]
#                   ↑
# [ '{', '[', '(' ]

def isBalanced(b):
    q = []
    bmap = { 
        "{":"}",
        "[":"]",
        "(": ")"
    }
    balanced = True

    for bracketset in b:
        started = None
        for bracket in bracketset:
            if started == None:
                q.append(bracket)
                started = True
                continue
            elif len(q) > 0:
                if bracket == bmap[q[-1]]:

                
    return None
    
if __name__ == '__main__':
    brackets = [list("{[(])}"), list("{[()[]}"), list("{{[[(())]]}}")]
    answer = isBalanced(brackets)
    print(answer)