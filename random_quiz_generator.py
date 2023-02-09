#! python3
"""This program creates quizzes with questions in a random order and an answer key for each quiz type"""

import random, pprint, os
from pathlib import Path

capitals = {
    'Abia': 'Umuahia', 'Adamawa': 'Yola', 'Akwa Ibom': 'Uyo', 'Anambra': 'Awka', 'Bauchi': 'Bauchi', 'Bayelsa': 'Yenagoa', 'Benue': 'Makurdi', 'Borno': 'Maiduguri', 'Cross River': 'Calabar', 'Delta': 'Asaba', 'Ebonyi': 'Abakaliki', 'Edo': 'Benin City', 'Ekiti': 'Ado Ekiti', 'Enugu': 'Enugu', 'Gombe': 'Gombe', 'Imo': 'Owerri', 'Jigawa': 'Dutse', 'Kaduna': 'Kaduna', 'Kano': 'Kano', 'Katsina': 'Katsina', 'Kebbi': 'Birnin' 'Kebbi', 'Kogi': 'Lokoja', 'Kwara': 'Ilorin', 'Lagos': 'Ikeja', 'Nasarawa': 'Lafia', 'Niger': 'Minna', 'Ogun': 'Abeokuta', 'Ondo': 'Akure', 'Osun': 'Oshogbo', 'Oyo': 'Ibadan', 'Plateau': 'Jos', 'Rivers': 'Port Harcourt', 'Sokoto': 'Sokoto', 'Taraba': 'Jalingo', 'Yobe': 'Damaturu', 'Zamfara': 'Gusau'
}

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
    option_letters = ['a', 'b', 'c', 'd', 'e']
    fake_options = list(capitals.values())
    random.shuffle(fake_options)

    for option in fake_options:
        if not(option in options):
            options.append(option)
            if len(options) >= options_number:
                break

    random.shuffle(options)

    output_str += f"The capital of {state} is __________\n"

    for index, option in enumerate(options):
        output_str += f"({option_letters[index]}) {option}\n"

    correct_option = option_letters[options.index(capitals[state])]

    return [output_str, correct_option]


def make_quiz(num_of_students):
    """This function makes a specified number of quizzes"""
    for quizNum in range(num_of_students):  
        # Create each quiz and answer key text file 
        current_quiz = quizNum + 1

        quiz = open(f"../quizzes/quiz{current_quiz}.txt", 'w')
        answer_key = open(f"../answer_keys/answer_key{current_quiz}.txt", 'w')

        # Create header
        quiz.write("Name:\n\nDate:\n\nCourse:\n\n")
        quiz.write(f"State Capitals Quiz (Form {current_quiz})")
        quiz.write("\n\n")
        answer_key.write(f"ANSWER KEY\nQUIZ FORM {current_quiz}\n\n")

        # Shuffle the order of the states
        states = list(capitals.keys())
        random.shuffle(states)

        # write a question to each question file
        for index in range(len(states)):
            question_num = index + 1
            question, answer = make_question(states[index], 4)
            quiz.write(f"{question_num}. {question} \n")
            answer_key.write(f"{(str(question_num) + '.').ljust(3, ' ')} {answer} \n")

        quiz.write(f"GOODLUCK!!")

make_quiz(20)