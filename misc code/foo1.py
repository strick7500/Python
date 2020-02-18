# import sys and pygame modules
import sys, pygame
# initialize all pygame modules
pygame.init()

# create variable 'size' and set value to variables
# 'width' and 'height', and set values of 'width' and
# 'height' to 320 and 240, respectively

size = width, height = 320, 240

# create variable 'speed' and set value to a list
# containing [2, 2]

speed = [2, 2]

# create variable 'black' and set value to 0, 0, 0

black = 0, 0, 0

# create variable 'screen' and set value to pygame
# method pygame.display.set_mode(size) and pass in value
# of 'size' as input parameter

screen = pygame.display.set_mode(size)

# create variable 'ball' and set value to pygame method
# pygame.image.load("intro_ball.gif") and specify filepath
# to desired image to load

ball = pygame.image.load("intro_ball.gif")

# create variable 'ballrect' and set value to pygame method
# ball.get_rect() (this indicates "ball direction")
ballrect = ball.get_rect()

# ---Game Loop---
# This while loop is an infinite loop and is bad practice
# but produces the desired effect

# while 1 = Truthy, execute code within loop

while 1:

    # repeat loop for each 'event' retrieved when 
    # calling pygame.event.get() method

    for event in pygame.event.get():

        # if the event type is pygame.QUIT, pygame
        # exits

        if event.type == pygame.QUIT: sys.exit()

    # each time the main loop iterates, set the 
    # balls direction based on the value input from
    # 'speed'
        
    ballrect = ballrect.move(speed)

    # If the balls' direction exceeds the width or height
    # of the surface it exists on, adjust speed to keep
    # image inbounds

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # fill screen with input value 'black' on each
    # iteration of game loop

    screen.fill(black)

    # blit the image onto the screen and move it
    # according to input values 'ball' and 'ballrect'

    screen.blit(ball, ballrect)

    # set game display to act in a way similar to a flip
    # book for image movement
    
    pygame.display.flip()