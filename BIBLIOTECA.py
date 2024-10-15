class pessoa():
    def __init__ (self, nome,peso,idade):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=False
        self.andando=False
        self.dormindo=False

    def comer(self):
        if self.comendo==False:
            if self.andando==False:
                if self.dormindo==False:
                    print(f"{self.nome} foi comer")
                    self.comendo=True
                else:
                    print(f"{self.nome} não foi comer pois esta dormindo")
            else:
                print(f"{self.nome} não foi comer pois esta andando")
        else:
            print(f"{self.nome} não foi comer pois ja esta comendo ")

    def andar(self):
        if self.andando == False:
            if self.dormindo == False:
                if self.comendo == False:
                    print(f"{self.nome} esta andando")
                    self.andando = True
                else:
                    print(f"{self.nome} não foi andar pois esta comendo")
            else:
                print(f"{self.nome} não foi andar pois esta dormindo")
        else:
            print(f"{self.nome} não foi andar pois esta andando")
