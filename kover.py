class Kover:
    def __init__(self, id: str, acceleration: dict, activate_shield: bool, attack: dict):
        self.id = id
        self.acceleration = acceleration
        self.activate_shield = activate_shield
        self.attack = attack