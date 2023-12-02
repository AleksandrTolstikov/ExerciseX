from itertools import product

def compare(s1, s2):
	ngrams = [s1[i:i+3] for i in range(len(s1))]
	count = 0
	for ngram in ngrams:
		count += s2.count(ngram)

	return count/max(len(s1), len(s2)) > 0.7

class Person:

	def __init__(self, name=None, age=None):
		self.name = name
		self.age = age

	def __eq__(self, obj):
		return (obj.name == None or self.name == None or compare(obj.name, self.name)) \
		   and (obj.age == None or self.age == None or abs(obj.age - self.age) < 3)

	def __repr__(self):
		return f"Person('{self.name}', {self.age})"

to_search = [
	Person('Алексанр', 38),
	Person(age=38),
	Person(name='Алексанр'),
]

people = [
	Person('Александр', 40),
	Person('Алексей', 35),
	Person('Михаил', 41),	
]

for p1, p2 in product(people, to_search):
	print(p1, p2, p1 == p2)

