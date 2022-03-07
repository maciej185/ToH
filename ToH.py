import os 
from time import sleep

licznik = 0
steps = []

def TOH(n, s, peg_from, peg_to, helpers = None):
    
    global licznik
    global steps
    
    if helpers == None:
        helpers = []
        
        for i in range(2, s):
            helpers.append(i)
    if n == 0:
        
        return
    
    if n <= s - 3:
        
        for i in reversed(range(n - 1)):
            #print('Z', peg_from, 'na', helpers[i])
            steps.append((peg_from, helpers[i]))
            licznik +=1
            
        #print('Z', peg_from, 'na', peg_to)
        steps.append((peg_from, peg_to))
        licznik +=1
        
        for i in range(n - 1):
            #print('Z', helpers[i], 'na', peg_to)
            steps.append((helpers[i], peg_to))
            licznik +=1
        return
 
    peg_to_new = helpers[-1]
    helpers.pop(len(helpers) - 1)
    helpers.append(peg_to)
    
    TOH(n - (s - 2), s, peg_from, peg_to_new, helpers)
    
    helpers.pop(len(helpers) - 1)
    
    helpers_new = helpers[::-1]
    helpers_new = helpers[:s - 3]
    
    for i in range(len(helpers_new)):
        if peg_from != helpers_new[i]:
        
            #print('Z', peg_from, 'na', helpers_new[i])
            steps.append((peg_from, helpers_new[i]))
            licznik +=1
        
    #print('Z', peg_from, 'na', peg_to)
    steps.append((peg_from, peg_to))
    licznik +=1
    
    helpers_new = helpers_new[::-1]
    
    for i in range(len(helpers_new)):
        if peg_to != helpers_new[i]:
            
            #print('Z', helpers_new[i], 'na', peg_to)
            steps.append((helpers_new[i], peg_to))
            licznik +=1

    helpers.append(peg_from)
    
    TOH(n - (s - 2), s , peg_to_new, peg_to, helpers)



#pobranie wartości od użytkownika 
ile_kr = int(input("Podaj liczbę krążków: "))
#nalezy podac minimum 3 dla liczby slupkow
while True:
    ile_sl = int(input("Podaj liczbą słupków: "))
    if ile_sl < 3:
        print("Liczba słupków mninmum 3!")
    elif ile_sl > 8:
        print("Liczba słupków maks 8!")
    else:
        break

#utworzenie listy słupków 
slupki = [[0 for _ in range(ile_kr)] for i in range(ile_sl)]

#modyfikacja pierwszego słupka tak, kolejne wartości odzwierciedlały szerokość krążków
slupki[0] = [i for i in range(1, ile_kr + 1)]

#wywolanie funkcji wypelnia tablice lista krokow 
TOH(ile_kr, ile_sl, 1, ile_sl)

#drukowanie poczatkowego polozenia krazkow 
'''
#srednia wersja, slupki drukuja sie jeden pod drugim

# drukowanie kolejnych słupków
for i in range(ile_sl):
    # drukowanie kolejnych poziomów słupków
    for j in range(1, ile_kr + 2):
        #print(j)
        #ostatni poziom, trzeba 'dodrukować' podstawę
        if j == (ile_kr + 1):

            for z in range(1, 2*(ile_kr + 1) + 1):
                if z == ile_kr + 1:
                    print("_|", end = "")
                elif z == 2*(ile_kr + 1):
                    print("_", end = "\n")
                else:
                    print("_", end = "")

        else:

            for z in range(1, 2*(ile_kr + 1) + 1):

                if z == ile_kr + 1:
                    print(" |", end = "")
                elif z == 2*(ile_kr + 1):
                    print(" ", end = "\n")
                else:
                    print(" ", end = "")

    print("\n")
'''
#wersja numer dwa

os.system("cls")

#PETLA NIE DRUKUJE OSTATNIEGO KROKU

