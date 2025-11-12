class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()
    
    def point_at_parameter(self, t):
        return self.origin + self.direction * t
    
    def __repr__(self):
        return f"Ray(origin={self.origin}, direction={self.direction})"