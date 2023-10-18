from pprint import pprint
class Person:
    def __init__(self, name, age, address):
        self.name, self.age, self.address = name, age, address
        self.key = (name, address)
    def __repr__(self):
        return "Persone('%s',%s,'%s')" % (self.name, self.age, self.address)

aleksandr = Person("Александр", 1983, "Пермь")
petr = Person("Пётр", 1990, "Киров")
mihail = Person("Михаил", 1987, "Саратов")
people = {
    aleksandr.key: aleksandr,
    petr.key: petr,
    mihail.key: mihail,
}
pprint(people)
pprint(people[aleksandr.key])
