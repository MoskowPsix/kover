from point import Point
import math
from request_hack import RequestHack


MAX_VELOCITY=10

def move_to_point(position1: Point, position2: Point):
    vector_position: Point = Point(position2.x - position1.x, position2.y - position1.y)
    vector_distance =get_vector_length(vector_position)
    if vector_distance > MAX_VELOCITY:
        k = MAX_VELOCITY/vector_distance
        vector_position = Point(vector_position.x * k, vector_position.y * k)
    return vector_position

def get_vector_length(vector: Point):
    return abs(math.sqrt(vector.x**2 + vector.y**2))