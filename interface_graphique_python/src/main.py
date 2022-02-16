import pygame
import Boutton



FOND_ECRAN = "/home/chalaud/Bureau/interface_graphique_python/ressources/image/fond.jpg"
LARGEUR_BOUTON_MENU = 50
LONGUEUR_BOUTON_MENU = 100

blank_color = (255, 255, 255)


def musique(path, volume):
    music = pygame.mixer.Sound(path)
    music.set_volume(volume)
    music.play()


def tableau_image():
    tab_image = [
        "/home/chalaud/Bureau/interface_graphique_python/ressources/image/jouer1.jpg",
        "/home/chalaud/Bureau/interface_graphique_python/ressources/image/jouer2.jpg",
        "/home/chalaud/Bureau/interface_graphique_python/ressources/image/sound_ON.png",
        "/home/chalaud/Bureau/interface_graphique_python/ressources/image/sound_OFF.png.png"
    ]
    return tab_image


def taille_ecran():
    fenetre = pygame.display.set_mode()
    x, y = fenetre.get_size()
    tab_size = [x, y]
    pygame.display.quit()

    return tab_size


pygame.init()
pygame.display.set_caption("my game")


def affichage_menu():

    taille = taille_ecran()
    window_surface = pygame.display.set_mode(taille)
    backgroud = pygame.image.load(FOND_ECRAN)
    backgroud.convert()
    window_surface.blit(backgroud, [0, 0])

    image_menu = tableau_image()

    bouton_jouer = Boutton.Button(image_menu[0], (taille[0]/2)-50, taille[1]/2,
                                  LONGUEUR_BOUTON_MENU, LARGEUR_BOUTON_MENU)
    bouton_jouer.affichage_du_bouton(window_surface)

    bouton_jouer2 = Boutton.Button(image_menu[1], (taille[0]/2)-50, (taille[1]/2) + 100,
                                   LONGUEUR_BOUTON_MENU, LARGEUR_BOUTON_MENU)
    bouton_jouer2.affichage_du_bouton(window_surface)


musique("/home/chalaud/Bureau/interface_graphique_python/ressources/son/maxkomusic-medieval-fantasy.wav", 0.5)
launched = True
affichage_menu()
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    pygame.display.flip()