#petla po liscie krokow
for step in range(len(steps)):

    
    #drukowanie kolejnych poziomow, jest ich ile_kr + 1
    for j in range(1, ile_kr + 2):
        #szerokość kazdego poziomu, tj. 'liczba slupkow' x '(2 * (liczba krazkow + 1) )'
        licz = 0 
        poz = 0
        for i in range(1, (ile_sl)*(2*(ile_kr + 1)) + 1):
            #zmienna informujaca, 'na' ktorym slupku jestem

            ktory = licz + 1
            #zmienna mowiaca, w krorej 'komorce' danego slupka jestem 
        
            poz = poz % (2*(ile_kr + 1))
            poz +=1

            #update licznika co każde 2*(ile_kr + 1)
            if i % (2 * (ile_kr + 1)) == 0:
                licz += 1

            #środek słupka
            if i == licz*(2*(ile_kr + 1)) + (ile_kr + 1):

                if j == ile_kr + 1:
                    print("_|",end = "")
                else:
                    if slupki[ktory - 1][j - 1] != 0:
                        print("_|", end = "")
                        
                    else:
                        print(" |", end = "")
                
            #koniec słupka
            elif i % (2* (ile_kr + 1)) == 0:
                if j == ile_kr + 1:
                    print("_", end = "  ")
                else:
                    print(" ", end  = "  ")

            #pozostałe miejsca 
            else:
                if j == ile_kr + 1:
                    print("_", end = "")
                else:
                    #zlozony warunek logiczny na sprawdzenie, czy na aktualnie rysowanej pozycji powinien znalezc sie element krazka
                    if slupki[ktory - 1][j - 1] != 0 and ((poz < (ile_kr + 1) and poz >= ile_kr + 2 - slupki[ktory - 1][j -1] ) or  \
                        (poz > (ile_kr +1 ) and poz <= ile_kr + 1 + slupki[ktory - 1][j - 1])):

                        print("_", end = "")
                    else:
                        print(" ", end = "")

            #przejscie do nastepnego poziomu
            if i == (ile_sl)*(2*(ile_kr + 1)):
                print("", end = "\n")
    #update listy slupkow na podstawie listy krokow
    
    krok = steps[step]

    
    z = krok[0]
    na = krok[1]

    #biore pierwszy niezerowy element z listy reperezentujacej slupek 'z'
    for i in range(len(slupki[z - 1])):
        if slupki[z-1][i] != 0:
            krazek = slupki[z-1][i]
            slupki[z-1][i] = 0
            #po znalezieniu pierwszego niezerowego elementu nie musze szukac dalej
            break

    #znajduje pierwszy niezerowy element i na miejsce PRZED nim wstawiam krazek, ktory wczesniej 'zabralem'
    for i in range(len(slupki[na - 1])):
        if slupki[na - 1][i] != 0:
            slupki[na - 1][i - 1] = krazek
            break
        #jesli slupek jest pusty 
        if i == len(slupki[na - 1]) - 1:
            slupki[na - 1][i] = krazek
            break

    sleep(0.8)
    os.system("cls")    

#dodrukowanie ostatecznego polozenia 
for j in range(1, ile_kr + 2):
        #szerokość kazdego poziomu, tj. 'liczba slupkow' x '(2 * (liczba krazkow + 1) )'
        licz = 0 
        poz = 0
        for i in range(1, (ile_sl)*(2*(ile_kr + 1)) + 1):
            #zmienna informujaca, 'na' ktorym slupku jestem

            ktory = licz + 1
            #zmienna mowiaca, w krorej 'komorce' danego slupka jestem 
        
            poz = poz % (2*(ile_kr + 1))
            poz +=1

            #update licznika co każde 2*(ile_kr + 1)
            if i % (2 * (ile_kr + 1)) == 0:
                licz += 1

            #środek słupka
            if i == licz*(2*(ile_kr + 1)) + (ile_kr + 1):

                if j == ile_kr + 1:
                    print("_|",end = "")
                else:
                    if slupki[ktory - 1][j - 1] != 0:
                        print("_|", end = "")
                        
                    else:
                        print(" |", end = "")
                
            #koniec słupka
            elif i % (2* (ile_kr + 1)) == 0:
                if j == ile_kr + 1:
                    print("_", end = "  ")
                else:
                    print(" ", end  = "  ")

            #pozostałe miejsca 
            else:
                if j == ile_kr + 1:
                    print("_", end = "")
                else:
                    #zlozony warunek logiczny na sprawdzenie, czy na aktualnie rysowanej pozycji powinien znalezc sie element krazka
                    if slupki[ktory - 1][j - 1] != 0 and ((poz < (ile_kr + 1) and poz >= ile_kr + 2 - slupki[ktory - 1][j -1] ) or  \
                        (poz > (ile_kr +1 ) and poz <= ile_kr + 1 + slupki[ktory - 1][j - 1])):

                        print("_", end = "")
                    else:
                        print(" ", end = "")

            #przejscie do nastepnego poziomu
            if i == (ile_sl)*(2*(ile_kr + 1)):
                print("", end = "\n")
