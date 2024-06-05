from  contato import Contato


# pessoa = Contato()

pessoa = Contato('gabs', 99999999, 20, 'xxx xxx xxx xxx')

pessoa.printContato()


print (type(pessoa.name))
print (type(pessoa.number))
print (type(pessoa.age))
print (type(pessoa.adress))