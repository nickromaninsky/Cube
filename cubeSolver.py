# Program that solves a Rubik's Cube



# import sys module
import sys


# import pgame module
import pygame


# import utils module from rubik_solver
from rubik_solver import utils


# import os module
import os


# import subprocess module
import subprocess



# initilize py game
pygame.init()



# define white as rgb value 255, 255, 255
white = (255, 255, 255)


# define black as rgb value 0, 0, 0
black = (0, 0, 0)


# define red as rgb value 255, 0, 0
red = (255, 0, 0)


# define green as rgb value 0, 255, 0
green = (0, 255, 0)


# define blue as rgb value 0, 0, 255
blue = (0, 0, 255)


# define yellow as rgb value 255, 255, 0
yellow = (255, 255, 0)


# define purple as rgb value 128, 0, 128
purple = (128, 0, 128)


# define orange as rgb value 255, 165, 0
orange = (255, 165, 0)





# set "FPS" to integer 60
FPS = 60




# set the window caption to "3x3x3 Rubik's Cube Solver"
pygame.display.set_caption("3x3x3 Rubik's Cube Solver")



# define "font" as a system font named arial of size 25
font = pygame.font.SysFont("Arial", 25)



# define "font2" as a system font named arial of size 15
font2 = pygame.font.SysFont("Arial", 15)



# define "info" as the pygame display info function
info = pygame.display.Info()


# define "screen_width" as the user's screen_surface width
screen_width = info.current_w


# define "screen_height" as the user's screen_surface height
screen_height = info.current_h


# let the screen_surface be displaying the user's screen_surface width and screen_surface height
screen_surface = pygame.display.set_mode((screen_width, screen_height))



# define "cube_image" as the image "how_to_hold_cube.jpeg" on user's hard drive
cube_image = pygame.image.load('how_to_hold_cube.jpeg')


# update cube_image to cube_image with a size of 250 pixels * 250 pixels
cube_image = pygame.transform.scale(cube_image, (250, 250))



# define "order_image" as the image "order.png" on user's hard drive
order_image = pygame.image.load('order.png')      


# update order_image to order_image with a size of 600 pixels * 400 pixels
order_image = pygame.transform.scale(order_image, (600, 400))



# define "example_image" as the image "example.png" on user's hard drive
example_image = pygame.image.load('example.png')           


# update example_image to example_image with a size of 250 pixels * 250 pixels
example_image = pygame.transform.scale(example_image, (250, 250))



# define "notation_image" as the image "notation.webp" on user's hard drive
notation_image = pygame.image.load('notation.webp')           



# create the input boxes

# define input_box1 as a py game rectangle located at 5 across and 125 down and a size of 300 pixels * 50 pixels
input_box1 = pygame.Rect(5, 125, 300, 50)


# define input_box2 as a py game rectangle located at 5 across and 225 down and a size of 300 pixels * 50 pixels
input_box2 = pygame.Rect(5, 225, 300, 50)


# define input_box3 as a py game rectangle located at 5 across and 325 down and a size of 300 pixels * 50 pixels
input_box3 = pygame.Rect(5, 325, 300, 50)


# define input_box4 as a py game rectangle located at 5 across and 425 down and a size of 300 pixels * 50 pixels
input_box4 = pygame.Rect(5, 425, 300, 50)


# define input_box5 as a py game rectangle located at 5 across and 525 down and a size of 300 pixels * 50 pixels
input_box5 = pygame.Rect(5, 525, 300, 50)


# define input_box6 as a py game rectangle located at 5 across and 625 down and a size of 300 pixels * 50 pixels
input_box6 = pygame.Rect(5, 625, 300, 50)


# "colors" as py game color black * 6
colors = [pygame.Color('black')] * 6

# "active" as false * 6
active = [False] * 6


# "text" as "" (empty) * 6
text = [''] * 6



# create the quit button as a py game rectangle located at 1350 pixels across and 15 pixels down with a size of 100 pixels * 50 pixels
quit_button = pygame.Rect(1350, 15, 100, 50)


