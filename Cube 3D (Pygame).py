import pygame
import math

class Cube:
    def __init__ (self, p1, p2, p3, p4):
        self.points = [self.p1, self.p2, self.p3, self.p4]
        self.p5 = [p1[0], p1[1]+90]
        self.p6 = [p2[0], p2[1]+90]
        self.p7 = [p3[0], p3[1]+90]
        self.p8 = [p4[0], p4[1]+90]
        self.points2 = [self.p5, self.p6, self.p7, self.p8]

        self.center = ((self.points[0][0]+self.points[2][0])/2, (self.points[0][1]+self.points[2][1])/2)

    def draw(self, screen):
        pygame.draw.polygon(screen, [255, 255, 255], self.points, 1)
        pygame.draw.polygon(screen, [255, 255, 255], self.points2, 1)
        for i in range(0, 4):
            pygame.draw.line(screen, [255, 255, 255], self.points[i], self.points2[i], 1)


    def rotate_horizontally(self, degrees_per_frame):
        self.center = ((self.points[0][0]+self.points[2][0])/2, (self.points[0][1]+self.points[2][1])/2)

        radians = math.pi/180 * degrees_per_frame
        matrix = [(math.cos(radians), -1*math.sin(radians)), (math.sin(radians), math.cos(radians))]

        for i in range(0, len(self.points)):
            point_x = self.center[0] + matrix[0][0]*(self.center[0]-self.points[i][0]) + matrix[0][1]*(self.center[1]-self.points[i][1])
            point_y = self.center[1] + matrix[1][0]*(self.center[0]-self.points[i][0]) + matrix[1][1]*(self.center[1]-self.points[i][1])
            self.points[i] = [point_x, point_y]

        self.p5 = [self.points[0][0], self.points[0][1]+100]
        self.p6 = [self.points[1][0], self.points[1][1]+100]
        self.p7 = [self.points[2][0], self.points[2][1]+100]
        self.p8 = [self.points[3][0], self.points[3][1]+100]
        self.points2 = [self.p5, self.p6, self.p7, self.p8]

def main():
    pygame.init()
    screen_size = [780, 540]
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Cube 3D")
    clock = pygame.time.Clock()
    
    screen.fill([0, 0, 0])

    cube = Cube([290,230], [370,190], [450,230], [370,270])

    end = False
    while end == False:
        clock.tick(60)
        screen.fill([0, 0, 0])

        cube.draw(screen)
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            cube.rotate_horizontally(2)
        elif keys[pygame.K_LEFT]:
            cube.rotate_horizontally(-2)
        
        pygame.display.update()

        # QUIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

if __name__ == "__main__":
    main()