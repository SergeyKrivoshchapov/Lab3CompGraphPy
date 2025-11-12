import math
import numpy as np
from PIL import Image
from vector import Vector
from camera import Camera
from scene import Scene

def render_scene(width, height):
    scene = Scene()
    scene.create_random_scene()
    
    camera = Camera(
        position=Vector(-5, -5, -5),
        look_at=Vector(0, 0, 1),
        up_vector=Vector(0, 1, 0),
        fov=75,
        width=width,
        height=height
    )
    
    x_coords, y_coords = np.meshgrid(np.arange(width), np.arange(height))
    x_coords = x_coords.flatten()
    y_coords = y_coords.flatten()
    
    image_buffer = np.zeros((len(x_coords), 3), dtype=np.float32)
    
    for i in range(len(x_coords)):
        ray = camera.generate_ray(x_coords[i], y_coords[i])
        sphere, t = scene.find_closest_intersection(ray)
        
        if sphere is not None:
            point = ray.point_at_parameter(t)
            normal = sphere.normal(point)
            view_direction = (camera.position - point).normalize()
            
            color = scene.compute_lighting(point, normal, view_direction, sphere)
            image_buffer[i] = [color.x, color.y, color.z]
        else:
            image_buffer[i] = [scene.background_color.x, 
                             scene.background_color.y, 
                             scene.background_color.z]
    
    image_buffer = (image_buffer.reshape(height, width, 3) * 255).astype(np.uint8)
    image = Image.fromarray(image_buffer, 'RGB')
    image.save('rendered_scene.png')
    image.show()
    
    print("saved")

if __name__ == "__main__":
    render_scene(800, 800)