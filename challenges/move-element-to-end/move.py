def moveElementToEnd(array, toMove):
    n = [x for x in array if x != toMove]
    count = array.count(toMove)
    return array.extend([toMove for i in range(count)])


if __name__ == '__main__':
	a = [2,1,2,2,2,3,4,2]
	m = 2
	answer = moveElementToEnd(a, m)
