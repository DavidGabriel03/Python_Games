import random
#varianta de joc pe care le avem
choices=[
    "foarfeca",
    "piatra",
    "hartie"
]
#numarul de runde castigate consecutiv
runda=1
#numarul de victorii dorit
target=(int)(input("Pana la ce numar de victorii vrei sa ajungi?"))
while True:
    print("Runda ",runda)
    #aici introduci varianta de joc
    user=input("Alege (piatra/foarfeca/hartie): ").lower()
    #aici adversarul alege varianta de joc
    comp=random.choice(choices)
    #rezultatul jocului
    if user==comp:
        print("Egalitate")
        print("Adversarul a ales :",comp)
    elif( ( user=="foarfeca" and comp=="hartie")or \
    (user=="hartie" and comp=="piatra") or  \
    (user=="piatra" and comp=="foarfeca")):
        print("Ai castigat")
        #crestem rundele si afisam ce a avut adversarul pentru debug
        runda+=1
        print("Adversarul a ales :",comp)
    else:
        print("Ai pierdut")
        #resetam rundele si afisam ce a avut adversarul pentru debug
        runda=1
        print("Adversarul a ales :",comp)
    
    if runda-1==target :
        #jocul se termina
        print("You won!!!!")
        break
    if input("You still wanna play?(yes/no)").lower()!="yes":
        break