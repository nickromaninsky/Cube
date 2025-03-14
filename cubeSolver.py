# Nick Romaninsky
# Period 8
# March 14th, 2025
# Program that solves a 3x3x3 Rubik's Cube using a graphical interface and the Kociemba algorithm.

import sys
import pygame
from rubik_solver import utils
import os
import subprocess

# Initialize pygame
pygame.init()

# Define color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

# Set FPS (frames per second) for the game
FPS = 60

# Set the window caption
pygame.display.set_caption("3x3x3 Rubik's Cube Solver")

# Define fonts
FONT = pygame.font.SysFont("Arial", 25)
SMALL_FONT = pygame.font.SysFont("Arial", 15)

# Get screen dimensions
screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h

# Set up the display surface
screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load and scale images
CUBE_IMAGE = pygame.transform.scale(pygame.image.load('how_to_hold_cube.jpeg'), (250, 250))
ORDER_IMAGE = pygame.transform.scale(pygame.image.load('order.png'), (600, 400))
EXAMPLE_IMAGE = pygame.transform.scale(pygame.image.load('example.png'), (250, 250))
NOTATION_IMAGE = pygame.transform.scale(pygame.image.load('notation.png'), (550, 350))

# Define input boxes
input_boxes = [
    pygame.Rect(5, 125, 300, 50),  # Yellow Side
    pygame.Rect(5, 225, 300, 50),  # Blue Side
    pygame.Rect(5, 325, 300, 50),  # Red Side
    pygame.Rect(5, 425, 300, 50),  # Green Side
    pygame.Rect(5, 525, 300, 50),  # Orange Side
    pygame.Rect(5, 625, 300, 50)   # White Side
]

# Initialize input box states
colors = [BLACK] * 6
active = [False] * 6
text = [''] * 6

# Define buttons
QUIT_BUTTON = pygame.Rect(1285, 15, 100, 50)
AGAIN_BUTTON = pygame.Rect(1285, 100, 175, 50)
SOLVE_BUTTON = pygame.Rect(1285, 185, 125, 50)

# Global variable to track if solve button is clicked
solve_clicked = False

# Function: solve
# Purpose: Solves the Rubik's Cube using the Kociemba algorithm and updates the display
def solve():
    global solve_clicked
    pygame.display.update()
    solve_clicked = True

# Function: handle_input_events
# Purpose: Handles user input events such as mouse clicks and key presses
def handle_input_events(event):
    global active, colors, text, solve_clicked

    if event.type == pygame.MOUSEBUTTONDOWN:
        if QUIT_BUTTON.collidepoint(event.pos):
            sys.exit()
        if AGAIN_BUTTON.collidepoint(event.pos):
            subprocess.run("python3 cubeSolver.py", shell=True)
        if SOLVE_BUTTON.collidepoint(event.pos):
            solve_clicked = True
        if solve_clicked:
            solve()
        for i, box in enumerate(input_boxes):
            if box.collidepoint(event.pos):
                active[i] = not active[i]
            else:
                active[i] = False
            colors[i] = BLUE if active[i] else BLACK

    if event.type == pygame.KEYDOWN:
        for i in range(len(active)):
            if active[i]:
                if event.key == pygame.K_BACKSPACE:
                    text[i] = text[i][:-1]
                else:
                    text[i] += event.unicode

# Function: draw_window
# Purpose: Draws all elements on the screen, including text, input boxes, buttons, and images
def draw_window():
    global running, solve_clicked

    clock = pygame.time.Clock()
    clock.tick(FPS)
    screen_surface.fill(WHITE)

    # Render text labels for input boxes
    labels = [
        "Enter Yellow Side (#0 - 8)",
        "Enter Blue Side (#9 - 17)",
        "Enter Red Side (#18 - 26)",
        "Enter Green Side (#27 - 35)",
        "Enter Orange Side (#36 - 44)",
        "Enter White Side (#45 - 53)"
    ]
    for i, label in enumerate(labels):
        text_surface = FONT.render(label, True, BLACK)
        screen_surface.blit(text_surface, (5, 100 + i * 100))

    # Render instructions
    instructions = [
        "Step One: Start with a scrambled cube. Position scrambled cube as in FIG. 1,",
        "with the yellow center piece on top and the red center piece facing you. The center",
        "piece of each side never moves and tells you what color that side will be when the cube is solved.",
        "Step Two: Enter colors of scramble into fields at left in the numerical order set out in FIG. 2.",
        "Type in the first letter of each color as shown in FIG. 3. (When entering Yellow Side, position",
        "cube so yellow center piece faces you and orange center piece is on top. When entering Blue,",
        "Red, Green, and Orange Sides, yellow center piece should be on top. When entering White Side,",
        "red center piece should be on top.)",
        "Step Three: Click 'Solve'. Solution will appear below. Execute moves using the pictures",
        "in FIG. 4. Be sure to maintain position of cube with yellow center on top and red",
        "center facing you. Note that a '2' next to a move means execute the move twice."
    ]
    for i, instruction in enumerate(instructions):
        text_surface = SMALL_FONT.render(instruction, True, BLACK)
        screen_surface.blit(text_surface, (340, 50 + i * 25))

    # Render input boxes
    for i, box in enumerate(input_boxes):
        pygame.draw.rect(screen_surface, colors[i], box, 2)
        text_surface = FONT.render(text[i], True, BLACK)
        screen_surface.blit(text_surface, (box.x + 5, box.y + 5))

    # Render buttons
    buttons = [
        (QUIT_BUTTON, "Quit"),
        (AGAIN_BUTTON, "Run Again"),
        (SOLVE_BUTTON, "Solve")
    ]
    for button, label in buttons:
        pygame.draw.rect(screen_surface, BLACK, button)
        text_surface = FONT.render(label, True, WHITE)
        screen_surface.blit(text_surface, (button.x + 25, button.y + 10))

    # Display solution if solve button is clicked
    if solve_clicked:
        cube_state = ''.join(text).replace(" ", "")
        if cube_state == "yyyyyyyyybbbbbbbbbrrrrrrrrrgggggggggooooooooowwwwwwwww":
            solution_text = "Cube is already solved."
        else:
            solution = utils.solve(cube_state, "Kociemba")
            solution_text = str(solution)
        answer_surface = FONT.render(solution_text, True, BLACK)
        screen_surface.blit(answer_surface, (5, 750))

    # Display images
    screen_surface.blit(CUBE_IMAGE, (1000, 10))
    screen_surface.blit(ORDER_IMAGE, (890, 275))
    screen_surface.blit(EXAMPLE_IMAGE, (1250, 650))
    screen_surface.blit(NOTATION_IMAGE, (330, 325))

    # Update display
    pygame.display.update()

# Function: main
# Purpose: Main function to run the program and handle the game loop
def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        pygame.display.update()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            handle_input_events(event)
        draw_window()

    pygame.display.update()

# Run the main function
main()
