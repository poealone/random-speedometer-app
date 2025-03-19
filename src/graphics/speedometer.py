class Speedometer:
    def __init__(self, width=240, height=240):
        import pygame
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.angle = 0

    def draw_speedometer(self):
        import pygame
        self.screen.fill((255, 255, 255))
        pygame.draw.circle(self.screen, (0, 0, 0), (self.width // 2, self.height // 2), 100, 2)
        pygame.draw.line(self.screen, (255, 0, 0), 
                         (self.width // 2, self.height // 2), 
                         (self.width // 2 + 100 * pygame.math.cos(pygame.math.radians(self.angle)), 
                          self.height // 2 - 100 * pygame.math.sin(pygame.math.radians(self.angle))), 2)
        pygame.display.flip()

    def update_needle(self, value):
        self.angle = (value * 180) - 90  # Scale value to angle

    def run(self):
        import pygame
        pygame.init()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.draw_speedometer()
            self.clock.tick(60)
        pygame.quit()