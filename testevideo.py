import pygame

pygame.init()

# Substitua 'meu_video.mp4' pelo caminho completo do seu arquivo
video = pygame.movie.Movie("raffa_o_bardo.mp4")
screen = pygame.display.set_mode(video.get_size())
video.play()

while video.get_busy():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(video, (0, 0))
    pygame.display.flip()