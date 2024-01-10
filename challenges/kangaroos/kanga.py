if __name__ == '__main__':
    def kangaroo(x1, v1, x2, v2):
        result = ""
        if (x2 > x1) and (v2 >= v1):
            result = "NO"
        elif (x2 - x1) % (v1 - v2) == 0:
            result = "YES"
        else:
            result = "NO"
        return result
