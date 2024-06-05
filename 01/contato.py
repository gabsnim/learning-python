class Contato (object):
    name = ''
    number = 0
    age = 0
    adress = ''
    
    #construtor alternativo
    def __init__ (self, name, number, age, adress):
        self.name = name
        self.number = number
        self.age = age
        self.adress = adress

    
    #self semelhante ao this ->
    #converter para string ao mostrar na tela
    def printContato(self):
        print ('name = ' + self.name)
        print ('number = ' + str(self.number))
        print ('age = ' + str(self.age))
        print ('adress = ' + self.adress)


    