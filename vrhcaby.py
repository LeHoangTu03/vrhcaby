# 24.3. Jen jsem přepsal myšlenku z emailu co nám poslal pan Fišer
# 31.3. Úprava úvodu hry

from random import randint

# idk kam to implementovat, ale zde je herní pole (ano nudím se)
herni_pole = [["------      ------"],
              ["------      ------"],
              ["------      ------"],
              ["------      ------"],
              ["------      ------"],
              ["------      ------"],
              ["██████████████████"], # jakože bar
              ["------      ------"],
              ["------      ------"],
              ["------      ------"],
              ["------      ------"],
              ["------      ------"],
              ["------      ------"]]

class Hra:  #herní deska

    def __init__(self):
       pass
    
    def hernipole(self): # modifikovaný zásobník, lze vkládat jen kameny stejných barev
        pass

    def dvojkostka(self): # vrací hodnoty kostek a seznam možných tahů 
        prvni_kostka = randint(1,6)
        druha_kostka = randint(1,6)
        hod = f"{prvni_kostka} {druha_kostka}"
        if prvni_kostka == druha_kostka:
            return hod + "\nHodil si double"
        else:
            return hod

    def bar(self):  # továrna na herní kameny, s řízenou produkcí
        pass

    def herni_kamen(self):  # s pamětí, kde se postupně nacházel
        pass

class Hrac(Hra):    # odvozená třída
    
    def __init__(self):
        pass


def main(): # Nějaký úvod do hry s volbou hráče
    print(
        "[1]-proti random cápkovi kterého jsem potkal na ulici, protože nemám žádné kamarády\n"
        "[2]-proti počítači, protože nechodím ven, a protože nemám žádné kamarády")
    hrac = int(input("Vyber s kým chceš hrát: "))
    if hrac == 1 or hrac == 2:
        hra(hrac)
    else:
        print("\nŠpatná volba")
        main()


def hra(hrac): # spouští hru
    hra = Hra()
    input("Pro hod kostkami stiskni libovolnou klávesu")
    print(hra.dvojkostka())
    # for i in herni_pole:
    #     print(i)


if __name__ == "__main__": # zjišťuje zda se spouští jako program
    print("Vitej dobrodružníku")
    main()



