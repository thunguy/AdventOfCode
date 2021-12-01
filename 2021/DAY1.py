file = open('depths.txt', 'r')
lines = file.readlines()
depths = [int(l) for l in lines]

def get_increases1():
    count = 0
    for i in range(len(depths) - 1):
        if depths[i] < depths[i + 1]:
            count += 1
    return count

def get_increases2():
    count, prev = 0, sum(depths[:3])
    for i in range(1, len(depths) - 2):
       curr = sum(depths[i:i+3])
       if curr > prev: count += 1
       prev = curr
    return count