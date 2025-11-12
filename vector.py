import numpy as np
import math

class Vector:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.data = np.array([x, y, z], dtype=np.float64)
    
    @property
    def x(self):
        return self.data[0]
    
    @property
    def y(self):
        return self.data[1]
    
    @property
    def z(self):
        return self.data[2]
    
    def __add__(self, other):
        return Vector(*(self.data + other.data))
    
    def __sub__(self, other):
        return Vector(*(self.data - other.data))
    
    def __mul__(self, scalar):
        return Vector(*(self.data * scalar))
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def dot(self, other):
        return np.dot(self.data, other.data)
    
    def cross(self, other):
        result = np.cross(self.data, other.data)
        return Vector(*result)
    
    def length(self):
        return np.linalg.norm(self.data)
    
    def normalize(self):
        length = self.length()
        if length > 0:
            return Vector(*(self.data / length))
        return Vector()
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __setitem__(self, index, value):
        self.data[index] = value
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
