import sys


def circular_path(n: int, m: int) -> list[int]:
    circular_array = list(range(1, n + 1))
    path = []
    current_index = 0

    while True:
        path.append(circular_array[current_index])
        if len(path) > 1 and path[0] == path[-1]:
            break
        current_index = (current_index + m - 1) % n

    return path[:-1]


if __name__ == "__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    result = circular_path(n, m)
    print(''.join(map(str, result)))
# python task_1/task_1.py 4 3