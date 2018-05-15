# -*- coding: utf-8 -*-
import random

question_set = []
answer_set = []
questions = open("F://Python/question/question.txt")
answers = open("F://Python/question/answer.txt")
rules = open("F://Python/question/rules.txt")
question_count = []

print "\nWelcome to FORRER Game !!!\n"
print rules.read()
print "\nGame Start..."
print "-"* 20

q = questions.readline()
r = answers.readline()
while q != "":
    question_set.append(q)
    answer_set.append(r)
    r = answers.readline()
    q = questions.readline()
    #print q,r

def getQuestion():
    q_number = random.randint(0, len(question_set)-1)
    return [question_set[q_number],answer_set[q_number]]

solution_with_problem = getQuestion()
print "\n", solution_with_problem[0]
while True == True:
    answer1 = raw_input("Show Answer(y/n):> ")
    if answer1 == 'y':
        print "\n Ans:",solution_with_problem[1]
        solution_with_problem = getQuestion()
        print "\n", solution_with_problem[0]
    else:
        print "Thank You :)"
        break
