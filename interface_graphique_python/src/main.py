import pygame
import Boutton
import math

FOND_ECRAN = \
    "/home/chalaud/Bureau/git/projet_perso/interface_graphique_python/ressources/image/fond.jpg"
LARGEUR_BOUTON_MENU = 50
LONGUEUR_BOUTON_MENU = 150
LARGEUR_TITRE = 250
LONGUEUR_TITRE = 350

MUTE_SOUND = 0
MODE_JOUER = 1
MODE_OPTIONS = 2

blank_color = (255, 255, 255)


def musique(path, volume):
    music = pygame.mixer.Sound(path)
    music.set_volume(volume)
    music.play()


def tableau_image():
    tab_image = [
        "/home/chalaud/Bureau/git/projet_perso/interface_graphique_python/ressources/image/titre.jpeg",
        "/home/chalaud/Bureau/git/projet_perso/interface_graphique_python/ressources/image/play.jpg",
        "/home/chalaud/Bureau/git/projet_perso/interface_graphique_python/ressources/image/settings.jpg",
        "/home/chalaud/Bureau/git/projet_perso/interface_graphique_python/ressources/image/exit.jpg",
        "/home/chalaud/Bureau/git/projet_perso/interface_graphique_python/ressources/image/sound_ON.png",
        "/home/chalaud/Bureau/git/projet_perso/interface_graphique_python/ressources/image/sound_OFF.png",
        "/home/chalaud/Bureau/git/projet_perso/interface_graphique_python/ressources/image/jouer1.jpg",
        "/home/chalaud/Bureau/git/projet_perso/interface_graphique_python/ressources/image/retour.jpeg"

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

    bouton_titre = Boutton.Button(image_menu[0], image_menu[0], (taille[0]/2)-140, (taille[1]/2)-400,
                                  LONGUEUR_TITRE, LARGEUR_TITRE)
    bouton_titre.affichage_du_bouton(window_surface)

    bouton_jouer = Boutton.Button(image_menu[1], image_menu[1], (taille[0]/2)-50, taille[1]/2-30,
                                  LONGUEUR_BOUTON_MENU, LARGEUR_BOUTON_MENU)
    bouton_jouer.affichage_du_bouton(window_surface)

    bouton_options = Boutton.Button(image_menu[2], image_menu[2], (taille[0]/2)-50, (taille[1]/2) + 110,
                                   LONGUEUR_BOUTON_MENU, LARGEUR_BOUTON_MENU)
    bouton_options.affichage_du_bouton(window_surface)

    bouton_quitter = Boutton.Button(image_menu[3], image_menu[3], (taille[0]/2)-50, (taille[1]/2) + 40,
                                   LONGUEUR_BOUTON_MENU, LARGEUR_BOUTON_MENU)
    bouton_quitter.affichage_du_bouton(window_surface)

    bouton_son_on = Boutton.Button(image_menu[4], image_menu[4], (taille[0]/12), (taille[1] - (taille[1]/6)), 75, 75)
    bouton_son_on.affichage_du_bouton(window_surface)

    bouton_son_off = Boutton.Button(image_menu[5], image_menu[5], (taille[0]/12), (taille[1] - (taille[1]/6)), 75, 75)

    pygame.display.flip()
    status_son = 0
    launched = True
    while launched:
        musique("/home/chalaud/Bureau/git/projet_perso/interface_graphique_python/ressources/son/maxkomusic-medieval-fantasy.wav", 0.5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                launched = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and bouton_son_on.reactangle.collidepoint(event.pos) and status_son == 0:
                    print("on off")
                    window_surface.blit(window_surface, [0, 0])
                    bouton_son_off.affichage_du_bouton(window_surface)
                    pygame.mixer.pause()
                    MUTE_SOUND = 1
                    status_son = 1
                    break
                elif event.button == 1 and bouton_son_on.reactangle.collidepoint(event.pos) and status_son == 1:
                    musique("/home/chalaud/Bureau/git/projet_perso/interface_graphique_python/ressources/son/maxkomusic-medieval-fantasy.wav", 0.5)
                    MUTE_SOUND = 0
                    print("off on")
                    window_surface.blit(window_surface, [0, 0])
                    bouton_son_on.affichage_du_bouton(window_surface)
                    pygame.mixer.unpause()
                    status_son = 0
                    break
                elif event.button == 1 and bouton_quitter.reactangle.collidepoint(event.pos):
                    launched = False
                elif event.button == 1 and bouton_jouer.reactangle.collidepoint(event.pos):
                    launched = False
                    choix_mode = MODE_JOUER
                    break
                elif event.button == 1 and bouton_options.reactangle.collidepoint(event.pos):
                    launched = False
                    choix_mode = MODE_OPTIONS
                    break
        if launched == False:
            break
        pygame.display.flip()
    return choix_mode


def affichage_mode_jouer():

    taille = taille_ecran()
    window_surface = pygame.display.set_mode(taille)
    backgroud = pygame.image.load(FOND_ECRAN)
    backgroud.convert()
    window_surface.blit(backgroud, [0, 0])
    image_mode_jouer = tableau_image()

    bouton_titre_jouer = Boutton.Button(image_mode_jouer[0], image_mode_jouer[0], (taille[0]/2)-140, (taille[1]/2)-400,
                                        LONGUEUR_TITRE, LARGEUR_TITRE)
    bouton_titre_jouer.affichage_du_bouton(window_surface)

    bouton_jvj = Boutton.Button(image_mode_jouer[6], image_mode_jouer[6], (taille[0]/2)-50, (taille[1]/2)-30,
                                LONGUEUR_BOUTON_MENU, LARGEUR_BOUTON_MENU)
    bouton_jvj.affichage_du_bouton(window_surface)

    bouton_jvo = Boutton.Button(image_mode_jouer[6], image_mode_jouer[6], (taille[0]/2)-50, (taille[1]/2)+40,
                                LONGUEUR_BOUTON_MENU, LARGEUR_BOUTON_MENU)
    bouton_jvo.affichage_du_bouton(window_surface)

    bouton_retour = Boutton.Button(image_mode_jouer[7], image_mode_jouer[7],
                                   (taille[0]/12), (taille[1] - (taille[1]/6)), 75, 75)
    bouton_retour.affichage_du_bouton(window_surface)

    pygame.display.flip()
    launched = True
    while launched:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                launched = False


affichage_mode_jouer()
