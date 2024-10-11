class Kover:
    def __init__(self, id: str, acceleration: dict, activate_shield: bool, attack: dict):
        self.id = id
        self.acceleration = acceleration
        self.activate_shield = activate_shield
        self.attack = attack
    
    def to_json(self):
        return {
            "acceleration": {
                "x": self.acceleration.x,
                "y": self.acceleration.y
            },
            "activateShield": self.activate_shield,
            "attack": self.attack
        }