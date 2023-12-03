import pygame
import configs
import assets
from objects.background import Background
from objects.bird import Bird
from objects.floor import Floor 
from objects.column import Column
from objects.gameover_message import GameOverMessage
from objects.gamestart_message import GameStartMessage
from objects.score import Score 
from objects.credit import Music


pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
column_create_event = pygame.USEREVENT
running = True
gameover = False
gamestarted = False
 

assets.load_sprites()
assets.load_audios()

sprites = pygame.sprite.LayeredUpdates()


def create_sprites():
    Music(0, sprites)
    Background(0,sprites)
    Background(1,sprites)
    Floor(0, sprites)
    Floor(1, sprites)

    return Bird(sprites), GameStartMessage(sprites), Score(sprites)

bird, game_start_message, score = create_sprites()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type ==column_create_event:
            Column(sprites)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not gamestarted and not gameover:
                gamestarted = True
                assets.play_audio("mainmenu")

                game_start_message.kill()
                pygame.time.set_timer(column_create_event, 1500)

            if event.key == pygame.K_ESCAPE and gameover:
                gameover = False
                assets.stop_audio("mainmenu")

                gamestarted = False
                sprites.empty()
                bird, game_start_message, score = create_sprites()



        bird.handle_event(event)


    screen.fill("pink")

    sprites.draw(screen)

    if gamestarted and not gameover:
        sprites.update()

    if bird.check_collision(sprites) and not gameover:
        gameover = True
        assets.stop_audio("mainmenu")

        gamestarted = False
        GameOverMessage(sprites)
        pygame.time.set_timer(column_create_event, 0)
        assets.play_audio("hit")


    for sprite in sprites:
        if type(sprite) is Column and sprite.is_passed():
            score.value += 1
            assets.play_audio("point")
        



    pygame.display.flip()
    clock.tick(configs.FPS)

pygame.quit()