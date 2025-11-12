import math
from vector import Vector
from ray import Ray

class Sphere:
    def __init__(self, center, radius, color, specular=0.5, reflection=0.2):
        self.center = center
        self.radius = radius
        self.color = color
        self.specular = specular 
        self.reflection = reflection 
    
    def intersect(self, ray):
        oc = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = 2.0 * oc.dot(ray.direction)
        c = oc.dot(oc) - self.radius * self.radius
        
        discriminant = b * b - 4 * a * c
        
        if discriminant < 0:
            return None
        
        sqrt_d = math.sqrt(discriminant)
        t1 = (-b - sqrt_d) / (2.0 * a)
        t2 = (-b + sqrt_d) / (2.0 * a)
        
        if t1 > 0.001:
            return t1
        elif t2 > 0.001:
            return t2
        else:
            return None
    
    def normal(self, point):
        return (point - self.center).normalize()