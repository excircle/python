def oneEdit(str1, str2):
    len1, len2 = len(str1), len(str2)
    
    # If there is more than 1 character difference in length, return False
    if abs(len1 - len2) > 1:
        return False

    # Set s1 to be the bigger string, and s2 to be the smaller string
    s1, s2 = (str1, str2) if len1 <= len2 else (str2, str1)
    
    found_difference = False
    i, j = 0, 0
    ls1, ls2 = len(s1), len(s2)

    # While pointers for str1 and str2 are not out of indexes to traverse
    while i < ls1 and j < ls2:
        # Check if the letters are the same
        if s1[i] != s2[j]:
            # If they are not the same, set loop terminator
            if found_difference: 
                return False
            found_difference = True
            if len1 == len2:
                i += 1
        else:
            i += 1
        j += 1
    return True

if __name__ == '__main__':
    answer = oneEdit("hello", "heo")
    print(answer)
