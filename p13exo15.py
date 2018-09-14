ji = 460
yi = 350
bi = 190

parti = [460, 350, 190]

somme = ji + yi+ bi

participationJi = ji * 100 / somme
participationYi = yi * 100 / somme
participationBi = bi * 100 / somme



somme = 0
for i in range (0,3) :
    print (parti[i])
    somme = somme + parti [i]
    print (somme)

for i in range (0,3) :
    print (parti[i] * 100 / somme)