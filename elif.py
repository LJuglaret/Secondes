type = input ()
poids = float (input())

if (type == "verte" ) :
    if (poids <= 20) :
        print (0.57)
    elif (poids <=50) :
        print (0.95)
    elif (poids <= 100) :
        print (1.40)

elif (type == "prioritaire") :
    if (poids <= 20) :
        print (0.60)
    elif (poids <=50) :
        print (1.00)
    elif (poids <= 100) :
        print (1.45)

elif (type == "ecopli"):
    if (poids <= 20) :
        print (0.55)
    elif (poids <=50) :
        print (0.78)
    elif (poids <= 100) :
        print (1.00)


#Exemple
#verte 5


# attention, ici les mauvaises saisies ne sont pas prises en compte.