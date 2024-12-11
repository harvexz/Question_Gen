import random
from Topics import number_operations

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


def main():
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

    topic_choice = input("Enter the number corresponding to your choice: ")
    num_questions = int(input("Enter the number of questions to generate: "))

    questions = []
    for _ in range(num_questions):
        if topic_choice == '1':
            question, answer = generate_number_operations_question()
        else:
            question, answer = generate_number_operations_question()
        questions.append((question, answer))

    for i, (q, a) in enumerate(questions, 1):
        print(f"Q{i}: {q} Answer: {a}")

if __name__ == "__main__":
    main()