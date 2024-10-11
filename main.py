from point import Point


def move_to_point(position1: Point, position2: Point):
    vector_position: Point = Point(position2.x - position1.x, position2.y - position1)
    
