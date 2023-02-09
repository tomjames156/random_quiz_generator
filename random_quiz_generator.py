#! python3
"""This program creates quizzes with questions in a random order and an answer key for each quiz type"""

import random, pprint, os
from pathlib import Path

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Creates the quizzes directory
if not(Path("../quizzes").exists()):
    print("Making quizzes directory...")
    os.mkdir("../quizzes")

# Creates the answer keys directory
if not(Path("../answer_keys").exists()):
    print("Making answer keys directory...")
    os.mkdir("../answer_keys")


def make_question(state, options_number):
    """This function makes a question"""

    output_str = ''
    options = [capitals[state]]
    fake_options = list(capitals.values())
    del fake_options[fake_options.index(options[0])]
    fake_options = random.sample(fake_options, 3)
    options += fake_options

    random.shuffle(options)

    output_str += f"The capital of {state} is __________\n"

    for index, option in enumerate(options):
        output_str += f" ({'ABCDE'[index]}) {option}\n"

    correct_option = 'ABCDE'[options.index(capitals[state])]

    return [output_str, correct_option]

for quizNum in range(35):  
    # Create each quiz and answer key text file 
    current_quiz = quizNum + 1

    quiz = open(f"../quizzes/quiz{current_quiz}.txt", 'w')
    answer_key = open(f"../answer_keys/answer_key{quizNum+1}.txt", 'w')

    # Create header
    quiz.write("Name:\n\nDate:\n\nCourse:\n\n")
    quiz.write(f"State Capitals Quiz (Form {current_quiz})")
    quiz.write("\n\n")
    answer_key.write(f"ANSWER KEY\nQUIZ FORM {current_quiz}\n\n")

    # Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # write a question to each question file
    for index in range(len(capitals)):
        q_num = index + 1
        question, answer = make_question(states[index], 4)
        quiz.write(f"{q_num}. {question} \n")
        answer_key.write(f"{(str(q_num) + '.').ljust(3, ' ')} {answer} \n")

    quiz.write(f"GOODLUCK!!")
    quiz.close()
    answer_key.close()