import pygame, thorpy
import Boutton

FOND_JEUX = "/home/chalaud/Bureau/git/projet_perso/interface_graphique_python/ressources/image/fond-jeux.jpg"

def tableau_image():
    tab_image = [
        "/home/chalaud/Bureau/git/projet_perso/interface_graphique_python/ressources/image/titre.jpeg",
        "/home/chalaud/Bureau/git/projet_perso/interface_graphique_python/ressources/image/play.jpg",
        "/home/chalaud/Bureau/git/projet_perso/interface_graphique_python/ressources/image/settings.jpg",
        "/home/chalaud/Bureau/git/projet_perso/interface_graphique_python/ressources/image/exit.jpg",
        "/home/chalaud/Bureau/git/projet_perso/interface_graphique_python/ressources/image/sound_ON.png",
        "/home/chalaud/Bureau/git/projet_perso/interface_graphique_python/ressources/image/sound_OFF.png",
        "/home/chalaud/Bureau/git/projet_perso/interface_graphique_python/ressources/image/jouer1.jpg",
        "/home/chalaud/Bureau/git/projet_perso/interface_graphique_python/ressources/image/retour.jpeg",
        "/home/chalaud/Bureau/git/projet_perso/interface_graphique_python/ressources/image/image_test.jpg",
        "/home/chalaud/Bureau/git/projet_perso/interface_graphique_python/ressources/image/verso_carte.jpg"

    ]
    return tab_image

def taille_ecran():
    fenetre = pygame.display.set_mode()
    x, y = fenetre.get_size()
    tab_size = [x, y]
    pygame.display.quit()

    return tab_size

pygame.init()

