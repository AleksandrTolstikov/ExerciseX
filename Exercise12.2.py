class Foreteller:
    def predict(self, question):
        answer = Answer(question)
        return answer

class Question:
    def __init__(self):
        value = input('Спрашивай? ')

class Answer:
    def __init__(self, question):
        from random import choice
        self.__rez = choice(['да','нет'])

    def __str__(self):
        return self.__rez


foreteller = Foreteller()
question = Question()
print(foreteller.predict(question))
