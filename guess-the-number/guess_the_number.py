import random

for x in range (1):
    num_rand = random.randint(0,100)

cont = 5
adm = True

while adm == True:

    resp_user = input("Digite o seu numero de 0 a 100: ")
    if resp_user > num_rand:
        cont = cont - 1
        print("O seu numero e maior, tente de novo")
        print("Voce  tem {} tentativas".format(cont))
        if cont == 0:
            print ("Suas chances acabaram. :(")
            adm = False

    elif resp_user < num_rand:
        cont = cont - 1
        print("O seu numero e menor, tente de novo")
        print("Voce tem {} tentativas".format(cont))
        if cont == 0:
            print ("Suas chances acabaram. :(")
            adm = False
    elif resp_user == num_rand:
            print("Parabens! Voce acertou! :D")
            adm = False