def affichage_age1():
    taille = taille_ecran()
    window_surface = pygame.display.set_mode(taille)
    backgroud = pygame.image.load(FOND_JEUX)
    backgroud.convert()
    window_surface.blit(backgroud, [0, 0])
    image_carte = tableau_image()

    bouton_carte1 = Boutton.Button(image_carte[8], image_carte[8], (taille[0] / 2) - 260, (taille[1] / 2) - 400,
                                   90, 140)
    bouton_carte1.affichage_du_bouton(window_surface)

    bouton_carte2 = Boutton.Button(image_carte[8], image_carte[8], (taille[0] / 2) - 160, (taille[1] / 2) - 400,
                                   90, 140)
    bouton_carte2.affichage_du_bouton(window_surface)

    bouton_carte3 = Boutton.Button(image_carte[8], image_carte[8], (taille[0] / 2) - 60, (taille[1] / 2) - 400,
                                   90, 140)
    bouton_carte3.affichage_du_bouton(window_surface)

    bouton_carte4 = Boutton.Button(image_carte[8], image_carte[8], (taille[0] / 2) + 40, (taille[1] / 2) - 400,
                                   90, 140)
    bouton_carte4.affichage_du_bouton(window_surface)

    bouton_carte5 = Boutton.Button(image_carte[8], image_carte[8], (taille[0] / 2) + 140, (taille[1] / 2) - 400,
                                   90, 140)
    bouton_carte5.affichage_du_bouton(window_surface)

    bouton_carte6 = Boutton.Button(image_carte[8], image_carte[8], (taille[0] / 2) + 240, (taille[1] / 2) - 400,
                                   90, 140)
    bouton_carte6.affichage_du_bouton(window_surface)

    bouton_carte7 = Boutton.Button(image_carte[9], image_carte[9], (taille[0] / 2) - 210, (taille[1] / 2) - 340,
                                   90, 140)
    bouton_carte7.affichage_du_bouton(window_surface)

    bouton_carte8 = Boutton.Button(image_carte[9], image_carte[9], (taille[0] / 2) - 110, (taille[1] / 2) - 340,
                                   90, 140)
    bouton_carte8.affichage_du_bouton(window_surface)

    bouton_carte9 = Boutton.Button(image_carte[9], image_carte[9], (taille[0] / 2) - 10, (taille[1] / 2) - 340,
                                   90, 140)
    bouton_carte9.affichage_du_bouton(window_surface)

    bouton_carte10 = Boutton.Button(image_carte[9], image_carte[9], (taille[0] / 2) + 90, (taille[1] / 2) - 340, 90, 140)
    bouton_carte10.affichage_du_bouton(window_surface)

    bouton_carte11 = Boutton.Button(image_carte[9], image_carte[9], (taille[0] / 2) + 190, (taille[1] / 2) - 340, 90, 140)
    bouton_carte11.affichage_du_bouton(window_surface)

    bouton_carte12 = Boutton.Button(image_carte[8], image_carte[8], (taille[0] / 2) - 160, (taille[1] / 2) - 280, 90, 140)
    bouton_carte12.affichage_du_bouton(window_surface)

    bouton_carte13 = Boutton.Button(image_carte[8], image_carte[8], (taille[0] / 2) - 60, (taille[1] / 2) - 280, 90, 140)
    bouton_carte13.affichage_du_bouton(window_surface)

    bouton_carte14 = Boutton.Button(image_carte[8], image_carte[8], (taille[0] / 2) + 40, (taille[1] / 2) - 280,
                                   90, 140)
    bouton_carte14.affichage_du_bouton(window_surface)

    bouton_carte15 = Boutton.Button(image_carte[8], image_carte[8], (taille[0] / 2) + 140, (taille[1] / 2) - 280,
                                   90, 140)
    bouton_carte15.affichage_du_bouton(window_surface)

    bouton_carte16 = Boutton.Button(image_carte[9], image_carte[9], (taille[0] / 2) - 110, (taille[1] / 2) - 220,
                                   90, 140)
    bouton_carte16.affichage_du_bouton(window_surface)

    bouton_carte17 = Boutton.Button(image_carte[9], image_carte[9], (taille[0] / 2) - 10, (taille[1] / 2) - 220,
                                   90, 140)
    bouton_carte17.affichage_du_bouton(window_surface)

    bouton_carte18 = Boutton.Button(image_carte[9], image_carte[9], (taille[0] / 2) + 90, (taille[1] / 2) - 220,
                                    90, 140)
    bouton_carte18.affichage_du_bouton(window_surface)

    bouton_carte19 = Boutton.Button(image_carte[8], image_carte[8], (taille[0] / 2) - 60, (taille[1] / 2) - 160,
                                    90, 140)
    bouton_carte19.affichage_du_bouton(window_surface)

    bouton_carte20 = Boutton.Button(image_carte[8], image_carte[8], (taille[0] / 2) +40, (taille[1] / 2) - 160,
                                    90, 140)
    bouton_carte20.affichage_du_bouton(window_surface)

    pygame.display.flip()
    launched = True
    while launched:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                launched = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and bouton_carte20.reactangle.collidepoint(event.pos):
                    bouton_carte20.reactangle.unblit()


#affichage_age1()




def lol():
    pygame.init()
    pygame.key.set_repeat(300, 30)
    screen = pygame.display.set_mode((400,400))
    screen.fill((255,255,255))
    rect = pygame.Rect((0, 0, 50, 50))
    rect.center = screen.get_rect().center
    clock = pygame.time.Clock()

    pygame.draw.rect(screen, (255,0,0), rect)
    pro = thorpy.Image(FOND_JEUX)

    pygame.display.flip()

    #declaration of some ThorPy elements ...
    slider = thorpy.SliderX(100, (12, 35), "My Slider")
    button = thorpy.make_button("Quit", func=thorpy.functions.quit_func)
    box = thorpy.Box(elements=[slider,button])

    #we regroup all elements on a menu, even if we do not launch the menu
    menu = thorpy.Menu(box)

    #important : set the screen as surface for all elements
    for element in menu.get_population():
        element.surface = screen

    #use the elements normally...
    box.set_topleft((100,100))
    box.blit()
    box.update()
    screen.blit(pro, [10, 10])
    pygame.display.flip()
    playing_game = True
    while playing_game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing_game = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pygame.draw.rect(screen, (255,255,255), rect) #delete old
                    pygame.display.update(rect)
                    rect.move_ip((-5,0))
                    pygame.draw.rect(screen, (255,0,0), rect) #drat new
                    pygame.display.update(rect)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    screen.unblit(pro)
            menu.react(event) #the menu automatically integrate your elements
    pygame.display.flip()

    pygame.quit()

lol()