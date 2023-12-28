class fractie:
    def __init__(self,numarator,numitor):
        if numitor == 0 :
            raise ValueError("Numitorul nu poate fi 0.")
        self.numarator=numarator
        self.numitor=numitor

    def __str__(self):
        return f"{self.numarator}/{self.numitor}"

    def __add__(self, other): #supraincarcarea operatorului +
        numitor_rez = self.numitor * other.numitor
        numarator_rez = self.numarator * other.numitor + other.numarator * self.numitor
        return fractie(numarator_rez, numitor_rez)

    def __sub__(self, other): #supraincarcarea operatorului -
        numitor_rez = self.numitor * other.numitor
        numarator_rez = self.numarator * other.numitor - other.numarator * self.numitor
        return fractie(numarator_rez, numitor_rez)

    def invers(self):
        if self.numarator == 0:
            raise ValueError("Nu se poate inversa fractia cu numaratorul 0.")
        return fractie(self.numitor,self.numarator)


fractie1= fractie(2,3)
fractie2= fractie(5,6)
print(fractie1+fractie2)
print(fractie1-fractie2)
print(fractie.invers(fractie1))