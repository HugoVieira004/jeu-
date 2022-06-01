import tkinter as tk
from tkinter import *
import csv # importation du module

po=[0,0,0,0,0,0,0]

fen = Tk()
fen.title('Projet de Elio, Hugo, Joan et Alexander')
w = 659
h = 659
ws = fen.winfo_screenwidth()
hs = fen.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
fen.geometry('%dx%d+%d+%d' % (w, h, x, y))
fen.resizable(False,False)



can = Canvas(fen, width=659, height=659, bg="silver")
j = can.create_oval(40, 40, 60, 60, fill="saddlebrown")


murs = [can.create_rectangle(0, 0, 660, 20, fill="grey"),  #mur haut
        can.create_rectangle(0,20, 20, 660, fill="grey"),  #murgauche
        can.create_rectangle(640,20, 660, 660, fill="grey"),  #murdroite
        can.create_rectangle(180,20, 200, 300, fill="grey"),  #murdroitesalle 1
        can.create_rectangle(20,280, 140, 300, fill="grey"),  #murbas salle 1
        can.create_rectangle(20,360, 140, 380, fill="grey"),  #murhaut salle 2
        can.create_rectangle(180,360, 200, 640, fill="grey"),  #murdroite salle 2
        can.create_rectangle(360,20, 380, 300, fill="grey"),  #mur droite salle 3
        can.create_rectangle(200,280, 320, 300, fill="grey"),  #mur bas salle 3
        can.create_rectangle(200,360, 320, 380, fill="grey"),  #mur haut salle4
        can.create_rectangle(360,360, 380, 640, fill="grey"),  #mur droite salle 4
        can.create_rectangle(460,20, 480, 160, fill="grey"),  #mur gauche salle 5
        can.create_rectangle(460,200, 640, 220, fill="grey"),  #mur bas salle 5
        can.create_rectangle(500, 220, 520, 320, fill="grey"),  #mur gauche salle 6
        can.create_rectangle(500, 320, 600, 340, fill="grey"),  #mur bas salle 6
        can.create_rectangle(460,420, 640, 440, fill="grey"),  #mur haut salle 7
        can.create_rectangle(460,440, 480, 600, fill="grey"),  #mur gauche salle 7
        can.create_rectangle(540,560, 560, 640, fill="grey"),  #mur gauche salle 8
        can.create_rectangle(560,560, 620, 580, fill="grey"),  #mur haut salle 8
        can.create_rectangle(20,640, 640, 660, fill="grey")]#murbas

#murs salle elio n°3
murse=[can.create_rectangle(200, 240, 260, 260, fill="chocolate"), #bureau prof
       can.create_rectangle(340, 20, 360, 200, fill="chocolate"), #bureau eleve mur
       can.create_rectangle(200, 80, 205, 200, fill="white"), #tableau
       can.create_rectangle(200, 20, 300, 40, fill="dimgrey"),#casier
       can.create_rectangle(240,80, 260, 120, fill="chocolate"),#bureau eleve 1G
       can.create_rectangle(240, 160, 260, 200, fill="chocolate"),#bureau eleve 1D
       can.create_rectangle(280, 80, 300, 120, fill="chocolate"),#bureau eleve 2G
       can.create_rectangle(280, 160, 300, 200, fill="chocolate"),#bureau eleve 2D
       can.create_rectangle(355, 20, 360, 200, fill="black"),# ordi
       can.create_rectangle(350, 20, 355, 200, fill="grey"),# ordi/ clavier
       can.create_rectangle(245, 185, 255, 195, fill="white"),  # ordi
       can.create_rectangle(285, 105, 295, 115, fill="white"),  # ordi
       can.create_rectangle(235, 245, 245, 255, fill="white"),  # ordi
       can.create_rectangle(210, 242, 230, 246, fill="black"),  # ordi prof
       can.create_rectangle(210, 246, 230, 249, fill="grey"),]  # ordi prof clavier

#murs salle elio extra n°5 directeur
murse=[can.create_rectangle(480, 20, 640, 40, fill="chocolate"),  #commode
       can.create_rectangle(480, 20, 500, 40, fill="saddlebrown"),  #pots de fleur
       can.create_rectangle(620, 20, 640, 40, fill="saddlebrown"),  #pots de fleur
       can.create_rectangle(482, 22, 498, 38, fill="limegreen"),  #fleur
       can.create_rectangle(622, 22, 638, 38, fill="limegreen"),  # fleur
       can.create_rectangle(520, 20, 600, 23, fill="black"),  #tv
       can.create_rectangle(500, 80, 505, 120, fill="tomato3"),  #canap P1 largeur
       can.create_rectangle(615, 80, 620, 120, fill="tomato3"),  # canap P2.2 largeur
       can.create_rectangle(505, 100, 615, 120, fill="chocolate"),  #canap P2 longeur
       can.create_rectangle(500, 115, 620, 120, fill="tomato3"),  #canap P2.2 longeur
       can.create_rectangle(505, 80, 520, 100, fill="chocolate"),  #canap small
       can.create_rectangle(600, 80, 615, 100, fill="chocolate"),  #canap small 2
       can.create_rectangle(620, 120, 640, 200, fill="chocolate"),  # table 1
       can.create_rectangle(540, 180, 640, 200, fill="chocolate"),  # table 2
       can.create_rectangle(560, 185, 570, 195, fill="sienna4"),  # point color  1
       can.create_rectangle(590, 185, 600, 195, fill="sienna4"),  # point color  2
       can.create_rectangle(625, 185, 635, 195, fill="wheat1"),  # point color  3
       can.create_rectangle(625, 155, 635, 165, fill="sienna2"),]  # point color 4

#murs salle elio salle quantique
mur_x = [can.create_rectangle(560, 220, 600, 240, fill="white"), #bureau
         can.create_rectangle(562, 222, 598, 224, fill="black"), #écran
         can.create_rectangle(564, 226, 596, 235, fill="grey40"), #clavier
         can.create_rectangle(600, 220, 640, 250, fill="grey40"), #serveur D
         can.create_rectangle(520, 220, 560, 250, fill="grey70"), #serveur G grey40
         can.create_rectangle(520, 290, 560, 320, fill="grey30"), #serveur GB
         can.create_rectangle(560, 300, 600, 320, fill="silver"), #casier
         ]

#murs salle hugo
mursh=[can.create_rectangle(220, 380, 300, 385, fill="white"),#tableau
       can.create_rectangle(200, 400, 240, 420, fill="chocolate"),#table prof
       can.create_rectangle(200, 460, 240, 480, fill="chocolate"),
can.create_rectangle(205, 465, 215, 475, fill="white"),#feuille1
       can.create_rectangle(200, 500, 240, 520, fill="chocolate"),
       can.create_rectangle(200, 540, 240, 560, fill="chocolate"),
       can.create_rectangle(200, 580, 240, 600, fill="chocolate"),
       can.create_rectangle(260, 460, 300, 480, fill="chocolate"),
       can.create_rectangle(260, 500, 300, 520, fill="chocolate"),
       can.create_rectangle(260, 540, 300, 560, fill="chocolate"),
       can.create_rectangle(260, 580, 300, 600, fill="chocolate"),
can.create_rectangle(265, 585, 275, 595, fill="white"),#feuille2
       can.create_rectangle(320, 460, 360, 480, fill="chocolate"),
       can.create_rectangle(320, 500, 360, 520, fill="chocolate"),
can.create_rectangle(325, 505, 335, 515, fill="white"),#feuille3
       can.create_rectangle(320, 540, 360, 560, fill="chocolate"),
       can.create_rectangle(320, 580, 360, 600, fill="chocolate"),
        can.create_rectangle(300, 620, 360, 640, fill="dimgrey"),#armoire
        can.create_rectangle(200, 620, 260, 640, fill="dimgrey")]#armoire



