import random

gramy = "tak"

podane = []
wylosowane = []

while gramy == "tak":
    for i in range(6):

        takiejJeszczeNieMa = 1
        podana = 0;
        while takiejJeszczeNieMa == 1:
            podana = int(input("Podaj liczbę numer "+str(i+1)+": "))
            for i in podane:
                if i == podana:
                    takiejJeszczeNieMa = 0;
        podane.append(podana)
        takiejJeszczeNieMa = 1
        wylosowana = 0;
        while takiejJeszczeNieMa == 1:
            wylosowana = random.randint(1,50)
            for i in wylosowane:
                if i == wylosowana:
                    takiejJeszczeNieMa = 0;
        wylosowane.append(wylosowana)
    trafione = 0
    for z in podane:
        for j in wylosowane:
            if z == j:
                trafione = trafione + 1

    print("Twój wynik to: "+str(trafione))
    print("Wylosowane liczby: ")
    for i in wylosowane:
        print(i)
    podane.clear()
    wylosowane.clear()
    gramy = input("Czy chcesz zagrać jeszcze raz? (tak/nie) ")
