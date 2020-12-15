# ===== ADVENT OF CODE 2020 =====

# Day 1 SOLUTION

data = [int(line) for line in open('day1.dat','r').readlines()]

# PART 1

def part1(arr):
    for i in arr:
        for j in arr:
            if (i+j==2020):
                return i*j

def part2(arr):
    for i in arr:
        for j in arr:
            for y in arr:
                if (i+j+y==2020):
                    return i*j*y

print("Part 1:", part1(data))
print("Part 2:", part2(data))