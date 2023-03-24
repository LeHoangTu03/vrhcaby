from random import randint

class Hra:  #herní deska

    def __init__(self):
       pass
    
    def hernipole(self):    # modifikovaný zásobník, lze vkládat jen kameny stejných barev
        pass

    def dvojkostka(self):   # vrací seznam možných dvojic či čtveřic
        prvni_kostka, druha_kostka = randint(1,6), randint(1,6)
        hod = f"Hod kostkou\nPrvní kostka: {prvni_kostka}\nDruhá kostka: {druha_kostka}"
        if prvni_kostka == druha_kostka:
            return hod + "\nHodil si double a proto můžeš táhnout čtyřikrát"
        else:
            return hod

    def bar(self):  # továrna na herní kameny, s řízenou produkcí
        pass

    def herni_kamen(self):  # s pamětí, kde se postupně nacházel
        pass

class Hrac(Hra):    # odvozená třída
    
    def __init__(self):
        pass


def main():
    hra = Hra()
    print(hra.dvojkostka())
    print("Dal bych si závitky")


if __name__ == "__main__":
    main()