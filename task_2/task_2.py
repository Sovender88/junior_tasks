import sys
import math

def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        line = file.readline().strip().split()
        center_x, center_y = float(line[0]), float(line[1])
        radius = float(file.readline().strip())
        return center_x, center_y, radius

def read_points_data(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points

def point_position(center_x, center_y, radius, point):
    dist = math.sqrt((point[0] - center_x)**2 + (point[1] - center_y)**2)
    if math.isclose(dist, radius):
        return 0
    elif dist < radius:
        return 1
    else:
        return 2

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python point_position.py circle_data.txt points_data.txt')
    else:
        center_x, center_y, radius = read_circle_data(sys.argv[1])
        points = read_points_data(sys.argv[2])

        for point in points:
            pos = point_position(center_x, center_y, radius, point)
            print(pos)
# python task_2/task_2.py task_2/circle_data.txt task_2/points_data.txt