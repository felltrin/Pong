import pygame as py


def ball_movement():
    py.draw.rect(screen, "black", py.Rect(ball_pos, (20, 20)))
    ball_pos.x += 5


def player_movement(player_one_pos, player_two_pos, dt):
    keys = py.key.get_pressed()
    if keys[py.K_w]:
        player_one_pos.y -= 300 * dt
    if keys[py.K_s]:
        player_one_pos.y += 300 * dt
    if keys[py.K_DOWN]:
        player_two_pos.y += 300 * dt
    if keys[py.K_UP]:
        player_two_pos.y -= 300 * dt


def player_constraint(player_one_pos, player_two_pos):
    if player_one_pos.y <= 0:
        player_one_pos.y = 0
    if player_one_pos.y >= 620:
        player_one_pos.y = 620
    if player_two_pos.y <= 0:
        player_two_pos.y = 0
    if player_two_pos.y >= 620:
        player_two_pos.y = 620


def draw_player(player_pos, screen):
    return py.draw.rect(screen, "black", py.Rect(player_pos, (20, 100)))


def draw_divider(screen):
    temp_pos = py.Vector2(screen.get_width() / 2, 0)
    for i in range(15):
        py.draw.rect(screen, "black", py.Rect(temp_pos, (20, 20)))
        temp_pos.y += 50


def draw_score(screen):
    screen.blit(player_one_score, (screen.get_width() / 4, 30))
    screen.blit(player_two_score, ((screen.get_width() / 4) * 3, 30))


if __name__ == '__main__':
    py.init()
    screen = py.display.set_mode((1280, 720))
    clock = py.time.Clock()
    running = True
    dt = 0

    my_font = py.font.SysFont("Sans Serif", 108)
    player_one_pos = py.Vector2(30, screen.get_height() / 2)
    player_two_pos = py.Vector2(1230, screen.get_height() / 2)
    ball_pos = py.Vector2(screen.get_width() / 2, 0)

    player_one_num, player_two_num = 0, 0
    player_one_score = my_font.render(str(player_one_num), 1, "black")
    player_two_score = my_font.render(str(player_two_num), 1, "black")

    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False

        screen.fill("green")

        draw_score(screen)
        player_one_rect = draw_player(player_one_pos, screen)
        player_two_rect = draw_player(player_two_pos, screen)
        player_movement(player_one_pos, player_two_pos, dt)
        player_constraint(player_one_pos, player_two_pos)
        draw_divider(screen)
        ball_movement()

        py.display.flip()

        dt = clock.tick(60) / 1000

    py.quit()
