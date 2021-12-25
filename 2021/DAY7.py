with open('07.txt') as file:
    nums = [int(x) for line in file.readlines() for x in line.split(',')]
    nums.sort()

median = nums[len(nums)//2]
fuel_part_1 = sum((abs(median - num) for num in nums))
print(f'DAY 7 | PART 1: {fuel_part_1}')

avg = sum(nums)/len(nums)
lower, upper = int(avg), int(avg) + 1
fuel1 = sum(sum(range(1, abs(lower - num) + 1)) for num in nums)
fuel2 = sum(sum(range(1, abs(upper - num) + 1)) for num in nums)

# fuel = sum(sum(range(1, abs(avg - num) + 1)) for num in nums)
# fuel = sum(map(lambda x: (abs(avg - x) * (abs(avg - x) + 1)) / 2, nums))
print(f'DAY 7 | PART 2: {fuel1 if fuel1 < fuel2 else fuel2}')