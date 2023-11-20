# На любой вопрос "да" или "нет"

from random import randint
answers = ('да', 'нет')
question = ''
while question != 'стоп':
    question = input()
    answer = answers[randint(0,len(answers) - 1)]
    print(answer)
    
    
