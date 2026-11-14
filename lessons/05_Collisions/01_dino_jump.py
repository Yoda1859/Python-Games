"""
Dino Jump

Use the arrow keys to move the blue square up and down to avoid the black
obstacles. The game should end when the player collides with an obstacle ...
but it does not. It's a work in progress, and you'll have to finish it. 

"""
import pygame
import random
from pathlib import Path
assets = Path(__file__).parent/"images"
# Initialize Pygame
pygame.init()

images_dir = Path(__file__).parent / "images" if (Path(__file__).parent / "images").exists() else Path(__file__).parent / "assets"

class Settings:

# Screen dimensions
    WIDTH, HEIGHT = 600, 300
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dino Jump")

# Colors
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

# FPS
    FPS = 60

# Player attributes
    PLAYER_SIZE = 35

    player_speed = 5

# Obstacle attributes
    OBSTACLE_WIDTH = 30
    OBSTACLE_HEIGHT = 30
    obstacle_speed = 5

# Font
    font = pygame.font.SysFont(None, 36)


# Define an obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.create_obstacle_image()
        self.rect = pygame.Rect(0,0, Settings.PLAYER_SIZE, Settings.PLAYER_SIZE)
        self.rect.x = Settings.WIDTH
        self.rect.y = Settings.HEIGHT - Settings.OBSTACLE_HEIGHT - 10
        self.image = pygame.transform.scale(self.image,(self.rect.size))

        self.explosion = pygame.image.load(images_dir / "explosion1.gif")

    def update(self):
        self.rect.x -= Settings.obstacle_speed
        # Remove the obstacle if it goes off screen
        if self.rect.right < 0:
            self.kill()

    def explode(self):
        """Replace the image with an explosition image."""
        
        # Load the explosion image
        self.image = self.explosion
        self.image = pygame.transform.scale(self.image, (Settings.OBSTACLE_WIDTH, Settings.OBSTACLE_HEIGHT))
        self.rect = self.image.get_rect(center=self.rect.center)

    def create_obstacle_image(self):
        self.image = pygame.image.load(assets/'cactus_9.png')

# Define a player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.create_dino_image()
        self.rect = pygame.Rect(0,0, Settings.PLAYER_SIZE, Settings.PLAYER_SIZE)
        self.rect.x = 50
        self.rect.y = Settings.HEIGHT - Settings.PLAYER_SIZE - 10
        self.speed = Settings.player_speed
        self.image = pygame.transform.scale(self.image,(self.rect.size))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Keep the player on screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > Settings.HEIGHT:
            self.rect.bottom = Settings.HEIGHT

    def create_dino_image(self):
        self.image = pygame.image.load(assets/'dino_0.png')

class Game:

# Add obstacles periodically
    def add_obstacle(obstacles):
    # random.random() returns a random float between 0 and 1, so a value
    # of 0.25 means that there is a 25% chance of adding an obstacle. Since
    # add_obstacle() is called every 100ms, this means that on average, an
    # obstacle will be added every 400ms.
    # The combination of the randomness and the time allows for random
    # obstacles, but not too close together. 
    
        if random.random() < 0.4:
            obstacle = Obstacle()
            obstacles.add(obstacle)
            return 1
        return 0


# Main game loop
    def game_loop():
        clock = pygame.time.Clock()
        game_over = False
        last_obstacle_time = pygame.time.get_ticks()

    # Group for obstacles
        obstacles = pygame.sprite.Group()

# Create a player object
        player = Player()
        player_group = pygame.sprite.GroupSingle(player)

        obstacle_count = 0

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        # Update player
            player.update()

        # Add obstacles and update
            if pygame.time.get_ticks() - last_obstacle_time > 500:
                last_obstacle_time = pygame.time.get_ticks()
                obstacle_count += Game.add_obstacle(obstacles)
        
            obstacles.update()

        # Check for collisions
            collider = pygame.sprite.spritecollide(player, obstacles, dokill=False)
            if collider:
                    collider[0].explode()
       
        # Draw everything
            Settings.screen.fill(Settings.WHITE)
            player_group.draw(Settings.screen)
            obstacles.draw(Settings.screen)

        # Display obstacle count
            obstacle_text = Settings.font.render(f"Obstacles: {obstacle_count}", True, Settings.BLACK)
            Settings.screen.blit(obstacle_text, (10, 10))

            pygame.display.update()
            clock.tick(Settings.FPS)

    # Game over screen
        Settings.screen.fill(Settings.WHITE)

if __name__ == "__main__":


    
    Game.game_loop()