#acceuille
mursa=[can.create_rectangle(520,580, 540, 640, fill="dimgrey"),
       can.create_rectangle(540,440, 640, 460, fill="red"),
        can.create_rectangle(620,440, 640, 500, fill="red"),
        can.create_rectangle(635,440, 640, 500, fill="red"),
        can.create_rectangle(540,440, 545, 460, fill="red"),
       can.create_rectangle(620,495, 640, 500, fill="red"),
       can.create_rectangle(540,440, 640, 445, fill="red"),
        can.create_rectangle(540,540, 560, 560, fill="brown"),
       can.create_rectangle(600,540, 620, 560, fill="brown"),
        can.create_rectangle(545,545, 555, 555, fill="green"),
       can.create_rectangle(605,545, 615, 555, fill="green"),
        can.create_rectangle(480,440, 485, 500, fill="black"),
        can.create_rectangle(480,520, 500, 540, fill="brown"),
        can.create_rectangle(485,525, 495, 535, fill="green")]



# salle de joan

[can.create_rectangle(120, 380, 40, 385, fill="white")] #tableau
[can.create_rectangle(140, 480, 180, 460, fill="chocolate")] #bureau rangé de droite 1
[can.create_rectangle(140, 580, 180, 600, fill="chocolate")] #bureau rangé de droite 4
[can.create_rectangle(140, 500, 180, 520, fill="chocolate")] #bureau rangé de droite 2
[can.create_rectangle(140, 540, 180, 560, fill="chocolate")] #bureau rangé de droite 3
[can.create_rectangle(80, 400, 20, 420, fill="chocolate")] #bureau du prof
[can.create_rectangle(60, 480, 20, 460, fill="chocolate")] #bureau rangé de gauche 1
[can.create_rectangle(60, 500, 20, 520, fill="chocolate")] #bureau rangé de gauche 2
[can.create_rectangle(60, 580, 20, 600, fill="chocolate")] #bureau rangé de gauche 4
[can.create_rectangle(60, 540, 20, 560, fill="chocolate")] #bureau rangé de gauche 3
[can.create_rectangle(80, 580, 100, 600, fill="chocolate")] #bureau rangé du milieux 4
[can.create_rectangle(100, 580, 120, 600, fill="chocolate")] #bureau rangé du milieux 4
[can.create_rectangle(100, 540, 120, 560, fill="chocolate")] #bureau rangé du milieux 3
[can.create_rectangle(100, 540, 80, 560, fill="chocolate")] #bureau rangé du milieux 3
[can.create_rectangle(100, 500, 80, 520, fill="chocolate")] #bureau rangé du milieux 2
[can.create_rectangle(100, 500, 120, 520, fill="chocolate")] #bureau rangé du milieux 2
[can.create_rectangle(100, 480, 80, 460, fill="chocolate")] #bureau rangé du milieux 1
[can.create_rectangle(100, 480, 120, 460, fill="chocolate")] #bureau rangé du milieux 1
[can.create_rectangle(165, 585, 175, 598, fill="white")] #feuille énigme 1 rangé de droite
[can.create_rectangle(75, 402, 65, 415, fill="white")] #feuille énigme 2 sur le bureau du prof
[can.create_rectangle(55, 505, 45, 518, fill="white")] # feuille énigme 3 sur le bureau rangé de gauche 2



# salle de alexander

[can.create_rectangle(40, 179, 60, 199, fill="chocolate")] #bureau rangé de gauche 1
[can.create_rectangle(20, 179, 40, 199, fill="chocolate")] #bureau rangé de gauche 1
[can.create_rectangle(40, 139, 60, 159, fill="chocolate")] #bureau rangé de gauche 2
[can.create_rectangle(20, 139, 40, 159, fill="chocolate")] #bureau rangé de gauche 2
[can.create_rectangle(40, 99, 60, 119, fill="chocolate")] #bureau rangé de gauche 3
[can.create_rectangle(20, 99, 40, 119, fill="chocolate")] #bureau rangé de gauche 3
[can.create_rectangle(40, 59, 60, 79, fill="chocolate")] #bureau rangé de gauche 4
[can.create_rectangle(20, 59, 40, 79, fill="chocolate")] #bureau rangé de gauche 4
[can.create_rectangle(80, 179, 120, 199, fill="chocolate")] #bureau rangé du millieu 1
[can.create_rectangle(80, 139, 120, 159, fill="chocolate")] #bureau rangé du millieu 2
[can.create_rectangle(80, 99, 120, 119, fill="chocolate")] #bureau rangé du millieu 3
[can.create_rectangle(80, 59, 120, 79, fill="chocolate")] #bureau rangé du millieu 4
[can.create_rectangle(140, 179, 160, 199, fill="chocolate")] #bureau rangé de droite 1
[can.create_rectangle(160, 179, 180, 199, fill="chocolate")] #bureau rangé de droite 1
[can.create_rectangle(140, 139, 160, 159, fill="chocolate")] #bureau rangé de droite 2
[can.create_rectangle(160, 139, 180, 159, fill="chocolate")] #bureau rangé de droite 2
[can.create_rectangle(140, 99, 160, 119, fill="chocolate")] #bureau rangé de droite 3
[can.create_rectangle(160, 99, 180, 119, fill="chocolate")] #bureau rangé de droite 3
[can.create_rectangle(140, 59, 160, 79, fill="chocolate")] #bureau rangé de droite 4
[can.create_rectangle(160, 59, 180, 79, fill="chocolate")] #bureau rangé de droite 4
[can.create_rectangle(20, 239, 80, 259, fill="chocolate")] #bureau du prof
[can.create_rectangle(30, 242, 50, 246, fill="black"),]  #ordi prof
[can.create_rectangle(30, 246, 50, 249, fill="grey"),]  #clavier ordi prof
[can.create_rectangle(65, 242, 75, 255, fill="white")] #énigme 1
[can.create_rectangle(145, 142, 155, 155, fill="white")] #énigme 2
[can.create_rectangle(25, 102, 35, 115, fill="white")] #énigme 3
[can.create_rectangle(40, 275, 120, 280, fill="white")] #tableau


can.create_rectangle(480, 220, 500, 320, fill="black") #casier ext

can.pack()

grille = [[0] * 33 for i in range(33)]
x = 2
y = 2
grille[x][y] = 1



# casier ext
for i in range (11,16):
    grille[24][i]= 300

f = open ("csv.csv", "r") # ouverture du fichier
table = list ( csv . DictReader (f)) # creation de la table
f. close () # fermeture du fichier
for e in table:
    e['statut'] = int(e['statut'])

