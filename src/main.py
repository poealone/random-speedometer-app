import pygame
import time
from graphics.speedometer import Speedometer
from controllers.gamepad import GamepadController
from utils.random_generator import generate_random_bits

def main():
    pygame.init()
    screen = pygame.display.set_mode((200, 200), pygame.NOFRAME)  # Use NOFRAME to simulate fullscreen without errors
    pygame.display.set_caption("Random Speedometer")
    
    gamepad = GamepadController()
    speedometer = Speedometer(screen)
    
    menu_options = {
        1: "1 Minute",
        2: "5 Minutes",
        3: "10 Minutes",
        4: "Exit"
    }
    
    running = True
    while running:
        # Display main menu
        speedometer.draw_menu(menu_options)
        
        # Wait for user input
        while True:
            gamepad.update()
            if gamepad.button_pressed("UP"):
                gamepad.select_previous_option()
            elif gamepad.button_pressed("DOWN"):
                gamepad.select_next_option()
            elif gamepad.button_pressed("SELECT"):
                selected_option = gamepad.get_selected_option()
                if selected_option == 4:  # Exit
                    running = False
                    break
                else:
                    duration = selected_option * 60  # Convert to seconds
                    start_time = time.time()
                    while time.time() - start_time < duration:
                        random_bits = generate_random_bits(1)
                        speedometer.update(random_bits[0])
                        speedometer.draw()
                        pygame.display.flip()
                        time.sleep(0.1)
                    break

    pygame.quit()

if __name__ == "__main__":
    main()