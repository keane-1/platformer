from pygame import *
window = display.set_mode((1280, 720))
display.set_caption("Platformer Game")
background = transform.scale(image.load("assets/7 Levels/Preview/2lvl.jpg"), (1280, 720))
sprite1 = transform.scale(image.load("assets/1 Main Characters/1/Jump.png"), (60, 60))
clock = time.Clock()
clock.tick(10)
mixer.init()
mixer.music.load("bg_music.wav")
mixer.music.play(loops=-1)
jump_sound = mixer.Sound("jump.wav")
jump_played = False
x1 = 570
y1 = 430

game = True
while game:
    keys_pressed = key.get_pressed()
    if keys_pressed[K_w]:
        y1 -= 1
        if jump_played == False:
            jump_sound.play()
            jump_played = True
    if not keys_pressed[K_w]:
        jump_played = False
    if keys_pressed[K_a]:
        x1 -= 1
    if keys_pressed[K_s]:
        y1 += 1
    if keys_pressed[K_d]:
        x1 += 1
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()