import random
from Topics import number_operations
from Topics import fractions_decimals_percentages


def get_choice():
    valid_choice = False

    while not valid_choice:
        try:
            topic_choice = int(input("Enter the number corresponding to your choice: "))
            if topic_choice > 0 and topic_choice < 8:
                valid_choice = True
            else:
                print("Selection must be from 1-7")
        except:
            print("Must be an integer")

    return topic_choice


def get_num():
    valid_num = False

    while not valid_num:
        try:
            num_questions = int(input("Enter the number of questions to generate: "))
            valid_num = True
        except:
            print("Must be an integer")

    return num_questions


def generate_number_operations_question():
    question_gen = number_operations.NumberOperations()
    q_type = random.randint(1,3)

    if q_type % 3 == 0:
        question, answer = question_gen.generate_basic_arithmetic_question()
    elif q_type % 3 == 1:
        question, answer = question_gen.generate_factors_and_multiples_question()
    elif q_type % 3 == 2:
        question, answer = question_gen.generate_place_value_and_rounding_question()
    else:
        raise ValueError()

    return question, answer


def generate_fractions_decimals_percentages():
    question_gen = fractions_decimals_percentages.FractionsDecimalsPercentages()
    q_type = random.randint(1,2)

    if q_type % 2 == 0:
        question, answer = question_gen.generate_conversion_question()
    elif q_type % 2 == 1:
        question, answer = question_gen.generate_calculation_question()
    else:
        raise ValueError()

    return question, answer


def main():
    valid_num = False
    topics = {
        '1': 'Number Operations and Properties',
        '2': 'Fractions, Decimals, and Percentages',
        '3': 'Ratio and Proportion',
        '4': 'Algebra',
        '5': 'Geometry and Measures',
        '6': 'Statistics and Probability',
        '7': 'Mixed'
    }

    print("Select a topic:")
    for key, value in topics.items():
        print(f"{key}. {value}")

    topic_choice = get_choice()
    num_questions = get_num()

    questions = []
    for _ in range(num_questions):
        if topic_choice == 1:
            question, answer = generate_number_operations_question()
        elif topic_choice == 2:
            question, answer = generate_fractions_decimals_percentages()
        else:
            question, answer = generate_number_operations_question()
        questions.append((question, answer))

    for i, (q, a) in enumerate(questions, 1):
        print(f"Q{i}: {q} Answer: {a}")

if __name__ == "__main__":
    main()