def get_count_of_neighbors(field, x, y):
    count_of_neighbors = 0

    for neighbor_x in range(x - 1, x + 2):
        for neighbor_y in range(y - 1, y + 2):
            if neighbor_x < 0 or neighbor_y < 0:
                continue
            if neighbor_x >= field.get_width() or \
                    neighbor_y >= field.get_height():
                continue
            if neighbor_x == x and neighbor_y == y:
                continue
            count_of_neighbors += field.get(
                neighbor_x,
                neighbor_y
            )
    return count_of_neighbors
