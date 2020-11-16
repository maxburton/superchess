from project.main.coord import Coord


def cardinal(dist=1):
    return [Coord(0, dist), Coord(0, -dist), Coord(dist, 0), Coord(-dist, 0)]


def diagonal(dist=1):
    return [Coord(dist, dist), Coord(dist, -dist), Coord(-dist, dist), Coord(-dist, -dist)]


def directional_range(min, max, unit):
    return list(map(lambda i: unit.scalar_multiply(i), range(min, max+1)))


def combine(list1, list2):
    combined = set()
    for move1 in list1:
        for move2 in list2:
            combined_move = move1.add(move2)
            if not combined_move == Coord(0, 0):
                combined.add(combined_move)
    return list(combined)