t1 = ([e for e in table if e["nom"]=="Porte 1"])[0]['statut']
t2 = ([e for e in table if e["nom"]=="Porte 2"])[0]['statut']
t3 = ([e for e in table if e["nom"]=="Porte 3"])[0]['statut']
t4 = ([e for e in table if e["nom"]=="Porte 4"])[0]['statut']
t5 = ([e for e in table if e["nom"]=="Porte 5"])[0]['statut']
t6 = ([e for e in table if e["nom"]=="Porte 6"])[0]['statut']
t7 = ([e for e in table if e["nom"]=="Porte 7"])[0]['statut']


grille[16][14]=t1#porte3
grille[17][14]=t1#porte3
grille[7][18]=t2#porte2
grille[8][18]=t2#porte2
grille[16][18]=t3#porte4
grille[17][18]=t3#porte4
grille[23][8]=t4#porte5
grille[23][9]=t4#porte5
grille[30][16]=t5#porte6
grille[31][16]=t5#porte6
grille[23][30]=t6#porte7
grille[23][31]=t6#porte7
grille[31][28]=t7#porte8

#portes
if grille[16][14]==3:
    porte3=can.create_rectangle(320,285, 360, 295, fill="tan")#porte3
if grille[7][18]==4:
    porte2=can.create_rectangle(140,365, 180, 375, fill="tan")#porte2
if grille[16][18]==5:
    porte4=can.create_rectangle(320,365, 360, 375, fill="tan")#porte4
if grille[23][8]==6:
    porte5=can.create_rectangle(465,160, 475, 200, fill="tan")#porte5
if grille[30][16]==7:
    porte6=can.create_rectangle(600,335, 640, 325, fill="tan")#porte6
if grille[23][31]==8:
    porte7=can.create_rectangle(465,600, 475, 640, fill="tan")#porte7
if grille[31][28]==9:
    porte8=can.create_rectangle(620,565, 640, 575, fill="tan")#porte8

# ----------------------------grille de la salle hugo
#tableau
grille[11][18] = 17
grille[12][18] = 17
grille[13][18] = 17
grille[14][18] = 17
#tprof
grille[10][20] = 2
grille[11][20] = 2
#feuille1 et t1
grille[10][23] = 14
grille[11][23] = 2
#t2
grille[10][25] = 2
grille[11][25] = 2
#t3
grille[10][27] = 2
grille[11][27] = 2
#t4
grille[10][29] = 2
grille[11][29] = 2
#t5
grille[13][23] = 2
grille[14][23] = 2
#t6
grille[13][25] = 2
grille[14][25] = 2
#t7
grille[13][27] = 2
grille[14][27] = 2
#t8
grille[13][29] = 15
grille[14][29] = 2
#t9
grille[16][23] = 2
grille[17][23] = 2
#t10
grille[16][25] = 16
grille[17][25] = 2
#t11
grille[16][27] = 2
grille[17][27] = 2
#t12
grille[16][29] = 2
grille[17][29] = 2
#armoire
grille[10][31] = 2
grille[11][31] = 2
grille[12][31] = 2
#armoire
grille[15][31] = 2
grille[16][31] = 2
grille[17][31] = 2

#----------------------------grille de la salle elio
    # bureau prof
for i in range(10,13):
    grille[i][12] = 10
    # bureau eleve
for i in range(1,10):
    grille[17][i] = 11
    #tableau
for i in range(4,10):
    grille[9][i] = 12
    #casier
for i in range(10,15):
    grille[i][1] = 13
    # bureau eleve 1G/D
for i in range(4,6):
    grille[12][i] = 2
    grille[14][i] = 2
    # bureau eleve 2G/D
for i in range(8,10):
    grille[12][i] = 2
    grille[14][i] = 2

#-------------------------------grille elio salle des prof
    # tv
for i in range (26,30):
    grille[i][1] = 18
for i in range (24,26):
    grille[i][1] = 2
for i in range (30,32):
    grille[i][1] = 2
    #canap1->3
for i in range (25,31):  #canap1
    grille[i][5] = 2
grille[25][4] = 2
grille[30][4] = 2
    # table 1/2
for i in range (6,10):
    grille[31][i] = 19
for i in range (27,32):
    grille[i][9] = 19

#-------------------------------grille de la salle de joan

#bureau du prof
grille[1][20] = 2
grille[2][20] = 2
grille[3][20] = 36

#rangé de gauche
#table1
grille[1][23] = 2
grille[2][23] = 2
#table 2
grille[1][25] = 2
grille[2][25] = 37
#table3
grille[1][27] = 2
grille[2][27] = 2
#table4
grille[1][29] = 2
grille[2][29] = 2

#rangé du milieu
#table1
grille[4][23] = 2
grille[5][23] = 2
#table2
grille[4][25] = 2
grille[5][25] = 2
#table3
grille[4][27] = 2
grille[5][27] = 2
#table4
grille[4][29] = 2
grille[5][29] = 2

#rangé de droite
#table1
grille[7][23] = 2
grille[8][23] = 2
#table2
grille[7][25] = 2
grille[8][25] = 2
#table3
grille[7][27] = 2
grille[8][27] = 2
#table4
grille[7][29] = 2
grille[8][29] = 33
grille[9][29] = 33


#-------------------------------grille de la salle de alexander

#bureau du prof
grille[1][12] = 43
grille[2][12] = 43
grille[3][12] = 40

#rangé de gauche
#table1
grille[1][9] = 2
grille[2][9] = 2
#table2
grille[1][7] = 2
grille[2][7] = 2
#table3
grille[1][5] = 41
grille[2][5] = 2
#table4
grille[1][3] = 2
grille[2][3] = 2

#rangé du millieu
#table1
grille[4][9] = 2
grille[5][9] = 2
#table2
grille[4][7] = 2
grille[5][7] = 2
#table3
grille[4][5] = 2
grille[5][5] = 2
#table4
grille[4][3] = 2
grille[5][3] = 2

#rangé de droite
#table1
grille[7][9] = 2
grille[8][9] = 2
#table2
grille[7][7] = 42
grille[8][7] = 2
#table3
grille[7][5] = 2
grille[8][5] = 2
#table4
grille[7][3] = 2
grille[8][3] = 2

#-------------------------grille ordi quantique
    # pc
grille[28][11]=25
grille[29][11]=25

    # serveur G
for i in range (26,28):
    grille[i][11]=2
    # serveur D
for i in range(30, 32):
    grille[i][11] = 2
    # serveur+casie
for i in range (26,30):
    grille[i][15]=2

#------------------------grille acceuille
for i in range(22,25):
    grille[31][i] = 2
for i in range(27,31):
    grille[i][22] = 2
grille[27][27] = 2
grille[30][27] = 20
grille[24][26] = 2
for i in range(29,32):
    grille[26][i] = 21
grille[31][29]= 1000
#-------------------------------grille_murs
for i in range(0,33):
    grille[i][0] = 2#blockmurhaut
    grille[0][i] = 2#blockmurgauche
    grille[32][i] = 2#blockmurdroite
    grille[i][32] = 2#blockmurbas

grille[9][1] = 2 #mur droite salle 1
grille[9][2] = 2 #mur droite salle 1
grille[9][3] = 2 #mur droite salle 1
grille[9][10] = 2 #mur droite salle 1
grille[9][11] = 2 #mur droite salle 1
grille[9][12] = 2 #mur droite salle 1
grille[9][13] = 2 #mur droite salle 1
grille[9][14] = 2 #mur droite salle 1
for i in range(1, 15):
    grille[18][i] = 2 #mur doite salle 3
