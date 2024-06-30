import sys

def min_moves(nums):
    total_moves = 0
    nums.sort()
    median = nums[len(nums) // 2]
    for num in nums:
        total_moves += abs(num - median)
    return total_moves

if len(sys.argv) < 2:
    print("Необходимо передать имя файла в качестве аргумента командной строки.")
    sys.exit(1)

file_name = sys.argv[1]

try:
    with open(file_name, 'r') as file:
        nums = [int(line.strip()) for line in file]
except FileNotFoundError:
    print("Файл не найден.")
    sys.exit(1)
except ValueError:
    print("Файл содержит неверные данные.")
    sys.exit(1)

result = min_moves(nums)
print(result)
# python task_4/task_4.py task_4/test_value.txt
