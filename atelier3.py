class Vecteur2D:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def affichage(self):
        print(self.x)
        print(self.y)
    def addition(self,V2D):
        x=self.x+V2D.x
        y=self.y+V2D.y
        
        print("la somme de la vecteur","(",self.x,",",self.y,")","et la vecteur","(",V2D.x,",",V2D.y,")","est la vecteur","("+str(x)+","+str(y)+"",")")

class Rectangle:
    def __init__(self,longeur=0,largeur=0,nom="rectangle"):
        self.longeur=longeur
        self.largeur=largeur
        self.nom=nom
    def surface(self):
        return self.longeur*self.largeur
    def affichage(self,surface=0):
        if surface==0:
             print(" il n'y a pas de rectangle")
        else:
         print("la surface de ce rectangle est:",surface)

class carre(Rectangle):
     def __init__(self, cote):
        super().__init__(cote, cote)
        self.nom = "carré"
        def surface(self):
             return self.cote**2

     def affichage(self,surface=0):
        if surface==0:
             print(" il n'y a pas de rectangle")
        else:
         print("la surface de ce rectangle est:",surface)

class Point:
    def __init__(self,x=0.0,y=0.0):
        self.x=x
        self.y=y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Segment:
    def __init__(self, x1, y1, x2, y2):
        self.orig = Point(x1, y1)
        self.extrem = Point(x2, y2)

    def __str__(self):
        return f"Segment de l'origine {self.orig} à l'extremité {self.extrem}"

    

vecteur1=Vecteur2D()
vecteur2=Vecteur2D(3,4)
vecteur3=Vecteur2D(5,7)

print("affichage sans parametre")
print(vecteur1.x)
print(vecteur1.y)

print("affichage avec parametre")

print(vecteur2.x)
print(vecteur2.y)

print("affichage avec methode d'affichage")
vecteur2.affichage()
vecteur1.affichage()
print("affichage de la somme de deux vecteur :")

vecteur2.addition(vecteur3)
rec1=Rectangle() # rectange sans parametre
rec1.affichage()

rec2=Rectangle(4,5) # rectange sans parametre
rec2.affichage(rec2.surface())

c1= carre(5)
r1=Rectangle(3,5)
print(c1.nom)
print(r1.surface())

print(c1.surface())

s=Segment(1,2,3,4)
print(s)

