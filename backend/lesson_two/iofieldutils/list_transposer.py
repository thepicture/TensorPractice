def transpose(list_):
    """Transposes the given list as if it was
    rotated by -45 degrees.
    """
    result = list()
    list_width = len(list_[0])
    list_height = len(list_)
    for x in range(list_width):
        row = list()
        for y in range(list_height):
            row.append(list_[y][x])
        print()
        result.append(row)

    return result
