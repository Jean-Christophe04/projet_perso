import pygame


class Button:

    def __init__(self, image, coordone_x, coordone_y, largeur, longueur):
        self.point_x = coordone_x
        self.point_y = coordone_y

        self.reactangle = pygame.Rect(coordone_x, coordone_y, largeur, longueur)

        self.chargement_image = pygame.image.load(image)
        self.image_affiche = pygame.transform.scale(self.chargement_image, (int(largeur), int(longueur)))

    def affichage_du_bouton(self, fenetre):
        fenetre.blit(self.image_affiche, (self.point_x, self.point_y))


