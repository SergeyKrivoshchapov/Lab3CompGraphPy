from vector import Vector
from ray import Ray
import math

class Camera:
    def __init__(self, position, look_at, up_vector, fov, width, height):
        self.position = position
        self.look_at = look_at
        self.up_vector = up_vector
        self.fov = fov
        self.width = width
        self.height = height
        
        self._calculate_vectors()
    
    def _calculate_vectors(self):
        forward = (self.look_at - self.position).normalize()
        right = forward.cross(self.up_vector).normalize()
        up = right.cross(forward)
        aspect_ratio = self.width / self.height
        plane_height = 2.0 * math.tan(math.radians(self.fov) / 2.0)
        plane_width = plane_height * aspect_ratio
        
        self.forward = forward
        self.right = right
        self.up = up
        self.plane_width = plane_width
        self.plane_height = plane_height
    
    def generate_ray(self, x, y):
        nx = (2.0 * x / self.width - 1.0) * self.plane_width / 2.0
        ny = (1.0 - 2.0 * y / self.height) * self.plane_height / 2.0
        direction = (self.forward + self.right * nx + self.up * ny).normalize()
        
        return Ray(self.position, direction)