for i in range(18, 32):
    grille[9][i] = 2#mur doite salle 2
    grille[18][i] = 2#mur doite salle 4
for i in range(1, 8):
    grille[23][i] = 2#mur gauche salle 5
for i in range(10, 16):
    grille[25][i] = 2#mur gauche salle 6
for i in range(22, 30):
    grille[23][i] = 2#mur gauche salle 7
for i in range(28, 33):
    grille[27][i] = 2#mur gauche salle 8
for i in range(1, 7):
    grille[i][14] = 2#mur bas salle 1
for i in range(10, 16):
    grille[i][14] = 2#mur bas salle 3
for i in range(1, 7):
    grille[i][18] = 2#mur haut salle 2
grille[10][18] = 2#mur haut salle 4
grille[15][18] = 2#mur haut salle 4
for i in range(23, 32):
    grille[i][10] = 2#mur bas salle 5
for i in range(25, 30):
    grille[i][16] = 2#mur bas salle 6
for i in range(23, 32):
    grille[i][21] = 2#mur haut salle 7
for i in range(28, 31):
    grille[i][28] = 2#mur haut salle 8

def droite(event):
    global x
    if grille[x + 1][y] == 0:
        grille[x][y] = 0
        x += 1
        grille[x][y] = 1
        can.move(j, 20, 0)

    elif grille[x+ 1][y] == 6:
        code4 = Tk()
        code4.resizable(False, False)
        code4.focus_force()
        L4 = Label(code4, text="Code")
        L4.pack(side=LEFT)
        E4 = Entry(code4, bd=5)
        E4.pack(side=LEFT)

        def verifier4():
            if E4.get() == "3246":
                can.delete(porte5)
                grille[23][8] = 0  # porte5
                grille[23][9] = 0  # porte5
                po[3]=2
                code4.destroy()

        b4 = Button(code4, bg="red",padx=9, command=lambda: verifier4())
        b4.pack(side=RIGHT)
        code4.mainloop()

    elif grille[x+ 1][y] == 8:
        code6 = Tk()
        code6.resizable(False, False)
        code6.focus_force()
        L6 = Label(code6, text="Code")
        L6.pack(side=LEFT)
        E6 = Entry(code6, bd=5)
        E6.pack(side=LEFT)
        def verifier6():
            if E6.get() == "3142":
                can.delete(porte7)
                grille[23][30] = 0  # porte7
                grille[23][31] = 0  # porte7
                po[5]=2
                code6.destroy()
        b6 = Button(code6, bg="red",padx=9, command=lambda: verifier6())
        b6.pack(side=RIGHT)
        code6.mainloop()
    #enigme ELio bureau eleve
    elif grille[x+1][y] == 11:
        app = Tk()
        labelExample = tk.Button(app, text="0")
        def change_label_number():
            counter = int(str(labelExample['text']))
            counter += 1
            labelExample.config(text=str(counter))
            if counter==163:
                counter = 0
                app.destroy()
                app2=Tk()
                appl = Label(app2, text="1er=9")
                appl.pack()
                app2.mainloop()
        buttonExample = tk.Button(app, text="cliquer", width=30,command=change_label_number)
        buttonExample.pack()
        labelExample.pack()
        app.mainloop()

# enigme Elio extra table à manger  salle des prof
    elif grille[x+1][y] == 19:
        EE3 = tk.Tk()
        lab = tk.Label(EE3, text="Vous voyez un oeuf mollet sur la table et vous")
        lab.pack(side=TOP)
        lab_2 = tk.Label(EE3, text="vous demander combien de temps il a fallu pour le cuire")
        lab_2.pack(side=TOP)

        def OnButtonClick(button_id):
            if button_id == 1:
                EE3.destroy()
                EE3_2 = Tk()
                lab = Label(EE3_2, text="1er=10")
                lab.pack(side=TOP)
            elif button_id == 2 or button_id == 3:
                EE3.destroy()
                EE3_2 = Tk()
                lab = Label(EE3_2, text="dommage")
                lab.pack(side=TOP)
                EE3_2.after(5000,lambda: EE3_2.destroy())

        BEE3_1 = Button(EE3, bg="red", text="3min", command=lambda: OnButtonClick(2))
        BEE3_1.pack()
        BEE3_2 = Button(EE3, bg="red",  text="6min", command=lambda: OnButtonClick(1))
        BEE3_2.pack()
        BEE3_3 = Button(EE3, bg="red",  text="9min", command=lambda: OnButtonClick(3))
        BEE3_3.pack()

        EE3.resizable(False, False)

    # enigme acceuille armoire
    elif grille[x + 1][y] == 21:
        EE10 = Tk()
        EE10.configure(bg="silver")
        EE10.focus_force()
        can17 = Canvas(EE10, width=500, height=500, bg="white")
        can17.pack(side=TOP)
        EE10.resizable(False, False)
        im6 = PhotoImage(file='eh6.gif', master=EE10)
        logo6 = can17.create_image(250, 288, image=im6)
        Ecan17 = Entry(EE10, bd=5)
        Ecan17.pack(side=BOTTOM)

        def verifiercan17():
            if Ecan17.get() == "une carte":
                EE10.destroy()
                EE10v2 = Tk()
                labEE10v2 = Label(EE10v2, text="1er=83")
                labEE10v2.pack(side=TOP)

        bcan17 = Button(EE10, bg="red", padx=9, command=lambda: verifiercan17())
        bcan17.pack(side=BOTTOM)
        EE10.mainloop()
        # sauvegarde
    elif grille[x + 1][y] == 300:
        EE300 = Tk()
        EE300.configure(bg="silver")
        EE300.focus_force()
        EE300.resizable(False, False)

        def verifiercan300():
            def valide(e):
                nom = e['nom']
                statut = e['statut']
                return {'nom':nom, 'statut':statut}
            table_valide = [valide(e) for e in table]

            if po[0]==2:
                table_valide[0]['statut'] = 0
            if po[1]==2:
                table_valide[1]['statut'] = 0
            if po[2]==2:
                table_valide[2]['statut'] = 0
            if po[3]==2:
                table_valide[3]['statut'] = 0
            if po[4]==2:
                table_valide[4]['statut'] = 0
            if po[5]==2:
                table_valide[5]['statut'] = 0
            if po[6]==2:
                table_valide[6]['statut'] = 0

            f = open('csv.csv', 'w+')
            w = csv.DictWriter(f, ['nom', 'statut'])
            w.writeheader()
            w.writerows(table_valide)
            f.close()
            EE300.destroy()
            fen.destroy()

        bcan300 = Button(EE300, bg="red", padx=9, command=lambda: verifiercan300())
        bcan300.config (text = "sauvegarder et quitter")
        bcan300.pack(side=BOTTOM)
        EE300.mainloop()

    #enigme 1 alexander table rangé droitew
    elif grille[x + 1][y] == 42:
        EA = Tk()
        EA.configure(bg="silver")
        EA.focus_force()
        can42 = Canvas(EA, width=500, height=450, bg="silver")
        can42.pack(side=TOP)
        EA.resizable(False, False)
        photo = PhotoImage(file='ea1.gif.', master=EA)
        logo7 = can42.create_image(250, 288, image=photo)
        Jcan42 = Entry(EA, bd=5)
        Jcan42.pack(side=BOTTOM)

        b6 = Button(EA, bg="red", width=5, command=lambda: verifier42())
        b6.pack(side=BOTTOM)

        def verifier42():
            if Jcan42.get() == "116 ans":
                EA.destroy()
                EA1 = Tk()
                appl = Label(EA1, text="3eme=0")
                appl.pack()
                EA1.mainloop()

        EA.mainloop()
