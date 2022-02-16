import pygame


#pygame.mixer.init()
pygame.init()


def musique(path, volume):
    music = pygame.mixer.Sound(path)
    music.set_volume(volume)
    music.play()


launched = True
while launched:
    musique("/home/chalaud/Bureau/interface_graphique_python/ressources/son/maxkomusic-medieval-fantasy.wav", 0.1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
