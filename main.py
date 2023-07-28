import pygame as py


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


def draw_player(player_pos, screen):
    py.draw.rect(screen, "black", py.Rect(player_pos, (20, 100)))


def draw_divider(screen):
    temp_pos = py.Vector2(screen.get_width() / 2, 0)
    for i in range(10):
        py.draw.rect(screen, "black", py.Rect(temp_pos, (10, 50)))
        temp_pos.y += 100


def main():
    py.init()
    screen = py.display.set_mode((1280, 720))
    clock = py.time.Clock()
    running = True
    dt = 0

    player_one_pos = py.Vector2(75, screen.get_height() / 2)
    player_two_pos = py.Vector2(1200, screen.get_height() / 2)

    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False

        screen.fill("green")

        draw_player(player_one_pos, screen)
        draw_player(player_two_pos, screen)
        player_movement(player_one_pos, player_two_pos, dt)
        draw_divider(screen)

        py.display.flip()

        dt = clock.tick(60) / 1000

    py.quit()


if __name__ == '__main__':
    main()
