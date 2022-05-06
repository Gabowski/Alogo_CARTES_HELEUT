
class Carte :                                                             # La classe Carte

    def __init__(self,Mana,Nom,Description,Attributs,Fonctions):          # Ses vars
        self._mana = Mana
        self._nom = Nom
        self._description = Description
        self._attributs = Attributs
        self._fonctions = Fonctions

    def afficheNameCarte(self):
        return(self._nom)
    
    def afficheManaCarte(self):
        return(self._mana)

    def afficheDescriptionCarte(self):
        return(self._description)

    def afficheAttributsCarte(self):
        return(self._attributs)

    def afficheFonctionsCarte(self):
        return(self._fonctions)


class Mage :                                                                  # La classe Mage

    def __init__(self,name,pv,mana,zone,defausse,main,manatotal):             # Ses vars
        self._nom = name
        self._hp = pv
        self._Mana = mana
        self._Zone = zone
        self._out = defausse
        self._totalmana = manatotal
        self._Main = main
        self._tour = 0
        self._carte = [Carte("Sven",15,"un puissant mage de vent","tornade\n"),Carte("Njörd",10,"fils du Jarl Ragnar et mage de la foudre","éclairs\n")]  # Les cartes
        self._hpEnnemie = 30

    def afficheNJ(self):
        print(self._nom, end = " ")

    def manaJ(self):
        return(self._Mana)
    
    def tourJeu(self):
        self._tour += 1
        return self._tour

    def pvJ(self):
        return(self._hp)

    def defausseCarte(self):          
        self._out = self._out + 1
        return self._out

    def partieGagnee(self):                                           # Fonction pour partie gagnée
        win = False
        if(self._hpEnnemie <= 0 ):
            win = True
            print("Féilicitations, vous avez gagné !")
    
    def partiePerdu(self):                                            # Fonction pour partie perdue
        defeat = False
        if(self._hp <= 0 ):
            defeat = True
            print("Dommage, vous avez perdu...")

    def mainJ(self):                                                  # Nombre de mana total
        self._Main = 100
        return self._Main
    
    def playCarte(self):                                              # Fonction pour jouer
        print("Voici vos cartes",self._carte)
        self._tour +=1
        firstchoice = int(input("Quelle carte voulez vous jouer?"))
        if(firstchoice == "Sven"):
            if(self._Mana != 15):
                print("Vous ne pouvez pas jouer cette carte, car vous n'avez pas assez de mana")
            else:
                print("Vous avez choisi la carte Sven")
                self._Mana = self._Mana - 15
        if(firstchoice == "Njörd"):
            if(self._Mana != 10):
                print("Vous ne pouvez pas jouer cette carte, car vous n'avez pas assez de mana")
            else:
                print("Vous avez choisi la carte Njörd")
                self._Mana = self._Mana - 10
        if(firstchoice == "cristal"):
            self._Mana = self._Mana + 5
            print("Vous avez regagné de la mana grace au cristal")

    def play(self):                                                 # Fonction qui continue le jeu en fonction du nombre de tour
        while(self._tour<3 and not self.partieGagnee()):
            self.playCarte()
    
class Cristal(Carte):                                               # La classe Cristal

    def __init__(self,valeur):                                      # Ses vars
        self._value = valeur
        Carte.__init__(self._mana,"cristal",", il vous permet de regagner de la mana au cours de la partie")

class Creature(Carte):                                              # La classe Creature

    def __init__(self,pv,scoreATK,mana):                            # Ses vars
        self._hp = pv
        self._attack = scoreATK
        Carte.__init__(self._mana,"creature",", vous pouvez jouer une creature contre de la mana")

class Blast(Carte):                                                 # La classe Blast

    def __init__(self,valeur,defausse):                             # Ses vars
        self._value = valeur
        self._out = defausse
    
    def defausseCarte(self):
        self._out = self._out + 1
        return self._out

myGame = Mage
myGame.play()