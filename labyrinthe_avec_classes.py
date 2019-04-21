class Labyrinthe:

    def __init__(self):
        self.robot = 'X'
        self.Labyrinthe = []


    def labyrinthe(self, fichier):
        with open(fichier, 'r') as une_carte:
            for line in une_carte:
                liste = line.strip()
                self.Labyrinthe.append(list(liste))
        return self.Labyrinthe

    def afficher_labyrinthe(self):
        for line in self.Labyrinthe:
            print(''.join(line))




continuer_partie = True

while continuer_partie:
    print("Labyrinthes existants :")
    print("  1- facile\n  2- prison")

    choix_labyrinthe = True

    while choix_labyrinthe:
        numero = input('Entrez un numéro de labyrinthe pour commencer à jouer : ')

        try:
            numero = int(numero)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            continue
