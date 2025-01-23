import pygame
import constants

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f'Screen width: {constants.SCREEN_WIDTH}')
    print(f'Screen height: {constants.SCREEN_HEIGHT}')
    running = True
    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color='red')
        pygame.display.flip()

if __name__ == "__main__":
    main()