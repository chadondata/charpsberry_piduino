#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Demonstrates a quiz application using raspberry pi with gpio LED

Premise: Load a quiz from disk and present it to the user for them to answer the questions.

Correct answer lights up a green LED. Wrong answer sends millions of volts through their body.

Or just lights a red LED. 

Haven't decided yet.

"""

import json
from pandas.io.json import json_normalize

if __name__ == '__main__':
    print('Hi, and welcome to the quiz!')

    print('Loading quiz questions...')
    quiz_file = open('quiz.json')
    quiz_questions = json.load(quiz_file)
    quiz_file.close()

    for q in quiz_questions['quiz_questions']:
        print(json.dumps(q))

