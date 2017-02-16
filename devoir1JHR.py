# script python3, devoir1.py
#coding: utf-8
item1 = range(30000,100000)
for i in item1:
    print ('{num:05d}'.format(num=i))
item2 = range(0,18000)
for i in item2:
    print ('{num:05d}'.format(num=i))

### Ça fonctionne bien!
### Je ne connaissais pas ces options de la fonction «.format»! Merci! :)
### Encore mieux : imbriquer une boucle dans une autre comme je l'ai montré en classe :)