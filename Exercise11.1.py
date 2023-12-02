# На любой вопрос "да" или "нет"

from head import Brain

brain = Brain()
promt = 'Что вы хотели?'

question = ''
while question != 'стоп':
    print(promt, end = '')
    answer = brain.think(input())
    print(answer)
        
    
    
