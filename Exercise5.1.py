from pprint import pprint

class Person:

	def __init__(self, name, age, address):
		self.name = name
		self.age = age
		self.address = address
		self.key = (name, age, address)
	
	def __repr__(self):
		return "Person('%s' ,%s ,'%s')" % (self.name, self.age, self.address)

alex = Person('Александр', 40, 'Пермь')
dim = Person('Дмитрий', 35, 'Киров')
mih = Person('Михаил', 41, 'Самара')
peolpe = {
    alex.key: alex,
    dim.key: dim,
    mih.key: mih,
}

pprint(alex.key)
