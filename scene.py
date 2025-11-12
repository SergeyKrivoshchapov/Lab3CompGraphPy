import random
import math
from sphere import Sphere
from vector import Vector
from light import Light
from ray import Ray

class Scene:
    def __init__(self):
        self.spheres = []
        self.lights = []
        self.background_color = Vector(0, 0, 1)      
    def add_sphere(self, sphere):
        self.spheres.append(sphere)
    
    def add_light(self, light):
        self.lights.append(light)
    
    def create_random_scene(self, num_spheres = 10):
        light = Light(Vector(-2, 6, 0), 1.0)
        self.add_light(light)
        
        colors = [ Vector(1.0, 0.0, 0.0), Vector(0.0, 1.0, 0.0), Vector(0.0, 0.5, 1.0), Vector(1.0, 1.0, 0.0), Vector(1.0, 0.0, 1.0), Vector(0.0, 1.0, 1.0), ]
        
        for i in range(num_spheres):
            center = Vector(
                random.uniform(-5, 5),
                random.uniform(-3, 4),
                random.uniform(2, 6)
            )
            radius = random.uniform(0.3, 0.5)
            color = random.choice(colors)
            specular = random.uniform(0.6, 0.8)
            
            sphere = Sphere(center, radius, color, specular)
            self.add_sphere(sphere)
    
    def find_closest_intersection(self, ray):
        closest_t = float('inf')
        closest_sphere = None
        
        for sphere in self.spheres:
            t = sphere.intersect(ray)
            if t is not None and t < closest_t:
                closest_t = t
                closest_sphere = sphere
        
        return closest_sphere, closest_t
    
    def is_in_shadow(self, point, light):
        shadow_ray = Ray(point + light.get_direction(point) * 0.001, light.get_direction(point))
        
        for sphere in self.spheres:
            t = sphere.intersect(shadow_ray)
            if t is not None and t < light.get_distance(point):
                return True
        
        return False
    
    def compute_lighting(self, point, normal, view_direction, sphere):
        total_intensity = Vector(0.1, 0.1, 0.1)  
        
        for light in self.lights:
            light_dir = light.get_direction(point)
            diffuse_intensity = max(0.0, normal.dot(light_dir))
            
            #phong
            reflect_dir = (normal * 2.0 * normal.dot(light_dir) - light_dir).normalize()
            specular_intensity = max(0.0, reflect_dir.dot(view_direction))
            specular_intensity = pow(specular_intensity, 50) * sphere.specular              
            if not self.is_in_shadow(point, light):
                light_effect = Vector(
                    diffuse_intensity + specular_intensity,
                    diffuse_intensity + specular_intensity,
                    diffuse_intensity + specular_intensity
                ) * light.intensity
                
                total_intensity = Vector(
                    total_intensity.x + light_effect.x,
                    total_intensity.y + light_effect.y,
                    total_intensity.z + light_effect.z
                )
        
        final_color = Vector(
            sphere.color.x * total_intensity.x,
            sphere.color.y * total_intensity.y,
            sphere.color.z * total_intensity.z
        )
        
        return Vector(
            min(1.0, max(0.0, final_color.x)),
            min(1.0, max(0.0, final_color.y)),
            min(1.0, max(0.0, final_color.z))
        )