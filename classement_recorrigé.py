"""
Nom: WOWUI
Prénom: Kossi Martin
Age: 18 ans
Niveau: Première Année EPL
Titre du projet: DELIBERATION

"""
import sys
#création de structure eleve qui va permettre de manipuler les notes et rangs d'eleves


class Eleve:
    def __init__(self):
        self.nom = ""
        self.prenom = ""
        self.phys = 0.0
        self.math = 0.0
        self.ang = 0.0
        self.fr = 0.0
        self.svt = 0.0
        self.his_geo = 0.0
        self.moy = 0.0


# Création d'une fonction qui permet de remplir les champs de la structure
def remplir():
    e = Eleve()
    e.nom = input("\n Saisir le nom de l'eleve:")
    e.prenom = input(" Entrer son prénom:")
    while not e.nom or not e.prenom:
        print(" Le nom ou le prenom ne doit pas être vide ! Réessayez .")
        e.nom = input("\n Saisir le nom de l'eleve:")
        e.prenom = input(" Entrer son prénom")
    while True:
        try:
            e.phys = float(input(" entrer la note de physique:"))
            if not 0 <= e.phys <= 20:
                raise ValueError(" Les notes doivent être comprises entre 0 et 20")
            e.math = float(input(" entrer la note de maths:"))
            if not 0 <= e.math <= 20:
                raise ValueError(" Les notes doivent être comprises entre 0 et 20")
            e.ang = float(input(" entrer la note d'anglais:"))
            if not 0 <= e.ang <= 20:
                raise ValueError(" Les notes doivent être comprises entre 0 et 20")
            e.svt = float(input(" entrer la note de SVT:"))
            if not 0 <= e.svt <= 20:
                raise ValueError(" Les notes doivent être comprises entre 0 et 20")
            e.hg = float(input(" entrer la note de Histo_géo:"))
            if not 0 <= e.hg <= 20:
                raise ValueError(" Les notes doivent être comprises entre 0 et 20")
            e.fr = float(input(" entrer la note francais:"))
            if not 0 <= e.fr <= 20:
                raise ValueError(" Les notes doivent être comprises entre 0 et 20")
            print(" ENTREES AVEC SUCCES!")
            break
        except ValueError as ve:
            print(ve)
    return e



# fonction permettant de remplir les champs de tous les eleves
def remplir_tout(n):
    t = []
    for i in range(n):
        t.append(remplir())
    return t


# fonction permettant de calculer la moyenne de chaque eleve
def moyenne(e,t0):
    e.moy = ((t0[3]*e.phys +t0[0]*e.math + t0[2]*e.ang + t0[5]*e.svt + t0[4]*e.fr + t0[1]*e.hg) / sum(t0))
    return e

def coefficient(k):
    if k==0:
        sys.exit("NULL")
    while True:
       try:
           raison = 0
           t0 = []
           cm, ch, ca, cs, cf, csv = 0, 0, 0, 0, 0, 0
           cm = int(input("\n \n ENTRER LE COEFFICIENT DE MATHS : "))
           ch = int(input(" ENTRER LE COEFFICIENT DE HISTO_GEO : "))
           ca = int(input(" ENTRER LE COEFFICIENT D' ANGLAIS  :"))
           cs = int(input(" ENTRER LE COEFFICIENT DE PHYSIQUES : "))
           cf = int(input(" ENTRER LE COEFFICIENT DE FRANCAIS  :"))
           csv = int(input(" ENTRER LE COEFFICIENT DE SVT  :"))
           t0 = [cm, ch, ca, cs, cf, csv]
           break
       except:
           print(" Le coéfficient entré est incorrect!  Revérifier puis entrer les coéfficients normaux !")
    return t0


# la moyenne de tous les eleves
def moyenne_tout(t,t0):
    t2 = []
    for i in range(n):
        t2.append(moyenne(t[i],t0))
    return t2


# comparaison puis trie par rapport aux moyennes
def classement(t2):
    liste_finale = sorted(t2, key=lambda x: x.moy, reverse=True)
    return liste_finale

# fonction des mentions des eleves

def mention(e):
    return{
        e.moy>=16 : "TRES BIEN",
        14<=e.moy<16 : " BIEN",
        12 <= e.moy < 14 : " ASSEZ BIEN",
        10 <= e.moy < 12 : " PASSABLE",
        9 <= e.moy < 10 : " ADMISSIBLE",
        e.moy < 9 : " INSSUFFISANT ! "
    }[True]

# affichage des resultats
def affichage(liste_finale):
    for i in range(n):
         print(f" {i + 1} :{liste_finale[i].nom} {liste_finale[i].prenom} {liste_finale[i].moy}  avec mention : {mention(liste_finale[i])}")

# passons aux demandes puis aux calucls
print("   BONJOUR MONSIEUR ET SOYEZ LES BIENVENUES DANS NOTRE PROGRAMME.  \n   CE PROGRAMME PERMET DE TRAITER LES INFORMATIONS SUR DES ELEVES AUCOURS DES EVALUATIONS\n   DE CLASSE ET POURQUOI PAS EXAMENS . DANS CE DERNIER , VOUS AUREZ A FOUNIR LES  INFORMATIONS SUR LES ELEVES. \n  NB: IL S'AGIT D'UN PROGRAMME INFORMATIQUE : LES DONNEES ENTREES SONT IRREVERSIBLES. ")
while True:
    try:
       n = int(input(" \n  VEUILLEZ ENTRER L'EFFECTIF DES ELEVES SUR LESQUELS VOUS VOULEZ FAIRE LES TRAITEMENTS :"))
       break
    except:
       print(" L'effectif entré n'est pas correct !")
if n==0:
    print(" L'effectif est nul , on ne peut rien faire . Si c'était une erreur ,  Veuillez redémarrer le programme!  Merci pour la confiance.")
t = remplir_tout(n)
t0 = coefficient(n)
t2 = moyenne_tout(t, t0)
liste_finale = classement(t2)
affichage(liste_finale)
