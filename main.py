import pygame as py


def main():
    py.init()
    screen = py.display.set_mode((1280, 720))
    clock = py.time.Clock()
    running = True

    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False

        screen.fill("green")

        py.display.flip()

        clock.tick(60)

    py.quit()


if __name__ == '__main__':
    main()
