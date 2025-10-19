# tuple_challenge.py

coordinates = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
sum_x = sum_y = sum_z = 0
n = len(coordinates)
for coord in coordinates:
    sum_x += coord[0]
    sum_y += coord[1]
    sum_z += coord[2]
avg_x = sum_x / n
avg_y = sum_y / n
avg_z = sum_z / n
print(f"Average coordinates: ({avg_x}, {avg_y}, {avg_z})")