# create the again button as a py game rectangle located at 1150 pixels across and 15 pixels down with a size of 175 pixels * 50 pixels
again_button = pygame.Rect(1150, 15, 175, 50)


# create the solve button as a py game rectangle located at 1200 pixels across and 15 pixels down with a size of 125 pixels * 50 pixels
solve_button = pygame.Rect(1200, 200, 125, 50)



# define solve_clicked to false
solve_clicked = False



# create a function named "solve"
def solve():


    # create a global variable called solve_clicked
    global solve_clicked


    # update the display using the pygame.display.update function in py game
    pygame.display.update()


    # set solve_clicked to true
    solve_clicked = True




# create a function named "handle_input_events" that takes an argument of event
def handle_input_events(event):


    # create four global variables called active, colors, texts, and solve_clicked
    global active, colors, texts, solve_clicked


    # if the event type is the py game function mouse button down (clicking) then do the following
    if event.type == pygame.MOUSEBUTTONDOWN:


        # if the quit button is collided (clicked) then do the following
        if quit_button.collidepoint(event.pos):


            # set running to false
            running = False


            # stop running the system
            sys.exit()

        

        # if the again button is clicked then do the following
        if again_button.collidepoint(event.pos):


            # set command to "python3 cubeSolver.py" (the command that runs the program again)
            command = "python3 cubeSolver.py"


            # run "command" in the terminal
            subprocess.run(command, shell=True)
        


        # if the solve button is clicked then do the following
        if solve_button.collidepoint(event.pos):


            # set solve_clicked to true
            solve_clicked = True

        
        # if solve_clicked is true then do the following
        if solve_clicked == True:


            # call the "solve" function
            solve()


        # for all six boxes
        for i, box in enumerate([input_box1, input_box2, input_box3, input_box4, input_box5, input_box6]):


            # if the box is clicked
            if box.collidepoint(event.pos):


                # active[i] = not active[i]
                active[i] = not active[i]
            

            # if nothing else fit earlier conditions, do the following
            else:


                # active boxes = false
                active[i] = False



            # if the boxes are clicked highlight them blue, if they aren't clicked then highlight them black
            colors[i] = pygame.Color('dodgerblue2') if active[i] else pygame.Color('black')

    

    

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 4: # scroll up
            pygame.surface.scroll()
        elif event.button == 5: # scroll down
            print("2")
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP: # move up
            print("3")
        elif event.key == pygame.K_DOWN: # move down
            print("4")




    if event.type == pygame.KEYDOWN:
        # in the each box
        for i in range(len(active)):


            # if the box is active then do the following
            if active[i]:


                # if the key pressed is delete
                if event.key == pygame.K_BACKSPACE:


                    # delete the most recently typed character
                    text[i] = text[i][:-1]


                # if the conditions don't meet the earlier conditionals
                else:


                    # add the unicode character to the text
                    text[i] += event.unicode