def gauche(event):
    global x
    if grille[x - 1][y] == 0:
        grille[x][y] = 0
        x -= 1
        grille[x][y] = 1
        can.move(j, -20, 0)

       # enigme elio tableau
    elif grille[x - 1][y] == 12:
        EE2 = Tk()
        can111 = Canvas(EE2, width=500, height=500, bg="white")
        can111.pack(side=TOP)
        img = PhotoImage(file="EE2.gif", master=EE2)
        logo1 = can111.create_image(250, 200, image=img)
        EE2.resizable(False, False)

        EE2_1 = Entry(EE2, bd=5, bg= "white")
        EE2_1.pack(side=BOTTOM )
        EE2_2 = Entry(EE2, bd=5,bg= "white" )
        EE2_2.pack(side=BOTTOM)
        EE2_3 = Entry(EE2, bd=5,bg= "white")
        EE2_3.pack(side=BOTTOM)
        EE2_4 = Entry(EE2, bd=5,bg= "white")
        EE2_4.pack(side=BOTTOM)

        def verifier6():
            if EE2_1.get() == "linéaire" and EE2_2.get() == "quadratique" and EE2_3.get() == "cubique" and EE2_4.get() == "logarithmique" :
                EE2.destroy()
                EE2__1 = Tk()
                appl = Label(EE2__1, text="2eme=2")
                appl.pack()
                EE2__1.mainloop()
        b6 = Button(EE2, bg="red",width=5, command=lambda: verifier6())
        b6.pack(side=BOTTOM)
        EE2.mainloop()

    # enigme acceuille fleur
    elif grille[x-1][y ] == 20:
        EE9 = Tk()
        EE9.configure(bg="silver")
        EE9.focus_force()
        can16 = Canvas(EE9, width=500, height=500, bg="white")
        can16.pack(side=TOP)
        EE9.resizable(False, False)
        im5 = PhotoImage(file='eh5.gif', master=EE9)
        logo5 = can16.create_image(250, 288, image=im5)
        Ecan16 = Entry(EE9, bd=5)
        Ecan16.pack(side=BOTTOM)

        def verifiercan16():
            if Ecan16.get() == "tulipe":
                EE9.destroy()
                EE9v2 = Tk()
                labEE9v2 = Label(EE9v2, text="2eme=39")
                labEE9v2.pack(side=TOP)

        bcan16 = Button(EE9, bg="red", padx=9, command=lambda: verifiercan16())
        bcan16.pack(side=BOTTOM)
        EE9.mainloop()

#enigme 3 alexander bureau prof
    elif grille[x - 1][y] == 40:
        EA = Tk()
        EA.configure(bg="silver")
        EA.focus_force()
        can40 = Canvas(EA, width=500, height=450, bg="silver")
        can40.pack(side=TOP)
        EA.resizable(False, False)
        photo = PhotoImage(file='ea3.gif', master=EA)
        logo7 = can40.create_image(250, 288, image=photo)
        Jcan40 = Entry(EA, bd=5)
        Jcan40.pack(side=BOTTOM)

        b6 = Button(EA, bg="red", width=5, command=lambda: verifier40())
        b6.pack(side=BOTTOM)

        def verifier40():
            if Jcan40.get() == "Barack Obama":
                EA.destroy()
                EA3 = Tk()
                appl = Label(EA3, text="2eme=2")
                appl.pack()
                EA3.mainloop()

        EA.mainloop()

def bas(event):
    global y
    if grille[x][y + 1] == 0:
        grille[x][y] = 0
        y += 1
        grille[x][y] = 1
        can.move(j, 0, 20)
    elif grille[x][y + 1] == 4:
        code2 = Tk()
        code2.resizable(False, False)
        code2.focus_force()
        L2 = Label(code2, text="Code")
        L2.pack(side=LEFT)
        E2 = Entry(code2, bd=5)
        E2.pack(side=LEFT)

        def verifier2():
            if E2.get() == "8339":
                can.delete(porte2)
                grille[7][18] = 0  # porte2
                grille[8][18] = 0  # porte2
                po[1]=2
                code2.destroy()

        b2 = Button(code2, bg="red", padx=9,command=lambda : verifier2())
        b2.pack(side=RIGHT)
        code2.mainloop()

    elif grille[x][y + 1] == 5:
        code3 = Tk()
        code3.resizable(False, False)
        code3.focus_force()
        L3 = Label(code3, text="Code")
        L3.pack(side=LEFT)
        E3 = Entry(code3, bd=5)
        E3.pack(side=LEFT)

        def verifier3():
            if E3.get() == "1020":
                can.delete(porte4)
                grille[16][18] = 0  # porte4
                grille[17][18] = 0  # porte4
                po[2]=2
                code3.destroy()

        b3 = Button(code3, bg="red",padx=9, command=lambda : verifier3())
        b3.pack(side=RIGHT)
        code3.mainloop()

    elif grille[x][y + 1] == 9:
        code7 = Tk()
        code7.resizable(False, False)
        code7.focus_force()
        L7 = Label(code7, text="Code")
        L7.pack(side=LEFT)
        E7 = Entry(code7, bd=5)
        E7.pack(side=LEFT)

        def verifier7():
            if E7.get() == "6468":
                can.delete(porte8)
                grille[31][28] = 0  # porte8
                po[6]=2
                code7.destroy()

        b7 = Button(code7, bg="red",padx=9,command=lambda : verifier7())
        b7.pack(side=RIGHT)
        code7.mainloop()
    # enigme ELio extra table à manger  salle des prof
    elif grille[x ][y+1] == 19:
        EE3 = tk.Tk()
        lab = tk.Label(EE3, text="Vous voyez un oeuf mollet sur la table et vous")
        lab.pack(side=TOP)
        lab_2 = tk.Label(EE3, text="vous demandez combien de temps il a fallu pour le cuire")
        lab_2.pack(side=TOP)

        def OnButtonClick(button_id):
            if button_id == 1:
                EE3.destroy()
                EE3_2 = Tk()
                lab = Label(EE3_2, text="2eme=10")
                lab.pack(side=TOP)
            elif button_id == 2:
                EE3.destroy()
                EE3_2 = Tk()
                lab = Label(EE3_2, text="dommage")
                lab.pack(side=TOP)
                EE3_2.after(5000,lambda: EE3_2.destroy())

        BEE3_1 = Button(EE3, bg="red", text="3min", command=lambda: OnButtonClick(2))
        BEE3_1.pack()
        BEE3_2 = Button(EE3, bg="red",  text="6min", command=lambda: OnButtonClick(1))
        BEE3_2.pack()
        BEE3_3 = Button(EE3, bg="red",  text="9min", command=lambda: OnButtonClick(2))
        BEE3_3.pack()

        EE3.resizable(False, False)


    # énigme 2 joan feuille sur le bureau du prof
    elif grille[x][y + 1] == 36:
        EJ = Tk()
        EJ.configure(bg="silver")
        EJ.focus_force()
        can36 = Canvas(EJ, width=500, height=450, bg="silver")
        can36.pack(side=TOP)
        EJ.resizable(False, False)
        photo = PhotoImage(file='EJ2.gif', master=EJ)
        logo6 = can36.create_image(250, 288, image=photo)
        Jcan36 = Entry(EJ, bd=5)
        Jcan36.pack(side=BOTTOM)

        b6 = Button(EJ, bg="red", width=5, command=lambda: verifier6())
        b6.pack(side=BOTTOM)

        def verifier6():
            if Jcan36.get() == "59":
                EJ.destroy()
                EJ2__1 = Tk()
                appl = Label(EJ2__1, text="1er=6")
                appl.pack()
                EJ2__1.mainloop()
        EJ.mainloop()

