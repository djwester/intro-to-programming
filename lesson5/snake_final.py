import random

import pygame

pygame.init()

yellow = (255, 255, 102)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

display_width = 600
display_height = 400
display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()


def display_score(score):
    score_font = pygame.font.SysFont("comicsansms", 35)
    value = score_font.render(f"Your Score: {score}", True, yellow)
    display.blit(value, [0, 0])


def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])  # noqa


def draw_food(foodx, foody, block_side_length):
    pygame.draw.rect(
        display, red, [foodx, foody, block_side_length, block_side_length]
    )  # noqa


def get_random_location(display_width, block_side_length):
    foodx = (
        round(random.randint(0, display_width - block_side_length) / 10.0)
        * 10.0  # noqa
    )  # noqa
    foody = (
        round(random.randint(0, display_height - block_side_length) / 10.0)
        * 10.0  # noqa
    )  # noqa
    return foodx, foody


game_over = False
snake_speed = 5
snake_length = 10
block_side_length = 10
snake_block_locations = []
direction = "right"

snake_x, snake_y = get_random_location(display_width, block_side_length)
foodx, foody = get_random_location(display_width, block_side_length)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = "left"
            elif event.key == pygame.K_RIGHT:
                direction = "right"
            elif event.key == pygame.K_UP:
                direction = "up"
            elif event.key == pygame.K_DOWN:
                direction = "down"

    if direction == "up":
        snake_y -= block_side_length
    elif direction == "down":
        snake_y += block_side_length
    elif direction == "left":
        snake_x -= block_side_length
    elif direction == "right":
        snake_x += block_side_length

    # check if the snake has hit the edge
    if (
        snake_x < 0
        or snake_x > display_width
        or snake_y < 0
        or snake_y > display_height
    ):
        game_over = True

    # check if the snake has hit itself
    for snake_block in snake_block_locations:
        if snake_block[0] == snake_x and snake_block[1] == snake_y:
            game_over = True

    snake_block_locations.append([snake_x, snake_y])

    if len(snake_block_locations) > snake_length:
        del snake_block_locations[0]

    display.fill(blue)
    draw_food(foodx, foody, block_side_length)
    draw_snake(block_side_length, snake_block_locations)

    pygame.display.update()

    # If the snake ate the food, move the food.
    if snake_x == foodx and snake_y == foody:
        foodx, foody = get_random_location(display_width, block_side_length)
        snake_length += 1

    clock.tick(snake_speed)

    while game_over:
        display.fill(green)
        display_score(snake_length - 1)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    snake_x = 100
                    snake_y = 100
                    foodx, foody = get_random_location(
                        display_width, block_side_length
                    )  # noqa
                    snake_speed = 5

                    snake_length = 10
                    snake_block_locations = []
                    direction = "right"
                    game_over = False
