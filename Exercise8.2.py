from pprint import pprint
from itertools import product
from utils import compare, int_val

NAME_WORDS = {'имя', 'зовут'} # Оформление по PEP8, легче найти в коде
AGE_WORDS = {'старше', 'младше'} # Оформление по PEP8, легче найти в коде
ADRESS_WORDS = {'живет'} # Оформление по PEP8, легче найти в коде


class Person:
    def __init__(self, name, age, address):
        self.name, self.age, self.address = name, age, address
        self.key = (name, address)

    def fuzzy_compare(self, query):
        q = set(query.split())
        score = 0
        for m, f in zip(
            [NAME_WORDS, AGE_WORDS, ADRESS_WORDS], # Оформление по PEP8
            [self.by_name, self.by_age, self.by_address]
        ):
            if m & q:
                score += f(q)
 
        return score > 0.55
          
    def by_name(self, Q):
         Q = Q - NAME_WORDS # Оформление по PEP8
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
        Q = Q - ADRESS_WORD # Оформление по PEP8
        W = set(self.address.split())
        rez = []
        for a,b in product(Q, W):
            rez += [(compare(a,b),a,b)]
 
        return max(rez)[0]
    # Оформление пробелов по PEP8 
        
    def __eq__(self, obj):
        if type(obj) == Person:
            return 
        elif type(obj) == str:
            return self.fuzzy_compare(obj)
        else:
            return false     
      
    def __repr__(self):
        return "Persone('%s',%s,'%s')" % (self.name, self.age, self.address) 
    # Оформление пробелов по PEP8 

if __name__ == '__main__':       
    aleksandr = Person("Александр", 40, "Пермь")
    petr = Person("Пётр", 33, "Киров")
    mihail = Person("Михаил", 36, "Саратов")

    quares = [
            'имя Михаил',
            'старше 35',
            'младше 35',
            'живет Киров',
            'зовут Алекс',]
      
    people = {
        aleksandr.key: aleksandr,
        petr.key: petr,
        mihail.key: mihail,
    }

    for query, person in product(quares, people.values()):
        if person == query:
            pprint((query, person))
