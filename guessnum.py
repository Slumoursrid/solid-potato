import random

hasard = random.randint(1,20)
essai = 1
essai_max = 6

for nombre in range(hasard):
    quest_rep = "J'ai un nombre en tete entre 1 et 20 choisi:"
    number_user = int(input(quest_rep))
    if number_user == nombre:
        print("bravo")
    elif number_user != nombre:
        print("mauvaise réponse, réessai")
        if number_user > 20 or number_user < 1:
            print("le nombre que j'ai en tete ne peux etre plus petit que 1 e plus grand que 20")
        essai += 1
        if essai <= essai_max:
            print("réessai")
        elif essai > essai_max:
            print("tu n'as plus de tour, le nombre auquel je pensais était" ,nombre)