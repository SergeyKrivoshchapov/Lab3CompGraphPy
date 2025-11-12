from vector import Vector

class Light:
    def __init__(self, position, intensity, color=Vector(1.0, 1.0, 1.0)):
        self.position = position
        self.intensity = intensity
        self.color = color
    
    def get_direction(self, point):
        return (self.position - point).normalize()
    
    def get_distance(self, point):
        return (self.position - point).length()