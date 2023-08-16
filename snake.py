import pygame, sys, time, random

speed = 15

#Window size

frame_size_x = 720
frame_size_y = 480

check_errors = pygame.init()

if(check_errors[1] > 0):
    print("Error" + check_errors[1])
else:
    print("Game succesfully initialized")


pygame.display.set_caption("Snake game")
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

#colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialize obstacle variables
obstacle_positions = [(3, 4), (2, 4), (3, 5), (2, 5),
                        (20, 4), (20, 5), (19, 4), (19, 5),
                            (9, 10), (8, 10), (7, 10), (6, 10), (5, 10), (4, 10), (10, 10), (11, 10), (12, 10), (13, 10), (14, 10), (15, 10), (16,10), (17, 10), (18, 10), (19, 10), (20, 10), (21, 10), (22,10), (23, 10), (24, 10), (25, 10), (26, 10), (27, 10), (28, 10), (29, 10), (30, 10),
                                (10, 15), (9, 15), (10, 14), (9, 14), (25, 15), (24, 15), (25, 14), (24, 14),
                                    (18, 11), (18, 12), (18, 13), (18, 14), (18, 15), (18, 16), (18, 17), (18, 18), (18, 19), (18, 20), (18, 21), (18, 22), (18, 23), (18, 24), (18, 25)]  
obstacle_color = (128, 128, 128)

fps_controller = pygame.time.Clock()
# one snake square size
square_size = 20

def init_vars():
    global head_pos, snake_body, food_pos, food_spawn, score, direction
    direction = "RIGHT"
    head_pos = [120, 60]
    snake_body = [[120, 60]]
    food_pos = [random.randrange(1,(frame_size_x // square_size)) * square_size,
                random.randrange(1,(frame_size_y // square_size)) * square_size]
    food_spawn = True
    score = 0

init_vars()

def place_food():
    global food_pos
    while True:
        food_pos = [random.randrange(1, (frame_size_x // square_size)) * square_size,
                    random.randrange(1, (frame_size_y // square_size)) * square_size]
        if all(food_pos != pos for pos in obstacle_positions):
            break


def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score: " + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x / 10, 15)
    else:
        score_rect.midtop = (frame_size_x/2 , frame_size_y/1.25)

    game_window.blit(score_surface, score_rect)


# Game loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if ( event.key == pygame.K_UP or event.key == ord("w")
                and direction != "DOWN"):
                direction = "UP"
            elif ( event.key == pygame.K_DOWN or event.key == ord("s")
                and direction != "UP"):
                direction = "DOWN"
            elif ( event.key == pygame.K_LEFT or event.key == ord("a")
                and direction != "RIGHT"):
                direction = "LEFT"
            elif ( event.key == pygame.K_RIGHT or event.key == ord("d")
                and direction != "LEFT"):
                direction = "RIGHT"

    if direction == "UP":
        head_pos[1] -= square_size
    elif direction == "DOWN":
        head_pos[1] += square_size
    elif direction == "LEFT":
        head_pos[0] -=square_size
    else:
        head_pos[0] +=square_size

    if head_pos[0] < 0:
        head_pos[0] = frame_size_x - square_size
    elif head_pos[0] > frame_size_x - square_size:
        head_pos[0] = 0
    elif head_pos[1] < 0:
        head_pos[1] = frame_size_y - square_size
    elif head_pos[1] > frame_size_y - square_size:
        head_pos[1] = 0  

    # Eating
    snake_body.insert(0, list(head_pos))
    if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()
        if score == 20:
            speed = 23

    # Food spawn
    if not food_spawn:
        food_pos = [random.randrange(1,(frame_size_x // square_size)) * square_size,
            random.randrange(1,(frame_size_y // square_size)) * square_size]
        food_spawn = True

            
    # GFX
    game_window.fill(black)

    for obstacle_pos in obstacle_positions:
        obstacle_rect = pygame.Rect(obstacle_pos[0] * square_size, obstacle_pos[1] * square_size, square_size, square_size)
        pygame.draw.rect(game_window, obstacle_color, obstacle_rect)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(
            pos[0] + 2, pos[1] + 2,
            square_size -2, square_size -2))
        
    pygame.draw.rect(game_window, red, pygame.Rect(food_pos[0],
                    food_pos[1], square_size, square_size))
    
    
    for obstacle_pos in obstacle_positions:
        obstacle_rect = pygame.Rect(obstacle_pos[0] * square_size, obstacle_pos[1] * square_size, square_size, square_size)
        pygame.draw.rect(game_window, obstacle_color, obstacle_rect)
    
    # Game over

    for block in snake_body[1:]:
        if head_pos[0] == block[0] and head_pos[1] == block[1]:
            init_vars()
    
    for obstacle_pos in obstacle_positions:
        if head_pos[0] == obstacle_pos[0] * square_size and head_pos[1] == obstacle_pos[1] * square_size:
            init_vars()

    show_score(1, white, 'consolas', 20)
    pygame.display.update()
    fps_controller.tick(speed)