import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600

v = pygame.math.Vector2(3, 4)
w = pygame.math.Vector2(9, -1)

print(v.x, v.y)

print(v + w)
print(v - w)
print(3 * v)

length_v = v.length()

len_sqr_v = v.length_squared()

print(length_v, len_sqr_v)

x_vec = pygame.math.Vector2(1, 0) # a normal vector on x-axis
angle = x_vec.angle_to(v)
print('direction angle of v', angle)