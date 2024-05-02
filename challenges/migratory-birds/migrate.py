# Import below sources "huge_bird_list.py" for a list containing 100k+ values
from huge_bird_list import huge_list

def migratoryBirds(s):
    # Create 'count' dict to hold sighting counts
    count = {}
    for id in s:
        if id in count.keys():
            count[id] += 1
        else:
            count[id] = 1
    
    # Obtain highest sighting value
    maxed = max(count.values())

    # Create a new dict of all IDs with "maxed" sighting value
    winners = { x[0]: x[1] for x in count.items() if x[1] == maxed }

    #return lowest valued ID 
    return min(winners.keys())
    

def main():
    # s = [1,2,3,4,5,4,3,2,1,3,4]
    # answer = migratoryBirds(s)
    answer = migratoryBirds(huge_list)
    print(answer)

if __name__ == '__main__':
    main()