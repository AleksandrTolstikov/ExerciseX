from pprint import pprint
from itertools import product
from utils import compare, int_val

fio_short = {'ФИО'}
age_short = {'возраст'}
address_short = {'адрес'}

class Person:
    def __init__(self, fio, age, address):
        self.fio, self.age, self.address = fio, age, address
        self.key = (fio, address)

    def fuzzy_compare(self, query):  
        q = set(query.split())
        score = 0
        for m, f in zip(
            [fio_short, age_short, address_short],
            [self.by_fio, self.by_age, self.by_address]
        ):
            if m & q:
                score += f(q)
 
        return score > 0.75
          
    def by_fio(self, Q): 
         Q = Q - fio_short
         W = set(self.fio.split())
         rez = []
         for a, b in product(Q, W):
             rez += [(compare(a,b),a,b)]

         return max(rez)[0]
           
    def by_age(self, Q):
        q_age = max([int_val(q) for q in Q])
        if 'старше' in Q:
            return q_age < self.age
        if 'младше' in Q:
            return q_age > self.age
 
        return q_age+1 >= self.age >=q_age-1 

    def by_address(self, Q):
        Q = Q - address_short
        W = set(self.address.split())
        rez = []
        for a,b in product(Q, W):
            rez += [(compare(a,b),a,b)]
 
        return max(rez)[0]    
    
        
    def __eq__(self, obj):
        if type(obj) == Person:
            return 
        elif type(obj) == str:
            return self.fuzzy_compare(obj)
        else:
            return false     
      

    def __repr__(self):
        return "Persone('%s',%s,'%s')" % (self.fio, self.age, self.address) 

if __name__ == '__main__':       
    aleksandr = Person("Семёнов Александр Аналольевич", 40, "Пермь, ул. Льва Шатрова, 36")
    petr = Person("Иванов Пётр Олегович", 33, "Пермь, ул. Героев Хасана, 31")
    mihail = Person("Сидоров Михаил Алексеевич", 36, "Пермь, ул. Баумана, 8")

    quares = [
            'ФИО Семёнов',
            'адрес Баумана',
            'возраст 33',]
      
    people = {
        aleksandr.key: aleksandr,
        petr.key: petr,
        mihail.key: mihail,
    }

    for query, person in product(quares, people.values()):
        if person == query:
            pprint((query, person))
