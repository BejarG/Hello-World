'''
PingPong Project
'''

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Bouncing Rectangle - With Keys input")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting position of the rectangle\
circle_x = 350
circle_y = 225
rect_x = 670
rect_y = 225
left_rect_x = 10
left_rect_y = 225

# Speed and direction of rectangle
circle_change_x = 4
circle_change_y = 4
rect_change_x = 0
rect_change_y = 0
left_rect_change_x = 0
left_rect_change_y = 0

# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_RIGHT:
            #     rect_change_x+=
            # elif event.key == pygame.K_LEFT:
            #     rect_change_x -= 5
            if event.key == pygame.K_UP:
                rect_change_y -= 5
            elif event.key == pygame.K_DOWN:
                rect_change_y += 5
            elif event.key == pygame.K_w:
                left_rect_change_y -= 5
            elif event.key == pygame.K_s:
                left_rect_change_y += 5


            # Write here the conditions to control the vertical motion

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT  or event.key == pygame.K_LEFT :
                rect_change_x = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                rect_change_y = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                left_rect_change_y = 0
            elif event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
                left_rect_change_x=0

            # Write here to stop the vertical motion when keys are up



    # --- Logic
    # Move the rectangle starting point
    rect_x += rect_change_x
    rect_y += rect_change_y
    left_rect_x+=left_rect_change_x
    left_rect_y+=left_rect_change_y
    circle_x += circle_change_x
    circle_y += circle_change_y

    # Bounce the ball if needed
    # if rect_y > 450 or rect_y < 0:
    #     rect_change_y = rect_change_y * -1
    # if rect_x > 650 or rect_x < 0:
    #     rect_change_x = rect_change_x * -1
    if circle_y > 490 or circle_y < 10 :
        circle_change_y = circle_change_y * -1
    if circle_x > 690 or circle_x < 10 :
        circle_change_x = circle_change_x * -1
    # if circle_y > rect_x:
    #     circle_change_x = circle_change_x * -1



    # --- Drawing
    # Set the screen background
    screen.fill(BLACK)

    # Draw the rectangle
    # pygame.draw.rect(Surface,color,Rect,width = 0)
    right = pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 20, 150])
    left = pygame.draw.rect(screen, WHITE, (left_rect_x, left_rect_y , 20, 150))
    pygame.draw.rect(screen,WHITE, (345, 0,20 , 700))

    ball = pygame.draw.circle(screen, RED, (circle_x, circle_y), 10, 0)

    if left.colliderect(ball):
        circle_change_x = circle_change_x * -1
    if right.colliderect(ball):
        circle_change_x = circle_change_x * -1



    # pygame.draw.circle(Surface, color, pos, radius, width=0) -> Rect

    # pygame.draw.circle(screen, RED, (200, 200), 20, 20)

    # --- Wrap-up
    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Close everything down

