import pygame
import math

class Cube:
    def __init__ (self, p1, p2, p3, p4, height):
        self.points = [p1, p2, p3, p4]
        self.height = height
        self.p5 = [p1[0], p1[1]+self.height]
        self.p6 = [p2[0], p2[1]+self.height]
        self.p7 = [p3[0], p3[1]+self.height]
        self.p8 = [p4[0], p4[1]+self.height]
        self.points2 = [self.p5, self.p6, self.p7, self.p8]

        self.center = ((self.points[0][0]+self.points[2][0])/2, (self.points[0][1]+self.points[2][1])/2)

    def draw(self, screen):
        pygame.draw.polygon(screen, [255, 255, 255], self.points, 1)
        pygame.draw.polygon(screen, [255, 255, 255], self.points2, 1)
        for i in range(0, 4):
            pygame.draw.line(screen, [255, 255, 255], self.points[i], self.points2[i], 1)

    def rotate_horizontally(self, degrees_per_frame):
        #self.center = ((self.points[0][0]+self.points[2][0])/2, (self.points[0][1]+self.points[2][1])/2)

        radians = math.pi/180 * degrees_per_frame
        matrix = [(math.cos(radians), -1*math.sin(radians)), (math.sin(radians), math.cos(radians))]

        for i in range(0, len(self.points)):
            temp_x = self.points[i][0]
            temp_y = self.points[i][1]
            point_x = self.center[0] + matrix[0][0]*(self.points[i][0]-self.center[0]) + matrix[0][1]*(self.points[i][1]-self.center[1])
            point_y = self.center[1] + matrix[1][0]*(self.points[i][0]-self.center[0]) + matrix[1][1]*(self.points[i][1]-self.center[1])
            self.points[i] = [point_x, point_y]

        self.p5 = [self.points[0][0], self.points[0][1]+self.height]
        self.p6 = [self.points[1][0], self.points[1][1]+self.height]
        self.p7 = [self.points[2][0], self.points[2][1]+self.height]
        self.p8 = [self.points[3][0], self.points[3][1]+self.height]
        self.points2 = [self.p5, self.p6, self.p7, self.p8]

def generate_cubes( x, y, focused_cube = 1, amount = 3, size = 80):
    generated_cubes = []
    for i in range(0, amount*size, size):
        for j in range(0, amount*size, size):
            generated_cubes.append(Cube([x+i, y+j], [x+size+i, y+j], [x+size+i, y+size+j], [x+i, y+size+j], size))

    for cube in generated_cubes:
        cube.center = generated_cubes[focused_cube - 1].center

    return generated_cubes

def main():
    pygame.init()
    screen_size = [780, 540]
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Cube 3D")
    clock = pygame.time.Clock()
    
    screen.fill([0, 0, 0])

    cube_list = []

    cube = Cube([290,230], [370,230], [370,310], [290,310], 80)
    cube_list.append(cube)
    cube2 = Cube([210,230], [290,230], [290,310], [210,310], 80)
    cube2.center = cube.center
    cube_list.append(cube2)
    cube3 = Cube([370,230], [450,230], [450,310], [370,310], 80)
    cube3.center = cube.center
    cube_list.append(cube3)
    degrees_per_frame = 2

    generated_cubes = generate_cubes(100, 100, 11, 4, 80)

    end = False
    while end == False:
        clock.tick(60)
        screen.fill([0, 0, 0])

        #for cub in cube_list:
            #cub.draw(screen)
        
        for cub in generated_cubes:
            cub.draw(screen)

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            for cub in cube_list:
                cub.rotate_horizontally(degrees_per_frame)
            for cub in generated_cubes:
                cub.rotate_horizontally(degrees_per_frame)
        elif keys[pygame.K_LEFT]:
            for cub in cube_list:
                cub.rotate_horizontally(-1*degrees_per_frame)
            for cub in generated_cubes:
                cub.rotate_horizontally(-1*degrees_per_frame)
        if keys[pygame.K_UP]:
            degrees_per_frame += 0.05
        if keys[pygame.K_DOWN]:
            if degrees_per_frame > 0.05:
                degrees_per_frame -= 0.05
        
        pygame.display.update()

        # QUIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

if __name__ == "__main__":
    main()