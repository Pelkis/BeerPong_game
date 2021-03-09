import pygame


pygame.init()
orange = (255, 200, 28)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
gameDisplay = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


def game_loop():
    decrease_speed = -1
    bar_start_width = 0
    bar_x = 100
    bar_y = 100
    bar_height = 50
    x_change = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = 5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        bar_start_width += x_change

        if bar_start_width > 0:
            bar_start_width += decrease_speed
        if bar_start_width <= 0:  # Set it to the minimum width of 1.
            bar_start_width = 1

    
        gameDisplay.fill(white)
        # Draw powerbar
        pygame.draw.rect(gameDisplay, green, (bar_x, bar_y, bar_start_width, bar_height))
          
        if bar_start_width >= 150:
            pygame.draw.rect(gameDisplay, orange, (bar_x, bar_y, bar_start_width, bar_height))
        if bar_start_width >= 300:
            pygame.draw.rect(gameDisplay, red, (bar_x, bar_y, bar_start_width, bar_height))
        if bar_start_width > 500:
            x_change = 0

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