#enigme 1 alexander table rangé droite
    elif grille[x][y + 1] == 42:
        EA = Tk()
        EA.configure(bg="silver")
        EA.focus_force()
        can42 = Canvas(EA, width=500, height=450, bg="silver")
        can42.pack(side=TOP)
        EA.resizable(False, False)
        photo = PhotoImage(file='ea1.gif.', master=EA)
        logo7 = can42.create_image(250, 288, image=photo)
        Jcan42 = Entry(EA, bd=5)
        Jcan42.pack(side=BOTTOM)

        b6 = Button(EA, bg="red", width=5, command=lambda: verifier42())
        b6.pack(side=BOTTOM)

        def verifier42():
            if Jcan42.get() == "116 ans":
                EA.destroy()
                EA1 = Tk()
                appl = Label(EA1, text="3eme=0")
                appl.pack()
                EA1.mainloop()

        EA.mainloop()
#enigme 2 alexander table rangé gauche
    elif grille[x][y + 1] == 41:
        EA = Tk()
        EA.configure(bg="silver")
        EA.focus_force()
        can41 = Canvas(EA, width=500, height=450, bg="silver")
        can41.pack(side=TOP)
        EA.resizable(False, False)
        photo = PhotoImage(file='ea2.gif', master=EA)
        logo7 = can41.create_image(250, 288, image=photo)
        Jcan41 = Entry(EA, bd=5)
        Jcan41.pack(side=BOTTOM)

        b6 = Button(EA, bg="red", width=5, command=lambda: verifier41())
        b6.pack(side=BOTTOM)

        def verifier41():
            if Jcan41.get() == "Tegucigalpa":
                EA.destroy()
                EA2 = Tk()
                appl = Label(EA2, text="4eme=9")
                appl.pack()
                EA2.mainloop()

        EA.mainloop()

#enigme 3 alexander bureau prof
    elif grille[x][y + 1] == 40:
        EA = Tk()
        EA.configure(bg="silver")
        EA.focus_force()
        can40 = Canvas(EA, width=500, height=450, bg="silver")
        can40.pack(side=TOP)
        EA.resizable(False, False)
        photo = PhotoImage(file='ea3.gif', master=EA)
        logo7 = can40.create_image(250, 288, image=photo)
        Jcan40 = Entry(EA, bd=5)
        Jcan40.pack(side=BOTTOM)

        b6 = Button(EA, bg="red", width=5, command=lambda: verifier40())
        b6.pack(side=BOTTOM)

        def verifier40():
            if Jcan40.get() == "Barack Obama":
                EA.destroy()
                EA3 = Tk()
                appl = Label(EA3, text="2eme=2")
                appl.pack()
                EA3.mainloop()
        EA.mainloop()
    elif grille[x][y + 1] == 1000:
        fin = Tk()
        wfin = 659
        hfin = 659
        wsfin = fin.winfo_screenwidth()
        hsfin = fin.winfo_screenheight()
        xfin = (wsfin / 2) - (wfin / 2)
        yfin = (hsfin / 2) - (hfin / 2)
        fin.geometry('%dx%d+%d+%d' % (wfin, hfin, xfin, yfin))
        fin.configure(bg="silver")
        fin.focus_force()
        canfin = Canvas(fin, width=660, height=660, bg="silver")
        canfin.pack()
        fin.resizable(False, False)
        photofin = PhotoImage(file='fin.gif', master=fin)
        logofin = canfin.create_image(335, 335, image=photofin)
        fen.destroy()

        def valide(e):
            nom = e['nom']
            statut = e['statut']
            return {'nom':nom, 'statut':statut}
        table_valide = [valide(e) for e in table]

        table_valide[0]['statut'] = 3
        table_valide[1]['statut'] = 4
        table_valide[2]['statut'] = 5
        table_valide[3]['statut'] = 6
        table_valide[4]['statut'] = 7
        table_valide[5]['statut'] = 8
        table_valide[6]['statut'] = 9

        f = open('csv.csv', 'w+')
        w = csv.DictWriter(f, ['nom', 'statut'])
        w.writeheader()
        w.writerows(table_valide)

        fin.mainloop()



