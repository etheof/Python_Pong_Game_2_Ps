import pygame

#initialize game window
pygame.init()
pygame.display.set_caption("Pong for Two, Mouse for Player 1, Arrow-Keys for Player 2")
w = 640
h = 480
screen = pygame.display.set_mode((w, h))
font = pygame.font.Font(None, 24)

#initialize elements
ball = pygame.draw.circle(screen, (0,255,0), (w /2, h /2), 8)
paddle1 = pygame.Rect((8, 200), (8, 80))
paddle2 = pygame.Rect((w -16, 200), (8, 80))

#initialize scoreboard and ball speed on axis
score1 = 0
score2 = 0
ball_speed = [6,4] 


# mainloop
#this was copied from the net, did not know event handlers
while True:
    # event handler
    for event in pygame.event.get():
        # quit event => close the game
        if event.type == pygame.QUIT:
            exit(0)
        # control Paddle 1 with the mouse
        elif event.type == pygame.MOUSEMOTION:
            paddle1.centery = event.pos[1]
           
            # correct paddle position if it's going out of window
            if paddle1.top < 0:
                paddle1.top = 0
            elif paddle1.bottom >= h:
                paddle1.bottom = h
            
            if paddle2.top < 0:
                paddle2.top = 0
            elif paddle2.bottom >= h:
                paddle2.bottom = h


    # Player 2 paddle controls
    if pygame.key.get_pressed()[pygame.K_UP] and paddle2.top > 0:
        paddle2.top -= 5
    elif pygame.key.get_pressed()[pygame.K_DOWN] and paddle2.bottom < h:
        paddle2.top += 5

    # update ball position
    ball.left += ball_speed[0]
    ball.top += ball_speed[1]

    # Top and bottom bounaries, bounce like reaction
    if ball.top <= 0 or ball.bottom >= h:
        ball_speed[1] = -ball_speed[1]


    # Ball out of left - right bounds, update score, reset ball
    elif ball.left <= 0:
        score1 -= 1
        ball = pygame.Rect((312, 232), (16, 16))
    
    elif ball.right >= w:
        score2 -= 1
        ball = pygame.Rect((312, 232), (16, 16))

    # Ball hits either paddle, point for respective player
    if paddle1.colliderect(ball):
        ball_speed[0] = -ball_speed[0]
        score1 += 1

    if paddle2.colliderect(ball):
        ball_speed[0] = -ball_speed[0]
        score2 += 1

    # clear screen
    screen.fill((0, 0, 0))

    # draw the ball, the paddles and the scoreboard
    pygame.draw.rect(screen, (0, 255, 0), paddle1) # Green player paddle
    pygame.draw.rect(screen, (255, 0, 0), paddle2) # Red player paddle
    pygame.draw.circle(screen, (0, 0, 255), ball.center, ball.width/2) # Blue Ball

    score_text = font.render(str(score1), True, (0, 255, 0))
    screen.blit(score_text, (320-font.size(str(score1))[0]/2, 5)) # score player 1

    score_text = font.render(str(score2), True, (255, 0, 0))
    screen.blit(score_text, (320-font.size(str(score2))[0]/2, h -20))  # score player2

    # update screen and wait 20 milliseconds
    pygame.display.flip()
    pygame.time.delay(20)