# create a function named "draw_window"
def draw_window():


    # create a global variable named running
    global running


    # create a global variable named solve_clicked
    global solve_clicked



    # set clock to the py game fuction time.Clock
    clock = pygame.time.Clock()

    # only let the clock "tick" as fast as FPS (earlier set to 60)
    clock.tick(FPS)



    # fil the screen_surface with the color "white" (rgb value of 255, 255, 255)
    screen_surface.fill(white)



    # render "Enter Yellow Side (#0 - 8)" as text1_surface that is true and black in color
    text1_surface = font.render("Enter Yellow Side (#0 - 8)", True, black)


    # display text1_surface to 5 pixels across and 100 pixels down
    screen_surface.blit(text1_surface, (5, 100))



    # render "Enter Blue Side (#9 - 17)" as text2_surface that is true and black in color
    text2_surface = font.render("Enter Blue Side (#9 - 17)", True, black)


    # display text2_surface to 5 pixels across and 200 pixels down
    screen_surface.blit(text2_surface, (5, 200))



    # render "Enter Red Side (#18 - 26)" as text3_surface that is true and black in color
    text3_surface = font.render("Enter Red Side (#18 - 26)", True, black)


    # display text3_surface to 5 pixels across and 300 pixels down
    screen_surface.blit(text3_surface, (5, 300))



    # render "Enter Green Side (#27 - 35)" as text4_surface that is true and black in color
    text4_surface = font.render("Enter Green Side (#27 - 35)", True, black)


    # display text4_surface to 5 pixels across and 400 pixels down
    screen_surface.blit(text4_surface, (5, 400))



    # render "Enter Orange Side (#36 - 44)" as text5_surface that is true and black in color
    text5_surface = font.render("Enter Orange Side (#36 - 44)", True, black)


    # display text5_surface to 5 pixels across and 500 pixels down
    screen_surface.blit(text5_surface, (5, 500))



    # render "Enter White Side (#45 - 53)" as text6_surface that is true and black in color
    text6_surface = font.render("Enter White Side (#45 - 53)", True, black)


    # display_text6 surface to 5 pixels across and 600 pixels down
    screen_surface.blit(text6_surface, (5, 600))



    # render "Step One: Scramble cube as much as desired. Position scrambled cube to match Fig. One, with yellow center piece on top and red" as stepOne_surface with font2 (smaller font) that is true and black in color
    stepOne_surface = font2.render("Step One: Scramble cube as much as desired. Position scrambled cube to match Fig. One, with yellow center piece on top", True, black)


    # display stepOne_surface to 340 pixels across and 50 pixels down
    screen_surface.blit(stepOne_surface, (340, 50)) 


    # render "center piece facing you. The center piece of each side never moves and tells you what color that side will be when the cube is solved." as stepTwo_surface with font2 (smaller font) that is true and black in color
    stepTwo_surface = font2.render("and the red center piece facing you. The center piece of each side never moves and tells you what color that side will be when the cube is solved.", True, black)
    

    # display stepTwo_urface to 340 pixels across and 75 pixels down
    screen_surface.blit(stepTwo_surface, (340, 75)) 



    # render "3x3x3 Rubik's Cube Solver" as text_surface that is true and black in color
    text_surface = font.render("3x3x3 Rubik's Cube Solver", True, black)


    # display text_surface to 25 pixels across and 400 pixels down
    screen_surface.blit(text_surface, (340, 15))



    # render the input boxes

    # draw a rectangle to the screen_surface
    pygame.draw.rect(screen_surface, colors[0], input_box1, 2)


    # render a surface with the first text
    text_surface = font.render(text[0], True, black)


    # display text_surface to the screen_surface
    screen_surface.blit(text_surface, (input_box1.x + 5, input_box1.y + 5))



    # draw a rectangle to the screen_surface
    pygame.draw.rect(screen_surface, colors[1], input_box2, 2)


    # render a surface with the second text
    text_surface = font.render(text[1], True, black)


    # display text_surface to the screen_surface
    screen_surface.blit(text_surface, (input_box2.x + 5, input_box2.y + 5))


    # draw a rectangle to the screen_surface
    pygame.draw.rect(screen_surface, colors[2], input_box3, 2)


    # render a surface with the third text
    text_surface = font.render(text[2], True, black)


    # display text_surface to the screen_surface
    screen_surface.blit(text_surface, (input_box3.x + 5, input_box3.y + 5))



    # draw a rectangle to the screen_surface
    pygame.draw.rect(screen_surface, colors[3], input_box4, 2)


    # render a surface with the fourth text
    text_surface = font.render(text[3], True, black)


    # display text_surface to the screen_surface
    screen_surface.blit(text_surface, (input_box4.x + 5, input_box4.y + 5))



    # draw a rectangle to the screen_surface
    pygame.draw.rect(screen_surface, colors[4], input_box5, 2)


    # render a surface with the fifth text
    text_surface = font.render(text[4], True, black)


    # display text_surface to the screen_surface
    screen_surface.blit(text_surface, (input_box5.x + 5, input_box5.y + 5))



    # draw a rectangle to the screen_surface
    pygame.draw.rect(screen_surface, colors[5], input_box6, 2)


    # render a surface with the sixth text
    text_surface = font.render(text[5], True, black)


    # display text_surface to the screen_surface
    screen_surface.blit(text_surface, (input_box6.x + 5, input_box6.y + 5))



    # draw the quit button rectangle
    pygame.draw.rect(screen_surface, black, quit_button)


    # create a text_surface that contains "quit" which is true and white in color
    text_surface = font.render('Quit', True, white)

    
    # display the quit text surface on the quit button
    screen_surface.blit(text_surface, (quit_button.x + 25, quit_button.y + 10))



    # draw the again button rectangle
    pygame.draw.rect(screen_surface, black, again_button)


    # create a text_surface that contains "run again" which is true and white in color
    text_surface = font.render('Run Again', True, white)


    # display the again text surface on the again button
    screen_surface.blit(text_surface, (again_button.x + 25, again_button.y + 10))



    # draw the solve button rectangle
    pygame.draw.rect(screen_surface, black, solve_button)


    # create a text_surface that contains "solve" which is true and white in color
    text_surface = font.render('Solve', True, white)


    # draw the again button rectangle
    screen_surface.blit(text_surface, (solve_button.x + 25, solve_button.y + 10))



    # if solve_clicked is set to true then do the following
    if solve_clicked:


        # create a global variable called answer_surface
        global answer_surface


        
        # set cube as text but it's a string
        cube = (str(text))


        # set new_cube1 equal to cube but "[" is relaced with " "
        new_cube1 = cube.replace("[", "")


        # set new_cube2 equal to new_cube1 but "]" is relaced with " "
        new_cube2 = new_cube1.replace("]", "")


        # set new_cube3 equal to new_cube2 but "," is relaced with " "
        new_cube3 = new_cube2.replace(",", "")


        # set new_cube4 equal to new_cube3 but "'" is relaced with " "
        new_cube4 = new_cube3.replace("'", "")


        # set new_cube5 equal to new_cube4 but " " is relaced with ""
        new_cube5 = new_cube4.replace(" ", "")

        if (new_cube5 == "yyyyyyyyybbbbbbbbbrrrrrrrrrgggggggggooooooooowwwwwwwww"):

            solution_text = "Cube is already solved."


        else: 
            
            
            
            # set solution to new_cube5 solved using the Kociemba method
            solution = utils.solve(new_cube5, "Kociemba")


            # set solution_text to solution as a string
            solution_text = str(solution)


        # set answer_surface to the solution_text which is true and black in color using the big font
        answer_surface = font.render(solution_text, True, black)


        # display the answer surface to the screen_surface at 600 pixels across and 125 pixels down
        screen_surface.blit(answer_surface, (600, 125))

    


    # display the cube image to the screen_surface at 340 pixels across and 100 pixels down
    screen_surface.blit(cube_image, (340, 100))


    # display the order image to the screen_surface at 230 pixels across and 400 pixels down
    screen_surface.blit(order_image, (230, 400))



    # set text8_surface to "Step Two: Enter colors of scramble into fields at left in the numeral order set out below in Fig. 2 while keeping yellow center on top and red center facing you." which is true and black in color using font2 (the smaller font)
    text8_surface = font2.render("Step Two: Enter colors of scramble into fields at left in the numeral order set out below in Fig. 2 while keeping yellow center on top and red center facing you.", True, black)


    #  display the text8 surface to the screen_surface at 340 pixels across and 350 pixels down
    screen_surface.blit(text8_surface, (340, 350))


    # set text8_surface to "Type in the first letter of each color, as shown in Fig. Three. (For White: Note that 45 - 47 is adjacent to red 24 - 26.)" which is true and black in color using font2 (the smaller font)
    text8_surface = font2.render("Type in the first letter of each color, as shown in Fig. Three. (For White: Note that 45 - 47 is adjacent to red 24 - 26.)", True, black)


    #  display the text8 surface to the screen_surface at 340 pixels across and 375 pixels down
    screen_surface.blit(text8_surface, (340, 375))



    # display the example image to the screen_surface at 725 pixels across and 400 pixels down
    screen_surface.blit(example_image, (725, 400))



    # display the notation image to the screen_surface at 975 pixels across and 525 pixels down
    screen_surface.blit(notation_image, (975, 525))


    # set text8_surface to "Example: gwryygrgo" which is true and black in color using font2 (the smaller font)
    text8_surface = font2.render("Example: gwryygrgo", True, black)


    # display the text8 surface to the screen_surface at 775 pixels across and 600 pixels down
    screen_surface.blit(text8_surface, (775, 600))
    

    
    # set text100_surface to "Step Three: Click solve and execute moves using the chart" which is true and black in color using font2 (the smaller font)
    text100_surface = font2.render("Step Three: Click solve and execute moves using the chart", True, black)


    # display the text 100 surface to the screen_surface at 1050 pixels across and 425 pixels down
    screen_surface.blit(text100_surface, (1050, 425))
    

    # set text400_surface to "below. Be sure to maintain position of cube with yellow center" which is true and black in color using font2 (the smaller font)
    text400_surface = font2.render("below. Be sure to maintain position of cube with yellow center", True, black)


    # display the text 400 surface to the screen_surface at 1050 pixels across and 450 pixels down
    screen_surface.blit(text400_surface, (1050, 450))
    
    
    # set text401_surface to "on top and red center facing you." which is true and black in color using font2 (the smaller font)
    text401_surface = font2.render("on top and red center facing you.", True, black)


    # display the text 401 surface to the screen_surface at 1050 pixels across and 475 pixels down
    screen_surface.blit(text401_surface, (1050, 475))



    # set text401_surface to "Fig. Three" which is true and black in color using font (the bigger font)
    text401_surface = font.render("Fig. Three", True, black)
 

    # display the text 401 surface to the screen_surface at 785 pixels across and 415 pixels down
    screen_surface.blit(text401_surface, (785, 415))



    # set text401_surface to "Fig. Two" which is true and black in color using font (the bigger font)
    text401_surface = font.render("Fig. Two", True, black)


    # display the text 401 surface to the scrren at 550 pixels across and 475 pixels down 
    screen_surface.blit(text401_surface, (550, 475))



    # set text401_surface to "Fig. One" which is true and black in color using font (the bigger one)
    text401_surface = font.render("Fig. One", True, white)


    # display the text 401 surface to the screen_surface at 430 pixels across and 323 pixels down
    screen_surface.blit(text401_surface, (430, 323))



    # set text401_surface to "2 = Do Move Twice" which is true and black in color using font (the bigger one)
    text401_surface = font.render("2 = Do Move Twice", True, black)


    # display the text 401 surface to the screen_surface at 900 pixels across and 215 pixels down
    screen_surface.blit(text401_surface, (900, 215))


    
    # update the display using the py game display.update function
    pygame.display.update()






# create a function named "main"
def main():


    
    # set clock to the py game function time.Clock
    clock = pygame.time.Clock()



    # set "running" to true
    running = True


    # while running is true
    while running:


        #update the display using the py game disply.update function
        pygame.display.update()



        # clock can only tick as fast as FPS (previousluy set to 60)
        clock.tick(FPS)


        # for the event in whatever event
        for event in pygame.event.get():


            # if the event is "QUIT"
            if event.type == pygame.QUIT:


                # set running to false
                running = False
            
            
            # call the "handle_input_events" function with the argument "events"
            handle_input_events(event)
        

        # call the "draw_window" function
        draw_window()

    
    # update the display using the py game display.update function
    pygame.display.update()




# call the "main" function
main()




# these final lines of code are for if someone imports this file into their own project. it makes the main function not imediately start unless they explicitly state main() in their code
if __name__ == "__main__":
    main()