def haut(event):
    global y
    if grille[x][y - 1] == 0:
        grille[x][y] = 0
        y -= 1
        grille[x][y] = 1
        can.move(j, 0, -20)
    elif grille[x][y - 1] == 3:
        code1 = Tk()
        code1.resizable(False, False)
        code1.focus_force()
        L1 = Label(code1, text="Code")
        L1.pack(side=LEFT)
        E1 = Entry(code1, bd=5)
        E1.pack(side=LEFT)
        def verifier1():
            if E1.get() == "4209":
                can.delete(porte3)
                grille[16][14] = 0  # porte3
                grille[17][14] = 0  # porte3
                po[0]=2
                code1.destroy()
        b1 = Button(code1, bg="red",padx=9,command=lambda : verifier1())
        b1.pack(side=RIGHT)
        code1.mainloop()

    elif grille[x][y - 1] == 7:
        code5 = Tk()
        code5.resizable(False, False)
        code5.focus_force()
        L5 = Label(code5, text="Code")
        L5.pack(side=LEFT)
        E5 = Entry(code5, bd=5)
        E5.pack(side=LEFT)
        def verifier5():
            if E5.get() == "9279":
                can.delete(porte6)
                grille[30][16] = 0  # porte6
                grille[31][16] = 0  # porte6
                po[4]=2
                code5.destroy()
        b5 = Button(code5, bg="red",padx=9,command=lambda : verifier5())
        b5.pack(side=RIGHT)
        code5.mainloop()

        # enigme 3 elio bureau prof
    elif grille[x][y - 1] == 10:
        EE3 = tk.Tk()
        lab = tk.Label(EE3, text="ETEZ VOUS UN ROBOT ")
        lab.pack(side=TOP)
        def OnButtonClick(button_id):
            if button_id == 1:
                EE3.destroy()
                EE3_2 = Tk()
                lab = Label(EE3_2, text="3eme=79 ")
                lab.pack(side=TOP)
            elif button_id == 2:
                EE3.destroy()
                EE3_2 = Tk()
                lab = Label(EE3_2, text="ETEZ VOUS SÛR??")
                lab.pack(side=TOP)
                def OnButtonClick2(button_id2):
                    if button_id2 == 1:
                        EE3_2.destroy()
                        EE3_3 = Tk()
                        lab = Label(EE3_3, text="3eme=79")
                        lab.pack(side=TOP)
                    elif button_id2 == 2:
                        EE3_2.destroy()
                BEE3_1 = Button(EE3_2, bg="red", padx=9, text="NON", command=lambda: OnButtonClick2(1))
                BEE3_1.pack(side=RIGHT)
                BEE3_2 = Button(EE3_2, bg="red", padx=9, text="OUI", command=lambda: OnButtonClick2(2))
                BEE3_2.pack(side=LEFT)
        BEE3_1 = Button(EE3, bg="red", padx=9, text="NON", command=lambda: OnButtonClick(2))
        BEE3_1.pack(side=RIGHT)
        BEE3_2 = Button(EE3, bg="red", padx=9, text="OUI", command=lambda: OnButtonClick(1))
        BEE3_2.pack(side=LEFT)
        EE3.resizable(False, False)

    # enigme tableau hugo
    elif  grille[x][y-1] == 17:
        EE5 = Tk()
        EE5.configure(bg='silver')
        EE5.focus_force()
        can12 = Canvas(EE5, width=500, height=500, bg='white')
        can12.pack(side=TOP)
        EE5.resizable(False, False)
        im = PhotoImage(file='eh1.gif', master=EE5)
        logo1 = can12.create_image(250, 288, image=im)
        Ecan12 = Entry(EE5, bd=5)
        Ecan12.pack(side=BOTTOM)
        def verifiercan12():
            if Ecan12.get() == "30":
                EE5.destroy()
                EE5v2=Tk()
                labEE5v2 = Label(EE5v2, text="1er=3")
                labEE5v2.pack(side=TOP)
        bcan12 = Button(EE5, bg="red", padx=9, command=lambda: verifiercan12())
        bcan12.pack(side=BOTTOM)
        EE5.mainloop()

    # enigme feuille1 hugo
    elif  grille[x][y-1] == 14:
        EE6 = Tk()
        EE6.configure(bg="silver")
        EE6.focus_force()
        can13 = Canvas(EE6, width=500, height=500, bg="white")
        can13.pack(side=TOP)
        EE6.resizable(False, False)
        im2 = PhotoImage(file='eh2.gif', master=EE6)
        logo2 = can13.create_image(250, 288, image=im2)
        Ecan13 = Entry(EE6, bd=5)
        Ecan13.pack(side=BOTTOM)
        def verifiercan13():
            if Ecan13.get() == "strictement croissante":
                EE6.destroy()
                EE6v2 = Tk()
                labEE6v2 = Label(EE6v2, text="2eme=1")
                labEE6v2.pack(side=TOP)
        bcan13 = Button(EE6, bg="red", padx=9, command=lambda: verifiercan13())
        bcan13.pack(side=BOTTOM)
        EE6.mainloop()
    # enigme feuille2 hugo
    elif  grille[x][y-1] == 15:
        EE7 = Tk()
        EE7.configure(bg="silver")
        EE7.focus_force()
        can14 = Canvas(EE7, width=500, height=500, bg="white")
        can14.pack(side=TOP)
        EE7.resizable(False, False)
        im3 = PhotoImage(file='eh3.gif', master=EE7)
        logo3 = can14.create_image(250, 288, image=im3)
        Ecan14 = Entry(EE7, bd=5)
        Ecan14.pack(side=BOTTOM)
        def verifiercan14():
            if Ecan14.get() == "3":
                EE7.destroy()
                EE7v2 = Tk()
                labEE7v2 = Label(EE7v2, text="2eme=4")
                labEE7v2.pack(side=TOP)
        bcan14 = Button(EE7, bg="red", padx=9, command=lambda: verifiercan14())
        bcan14.pack(side=BOTTOM)
        EE7.mainloop()
    # enigme feuille3 hugo
    elif  grille[x][y-1] == 16:
        EE8 = Tk()
        EE8.configure(bg="silver")
        EE8.focus_force()
        can15 = Canvas(EE8, width=500, height=500, bg="white")
        can15.pack(side=TOP)
        EE8.resizable(False, False)
        im4 = PhotoImage(file='eh4.gif', master=EE8)
        logo4 = can15.create_image(250, 288, image=im4)
        Ecan15 = Entry(EE8, bd=5)
        Ecan15.pack(side=BOTTOM)
        def verifiercan15():
            if Ecan15.get() == "888+88+8+8+8":
                EE8.destroy()
                EE8v2 = Tk()
                labEE8v2 = Label(EE8v2, text="4eme=2 ")
                labEE8v2.pack(side=TOP)
        bcan15 = Button(EE8, bg="red", padx=9, command=lambda: verifiercan15())
        bcan15.pack(side=BOTTOM)
        EE8.mainloop()

    # enigme Elio extrat   salle des prof tv
    elif grille[x][y - 1] == 18:
        EEX = Tk()
        EEX.resizable(False, False)
        #creation d'un canvas
        canX = Canvas(EEX, width=500, height=250, bg="black")
        canX.pack(side=TOP)
        #importe l'image + l'insere dans le canvas
        img = PhotoImage(file="EEX1.gif", master=EEX)
        lgx = canX.create_image(250, 200, image=img)

        EE2_1 = Entry(EEX, bd=5, bg="silver")
        EE2_1.pack(side=BOTTOM)
        def verifier6():
            if EE2_1.get() == "l'inverse d'un trou noir":
                EEX.destroy()
                EE2__1 = Tk()
                appl = Label(EE2__1, text="2eme=20")
                appl.pack()
                EE2__1.mainloop()

        b6 = Button(EEX, bg="red", width=5, command=lambda: verifier6())
        b6.pack(side=BOTTOM)
        EEX.mainloop()
    # enigme salle des ordi
    elif grille[x][y - 1] == 25:
        EO = Tk()
        EO.resizable(False, False)
        E_0 = Button(EO, bg="red", text="Question 1", command=lambda: OnButtonClick_2(1))
        E_0.pack()
        E_1 = Button(EO, bg="red", text="Question 2", command=lambda: OnButtonClick_2(2))
        E_1.pack()
        def OnButtonClick_2(button_id):
            if button_id == 1:
                EO.destroy()
                EO_2 = Tk()
                canO = Canvas(EO_2, width=500, height=500, bg="black")
                canO.pack(side=TOP)
                EO_2.resizable(False, False)
                img = PhotoImage(file="EO1.gif", master=EO_2)
                lg_O = canO.create_image(250, 250, image=img)
                EO_21 = Entry(EO_2, bd=5, bg="silver")
                EO_21.pack(side=BOTTOM)

                def verifier6():
                    if EO_21.get() == "les deux":
                        EO_2.destroy()
                        EO_22 = Tk()
                        appl = Label(EO_22, text="1er=3246")
                        appl.pack()
                        EO_22.mainloop()

                b_0 = Button(EO_2, bg="red", width=5, command=lambda: verifier6())
                b_0.pack(side=BOTTOM)
                EO_2.mainloop()

            if button_id == 2:
                EO.destroy()
                EO_2 = Tk()
                canO = Canvas(EO_2, width=500, height=250, bg="black")
                canO.pack(side=TOP)
                EO_2.resizable(False, False)
                img = PhotoImage(file="EO2.gif", master=EO_2)
                lg_O = canO.create_image(250, 200, image=img)
                EO_21 = Entry(EO_2, bd=5, bg="silver")
                EO_21.pack(side=BOTTOM)

                def verifier6():
                    if EO_21.get() == "ERROR":
                        EO_2.destroy()
                        EO_22 = Tk()
                        appl = Label(EO_22, text="1er=3246")
                        appl.pack()
                        EO_22.mainloop()

                b_0 = Button(EO_2, bg="red", width=5, command=lambda: verifier6())
                b_0.pack(side=BOTTOM)
                EO_2.mainloop()


    # énigme 1 joan feuille sur la rangée de droite

    elif grille[x][y - 1] == 3:
        code1 = Tk()
        code1.resizable(False, False)
        code1.focus_force()
        L1 = Label(code1, text="Code")
        L1.pack(side=LEFT)
        E1 = Entry(code1, bd=5)
        E1.pack(side=LEFT)
        def verifier1():
            if E1.get() == "4209":
                can.delete(porte3)
                grille[16][14] = 0  # porte3
                grille[17][14] = 0  # porte3
                code1.destroy()

        b1 = Button(code1, bg="red", padx=9, command=lambda: verifier1())
        b1.pack(side=RIGHT)
        code1.mainloop()

    elif grille[x][y-1] == 33:
        EJ1 = tk.Tk()
        lab = tk.Label(EJ1, text=" Quelle est la bonne traduction de : ")
        lab.pack(side=TOP)
        lab_2 = tk.Label(EJ1, text=" I am filled with determination ")
        lab_2.pack(side=TOP)
        def OnButtonClick(button_id):
            if button_id == 2:
                    EJ1.destroy()
                    EJ1_2 = Tk()
                    lab = Label(EJ1_2, text="2eme=4")
                    lab.pack(side=TOP)
            elif button_id == 1 or button_id == 3:
                    EJ1.destroy()
                    EJ1_2 = Tk()
                    lab = Label(EJ1_2, text="try again")
                    lab.pack(side=TOP)
                    EJ1_2.after(5000, lambda: EJ1_2.destroy())

        BEJ1_1 = Button(EJ1, bg="red", text="j'ai besoin de détermination", command=lambda: OnButtonClick(1))
        BEJ1_1.pack()
        BEJ1_2 = Button(EJ1, bg="red", text="je suis empli de détermination", command=lambda: OnButtonClick(2))
        BEJ1_2.pack()
        BEJ1_3 = Button(EJ1, bg="red", text="j'ai plein de détermination", command=lambda: OnButtonClick(3))
        BEJ1_3.pack()

        EJ1.resizable(False, False)
        EJ1.mainloop()


    #énigme 3 joan (bureau rangé de gauche)
    elif grille[x][y - 1] == 37:
        EJ = Tk()
        EJ.configure(bg="silver")
        EJ.focus_force()
        can37 = Canvas(EJ, width=500, height=450, bg="silver")
        can37.pack(side=TOP)
        EJ.resizable(False, False)
        photo = PhotoImage(file='EJ3.gif', master=EJ)
        logo7 = can37.create_image(250, 288, image=photo)
        Jcan37 = Entry(EJ, bd=5)
        Jcan37.pack(side=BOTTOM)

        b6 = Button(EJ, bg="red", width=5, command=lambda: verifier6())
        b6.pack(side=BOTTOM)

        def verifier6():
            if Jcan37.get() == "42":
                EJ.destroy()
                EJ3__1 = Tk()
                appl = Label(EJ3__1, text="3eme=6")
                appl.pack()
                EJ3__1.mainloop()
        EJ.mainloop()
