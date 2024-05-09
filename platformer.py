from pygame import *
window = display.set_mode((1280, 720))
display.set_caption("Platformer Game")
background = transform.scale(image.load("assets/7 Levels/Preview/2lvl.jpg"), (1280, 720))

game = True
while game:
    window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()