import json

try:
    with open('qiz.json', 'r') as f:
        qz = json.load(f)
except FileNotFoundError:
    print('Questions file not found.')
    qz = []

score = 0
for q in qz:
    print(q['question'])
    print(q['options'])
    us = input('Answer: ')
    if us == q['ans']:
        print('Correct')
        score += 1
    else:
        print('Wrong')
        print('Correct Answer:', q['ans'])

print(score, '/', len(qz))
