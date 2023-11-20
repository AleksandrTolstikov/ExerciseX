# На любой вопрос "да" или "нет"

from random import randint
from brain import was_asked, old_answer
memory = []
promt = 'Что вы хотели?'
answers = ('да', 'нет')
question = ''
while question != 'стоп':
    print(promt, end = '')
    question = input()
    if was_asked(memory, question):
        print(old_answer())
    else:
        answer = answers[randint(0,len(answers) - 1)]
        print(answer)
        memory += [(question, answer)]
    
    
