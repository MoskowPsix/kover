from point import Point
import math
from request_hack import RequestHack

URL = "https://games-test.datsteam.dev/play/magcarp/player/move"
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
  
p1 = Point(500, 100)
p2 = Point(120, 50)
    
print(move_to_point(p1, p2).x)

req = RequestHack()

params = {
    'transports': []
}
print(req.post(params))
