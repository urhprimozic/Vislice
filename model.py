import random

STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZMAGA = 'W'
PORAZ = 'X'

class Igra: 
    def __init__(self, geslo, crke=None): 
        self.geslo = geslo.upper()
        self.crke = [] if crke is None else [crka.upper() for crka in crke]

    def napacne_crke(self): 
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self, geslo, crke): 
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self, geslo, crke): 
        return len(self.napacne_crke())

    def poraz(self): 
        return self.stevilo_napak() >= STEVILO_DOVOLJENIH_NAPAK

    def zmaga(self): 
        #return set(self.geslo) == set(self.pravilne_crke())
        #return all(crka in self.crke for crka in self.geslo)
        for crka in self.geslo: 
            if crka not in self.crke: 
                return False
        return True

    def pravilni_del_gesla(self): 
        s = ''
        for crka in self.geslo: 
            s += crka if crka in self.crke else '_'
        return s

    def nepravilni_ugibi(self): 
        return ' '.join(self.napacne_crke())

    def ugibaj(self, ugibana_crka):
        ugibana_crka = ugibana_crka.upper()
        if ugibana_crka in self.crke: 
            return PONOVLJENA_CRKA
        else: 
            self.crke.append(ugibana_crka)
            if ugibana_crka in self.geslo: 
                if self.zmaga(): 
                    return ZMAGA
                else: 
                    return PRAVILNA_CRKA
            else: 
                if self.poraz(): 
                    return PORAZ
                else: 
                    return NAPACNA_CRKA

bazen_besed = []
for beseda in open('besede.txt', encoding='utf-8'): 
    bazen_besed.append(beseda.strip().upper())

def nova_igra(): 
    beseda = random.choice(bazen_besed)
    return Igra(beseda)