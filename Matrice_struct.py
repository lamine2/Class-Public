
#!/usr/bin/python

# Importation des packages utiles pour creer les fonctions
import numpy as np
import pandas as pd 

# Cette fonction permet de revenir en arriere en faisant quelques verifications
# Il prend en parametres la structure et une indice
def forward(stc,i):
    # initialisation des variables locales
    k = 1
    go = 1
    out = 0
    # On verifie si l'element qui se trouve à la ieme position sur la structure
    # est egale à une parenthese ouvrante
    if(stc[i]=="("):
        # si la condition evoquée au dessus est vefifiée alors on incremente l'indice 
        i=i+1
        # on parcours tout les elements de la structure en commencant par indice + 1
        for j in range(i,len(stc)) :
            # Cette condition sera toujours verifié au premiere passage
            if(go==1):
                # On verifie si l'element qui se trouve à la jeme position sur la structure
                # est egale à une parenthese fermente
                if(stc[j]==")"):
                    # si la condition est verifée alors 
                    # on decremente la variable k
                    k=k-1
                    # si la condition precedente est verifiée alors la variable out prend la 
                    # valeur de l'indice j pour qu'on suite continuer la verification de l'ensemble des elements
                    # de la structure
                    if(k==0):
                        out=j
                        # on reinitialise la variable locale
                        go=0
                    # Sinon si k != 0 alors ca veut dire que l'element qui se trouve à l'indice j 
                    # n'est pas egale à une parenthese fermente
                    # alors on verifie si c'est egale à une parenthese ouvrante
                    elif stc[j]=="(" :
                        # si la condition est vraie alors on incremente k
                        k=k+1
    # on retourne  valeur de l'indice pour faire la meme verrification pour toute la structure
    return out


# Cette fonction permet de parcourir en faisant quelques verifications
# Il prend en parametres la structure et une indice
def backward(stc,i):
    # initialisation des variables locales
    k = 1
    go = 1
    out = 0
    # On verifie si l'element qui se trouve à la ieme position sur la structure
    # est egale à une parenthese fermente
    if(stc[i]==")"):
        # si c'est le cas on decremente l'indice pour recuperer la valeur de l'element qui precede
        i=i-1
        # on parcours tout les elements de la structure en commencant par indice - 1
        for j in range(i,1) :
            # Cette condition sera toujours verifié au premiere passage
            if(go==1):
                # On verifie si l'element qui se trouve à la jeme position sur la structure
                # est egale à une parenthese ouvrante
                if(stc[j]=="("):
                    # si la condition est verifée alors 
                    # on decremente la variable k
                    k=k-1
                    # si la condition precedente est verifiée alors la variable out prend la 
                    # valeur de l'indice j pour qu'on puisse  continuer la verification de l'ensemble des elements
                    # de la structure
                    if(k==0):
                        out=j
                        go=0
                # Sinon si stc[j] != "(" alors ca veut dire que l'element qui se trouve à l'indice j 
                # n'est pas egale à une parenthese ouvrante
                # alors on verifie si c'est egale à une parenthese fermente
                elif(stc[j]==")"):
                    k=k+1
    # on retourne de valeur de l'indice pour faire la meme verification pour toute la structure
    return out



# Cette fonction permet de faire appel au autre fonction pour creer la matrice de la structure
# Il prend 2 parametres la structure et la sequence
def mat_struct(struct, seq):
    # Cette fonction permet de creer un tableau qui contient les caracteres de la sequence
    nts = seq.split()
    # Cette ligne de code permet de recuperer le premier caractere de la sequence
    nts = nts[0]
    # Cette fonction permet de creer un tableau qui contient les caracteres de la structure
    stc = struct.split()
    # Cette ligne de code permet de recuperer le premier caractere de la structure
    stc = stc[0]
    # On cree plusieurs liste pour contenir les informations de la matrice de structure
    first_position = []
    before =  []
    after = []
    sequence = []
    second_position = []
    bound = []
    # On parcours une boucle allant de 1 jusqu'à la taille de la structure
    # C'est dans cette boucle que la matrice de structure est crée
    for i in range(1,len(stc)):
        # On recupere le premier elelment de la sequence avec sa position et toutes les autres informations
        first_position.append(i)
        before.append(i-1)
        after.append(i+1)
        sequence.append(nts[i])
        second_position.append(i)
        # Si l'element qui se trouve à la ieme position est egale à un "." alors 
        # on a une liaison
        if stc[i] == "." :
            bound.append(0)
        # Sinon si l'element qui se trouve à la ieme position est egqle à une parenthese fermente alors 
        elif stc[i] == ")":
            # Cette fonction permet de retourner la position de l'element qui est en liaision avec l'element
            # se trouvant à la ieme position
            b = backward(stc,i)
            # on ajoute la liaison
            bound.append(b)
        elif(stc[i]=="("):
            # Cette fonction permet de retourner la position de l'element qui est en liaision avec l'element
            # se trouvant à la ieme position
            b = forward(stc,i)
            # on ajoute la liaison
            bound.append(b)
    # cette partie nous permet de creer le tableau dataframe
    df = pd.DataFrame(columns=['First Position', 'Before', 'After','Sequence','Second Position','Bound'])
    df['First Position'] = first_position
    df['Before'] = before
    df['After'] = after
    df['Sequence'] = sequence
    df['Second Position'] = second_position
    df['Bound'] = bound
    # on retourne la matrice
    return df