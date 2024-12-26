def bonAppetit(bill, k, b):
    anna_share = sum( [ x for x in bill if x != bill[k] ] ) // 2
    if b == anna_share:
        print("bon appetit")
    else:
        print( b - anna_share)
    

def main():
    bill = [3, 10, 2, 9]
    skip_index = 1
    annas_contribution = 12
    bonAppetit(bill, skip_index, annas_contribution)

if __name__ == '__main__':
    main()