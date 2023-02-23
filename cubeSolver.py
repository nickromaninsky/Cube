#Program that solves a cube

import sys
import pygame
from rubik_solver import utils
import os
import subprocess

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (128, 0, 128)
orange = (255, 165, 0)

FPS = 30

pygame.display.set_caption("Rubik's Cube Solver")

font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 26)

info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h
screen = pygame.display.set_mode((screen_width, screen_height))

cube_image = pygame.image.load('cube_image.jpeg')           
cube_image = pygame.transform.scale(cube_image, (250, 250))  

order_image = pygame.image.load('order.png')           
order_image = pygame.transform.scale(order_image, (400, 400))  

# create the input boxes
input_box1 = pygame.Rect(100, 125, 300, 50)
text = [''] * 6

input_box2 = pygame.Rect(100, 225, 300, 50)

input_box3 = pygame.Rect(100, 325, 300, 50)

input_box4 = pygame.Rect(100, 425, 300, 50)

input_box5 = pygame.Rect(100, 525, 300, 50)

input_box6 = pygame.Rect(100, 625, 300, 50)

colors = [pygame.Color('black')] * 6
active = [False] * 6

x = 2
y = 1

# create the quit button
quit_button = pygame.Rect(1300, 25, 100, 50)

# create the again button
again_button = pygame.Rect(1100, 25, 175, 50)

# create the solve button
solve_button = pygame.Rect(1200, 475, 125, 50)

solve_clicked = False

def solve():
    global solve_clicked
    pygame.display.update()
    solve_clicked = True

def handle_input_events(event):

    global active, colors, texts, solve_clicked
    if event.type == pygame.MOUSEBUTTONDOWN:
        if quit_button.collidepoint(event.pos):
            sys.exit()
        if again_button.collidepoint(event.pos):
            command = "python3 cubeSolver.py"
            subprocess.run(command, shell=True)
        if solve_button.collidepoint(event.pos):
            solve_clicked = True
        if solve_clicked == True:
            solve()
        for i, box in enumerate([input_box1, input_box2, input_box3, input_box4, input_box5, input_box6]):
            if box.collidepoint(event.pos):
                active[i] = not active[i]
            else:
                active[i] = False
            colors[i] = pygame.Color('dodgerblue2') if active[i] else pygame.Color('lightskyblue3')
    if event.type == pygame.KEYDOWN:
        for i in range(len(active)):
            if active[i]:
                if event.key == pygame.K_BACKSPACE:
                    text[i] = text[i][:-1]
                else:
                    text[i] += event.unicode


def draw_window():
    global running
    global solve_clicked


    clock = pygame.time.Clock()
    clock.tick(FPS)
    screen.fill(white)

    text1_surface = font.render("Enter Yellow Side (0 - 8): ", True, black)
    screen.blit(text1_surface, (100, 100))

    text2_surface = font.render("Enter Blue Side (9 - 17): ", True, black)
    screen.blit(text2_surface, (100, 200))

    text3_surface = font.render("Enter Red Side (18 - 26): ", True, black)
    screen.blit(text3_surface, (100, 300))

    text4_surface = font.render("Enter Green Side (27 - 35): ", True, black)
    screen.blit(text4_surface, (100, 400))

    text5_surface = font.render("Enter Orange Side (36 - 44): ", True, black)
    screen.blit(text5_surface, (100, 500))

    text6_surface = font.render("Enter White Side (45 - 53): ", True, black)
    screen.blit(text6_surface, (100, 600))

    solution_surface = font2.render("Step One: Position cube like this, with yellow center piece on top and red center", True, black)
    screen.blit(solution_surface, (415, 50)) 

    solution_surface = font2.render("piece facing you. The center piece of each side never moves and tells you what color that side will be when the cube is solved.", True, black)
    screen.blit(solution_surface, (415, 75)) 

    # render the input boxes
    pygame.draw.rect(screen, colors[0], input_box1, 2)
    text_surface = font.render(text[0], True, black)
    screen.blit(text_surface, (input_box1.x + 5, input_box1.y + 5))

    pygame.draw.rect(screen, colors[1], input_box2, 2)
    text_surface = font.render(text[1], True, black)
    screen.blit(text_surface, (input_box2.x + 5, input_box2.y + 5))

    pygame.draw.rect(screen, colors[2], input_box3, 2)
    text_surface = font.render(text[2], True, black)
    screen.blit(text_surface, (input_box3.x + 5, input_box3.y + 5))

    pygame.draw.rect(screen, colors[3], input_box4, 2)
    text_surface = font.render(text[3], True, black)
    screen.blit(text_surface, (input_box4.x + 5, input_box4.y + 5))

    pygame.draw.rect(screen, colors[4], input_box5, 2)
    text_surface = font.render(text[4], True, black)
    screen.blit(text_surface, (input_box5.x + 5, input_box5.y + 5))

    pygame.draw.rect(screen, colors[5], input_box6, 2)
    text_surface = font.render(text[5], True, black)
    screen.blit(text_surface, (input_box6.x + 5, input_box6.y + 5))

    pygame.draw.rect(screen, black, quit_button)
    text_surface = font.render('Quit', True, white)
    screen.blit(text_surface, (quit_button.x + 25, quit_button.y + 10))

    pygame.draw.rect(screen, black, again_button)
    text_surface = font.render('Run Again', True, white)
    screen.blit(text_surface, (again_button.x + 25, again_button.y + 10))

    pygame.draw.rect(screen, black, solve_button)
    text_surface = font.render('Solve', True, white)
    screen.blit(text_surface, (solve_button.x + 25, solve_button.y + 10))

    if solve_clicked:
        global answer_surface
        cube = (str(text))
        new_cube1 = cube.replace("[", "")
        new_cube2 = new_cube1.replace("]", "")
        new_cube3 = new_cube2.replace(",", "")
        new_cube4 = new_cube3.replace("'", "")
        new_cube5 = new_cube4.replace(" ", "")
        solution = utils.solve(new_cube5, "Kociemba")
        solution_text = str(solution)  # convert to string
        answer_surface = font.render(solution_text, True, black)
        screen.blit(answer_surface, (700, 525))
        text9_surface = font.render("Thank you for using my Rubik's Cube Solver!", True, black)
        screen.blit(text9_surface, (700, 675))
        text10_surface = font.render("Click the run again button to try again,", True, black)
        screen.blit(text10_surface, (700, 700))
        text11_surface = font.render("or the quit button to quit the program.", True, black)
        screen.blit(text11_surface, (700, 725))
    


    #screen.blit(cube_image, (415, 525))

    #screen.blit(order_image, (415, 70))

    #text8_surface = font2.render("You MUST hold the cube like this the whole time. Look at the other sides from this angle.", True, black)
    #screen.blit(text8_surface, (415, 500))
    
    #text100_surface = font2.render("Position cube like this, with yellow center peice on top and red center peice facing you.", True, black)
    #screen.blit(text100_surface, (415, 475))
    
    #text400_surface = font2.render("Type in the colors in this order. Type in the first letter of the color for each facelet.", True, black)
    #screen.blit(text400_surface, (400, 50))
    pygame.display.update()

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


main()


if __name__ == "__main__":
    main()

