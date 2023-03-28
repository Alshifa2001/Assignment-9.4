

def convert_to_positive(coordinates):
    min_x = min([c[0] for c in coordinates])
    min_y = min([c[1] for c in coordinates])
    new_coordinates = [(c[0] + abs(min_x), c[1] + abs(min_y)) for c in coordinates]
    return new_coordinates
