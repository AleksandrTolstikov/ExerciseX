from pprint import pprint
from itertools import product
from utils import compare, int_val

name_short = {'зовут'}
age_short = {'старше', 'младше', 'возраст'}
address_short = {'живет'}

class Person:
    def __init__(self, name, age, address):
        self.name, self.age, self.address = name, age, address
        self.key = (name, address)

    def fuzzy_compare(self, query):
        q = set(query.split())
        score = 0
        for m, f in zip(
            [name_short, age_short, address_short],
            [self.by_name, self.by_age, self.by_address]
        ):
            if m & q:
                score += f(q)
 
        return score > 0.55
          
    def by_name(self, Q):
         Q = Q - name_short
         W = set(self.name.split())
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
 
        return q_age+7 >= self.age >=q_age-7 

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
        return "Persone('%s',%s,'%s')" % (self.name, self.age, self.address) 

if __name__ == '__main__':       
    aleksandr = Person("Александр", 40, "Пермь")
    petr = Person("Пётр", 33, "Киров")
    mihail = Person("Михаил", 36, "Саратов")

    quares = [
            'зовут Михаил',
            'старше 35',
            'младше 35',
            'живет Пермь',]
      
    people = {
        aleksandr.key: aleksandr,
        petr.key: petr,
        mihail.key: mihail,
    }

    for query, person in product(quares, people.values()):
        if person == query:
            print(query, person)
