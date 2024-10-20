import random
import time
import os
from colorama import Fore, Style, init

# Function to initialize colorama
def initialize():
    init()

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main function for matrix effect
def matrix_effect():
    # Initializing the list of symbols
    symbols = ['*', '#', '$', '%', '&', '@', '!', '?', '+', '-', '=', '/', '^', '|', '~', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    # Getting terminal size
    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines

    try:
        while True:
            clear_screen()
            # Loop to generate random lines with symbols
            for _ in range(height // 2):  # Output for half the height of the terminal
                line = ''.join(random.choice(symbols) for _ in range(width))
                print(Fore.GREEN + line + Style.RESET_ALL)
            time.sleep(0.1)  # Pause for a short period to create the effect
    except KeyboardInterrupt:
        clear_screen()
        print("Exiting...")

# Run the program
if __name__ == "__main__":
    initialize()  # Initialize colorama
    matrix_effect()