#enigme 1 alexander table rangé droite
    elif grille[x][y - 1] == 42:
        EA = Tk()
        EA.configure(bg="silver")
        EA.focus_force()
        can42 = Canvas(EA, width=500, height=450, bg="silver")
        can42.pack(side=TOP)
        EA.resizable(False, False)
        photo = PhotoImage(file='ea1.gif.', master=EA)
        logo7 = can42.create_image(250, 288, image=photo)
        Jcan42 = Entry(EA, bd=5)
        Jcan42.pack(side=BOTTOM)

        b6 = Button(EA, bg="red", width=5, command=lambda: verifier42())
        b6.pack(side=BOTTOM)

        def verifier42():
            if Jcan42.get() == "116 ans":
                EA.destroy()
                EA1 = Tk()
                appl = Label(EA1, text="3eme=0")
                appl.pack()
                EA1.mainloop()

        EA.mainloop()

#enigme 2 alexander table rangé gauche
    elif grille[x][y - 1] == 41:
        EA = Tk()
        EA.configure(bg="silver")
        EA.focus_force()
        can41 = Canvas(EA, width=500, height=450, bg="silver")
        can41.pack(side=TOP)
        EA.resizable(False, False)
        photo = PhotoImage(file='ea2.gif', master=EA)
        logo7 = can41.create_image(250, 288, image=photo)
        Jcan41 = Entry(EA, bd=5)
        Jcan41.pack(side=BOTTOM)

        b6 = Button(EA, bg="red", width=5, command=lambda: verifier41())
        b6.pack(side=BOTTOM)

        def verifier41():
            if Jcan41.get() == "Tegucigalpa":
                EA.destroy()
                EA2 = Tk()
                appl = Label(EA2, text="4eme=9")
                appl.pack()
                EA2.mainloop()

        EA.mainloop()

# enigme 3 alexander bureau prof
    elif grille[x][y - 1] == 40:
        EA = Tk()
        EA.configure(bg="silver")
        EA.focus_force()
        can40 = Canvas(EA, width=500, height=450, bg="silver")
        can40.pack(side=TOP)
        EA.resizable(False, False)
        photo = PhotoImage(file='ea3.gif', master=EA)
        logo7 = can40.create_image(250, 288, image=photo)
        Jcan40 = Entry(EA, bd=5)
        Jcan40.pack(side=BOTTOM)

        b6 = Button(EA, bg="red", width=5, command=lambda: verifier40())
        b6.pack(side=BOTTOM)

        def verifier40():
            if Jcan40.get() == "Barack Obama":
                EA.destroy()
                EA3 = Tk()
                appl = Label(EA3, text="2eme=2")
                appl.pack()
                EA3.mainloop()

        EA.mainloop()

#enigme 4 alexander ordi prof
    elif grille[x][y - 1] == 43:
        EA = Tk()
        EA.configure(bg="silver")
        EA.focus_force()
        can43 = Canvas(EA, width=500, height=450, bg="silver")
        can43.pack(side=TOP)
        EA.resizable(False, False)
        photo = PhotoImage(file='ea4.gif', master=EA)
        logo7 = can43.create_image(250, 250, image=photo)
        Jcan43 = Entry(EA, bd=5)
        Jcan43.pack(side=BOTTOM)

        b6 = Button(EA, bg="red", width=5, command=lambda: verifier43())
        b6.pack(side=BOTTOM)

        def verifier43():
            if Jcan43.get() == "le Vatican":
                EA.destroy()
                EA4 = Tk()
                appl = Label(EA4, text="1er=4")
                appl.pack()
                EA4.mainloop()

        EA.mainloop()


can.focus_force()

can.bind("d", droite)
can.bind("a", gauche)
can.bind("w", haut)
can.bind("s", bas)


fen.mainloop()
f. close () # fermeture du fichier