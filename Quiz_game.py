# Simple-Quiz-Game-In-Python

print('Welcome to Aryanshu Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3

if answer.lower()=='yes':
    answer=input('Question 1: what is the easiest programming language?')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')


    answer=input('Question 2: who is the world richest person ? ')
    if answer.lower()=='Elon Musk':

        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 3: Birthday of Elon Musk?')
    if answer.lower()=='28 June':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

print('Than kyou for Playing',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')
print('Made by ARYANSHU')
