import random

class NumberOperations:
    def __init__(self):
        pass

    def generate_basic_arithmetic_question(self):
        """Generates a basic arithmetic question (addition, subtraction, multiplication, division)."""
        operations = ['+', '-', '*', '/']
        num1 = random.randint(-10, 50)
        num2 = random.randint(1, 50)

        operation = random.choice(operations)
        if operation == '/':  # Ensure division results in an integer
            num1 = num1 * num2  # Make num1 a multiple of num2

        question = f"What is {num1} {operation} {num2}?"
        answer = eval(f"{num1} {operation} {num2}")
        return question, answer

    def generate_factors_and_multiples_question(self):
        """Generates a question on factors and multiples."""
        answers = []
        question_type = random.choice(['factors', 'multiples'])
        number = random.randint(10, 50)

        if question_type == 'factors':
            question = f"List all the factors of {number}."
            for x in range(1, number + 1):
                if number % x == 0:
                    answers.append(x)
        else:  # multiples
            limit = random.randint(3, 10)
            question = f"List the first {limit} multiples of {number}."
            for x in range(1, limit + 1):
                answers.append(number * x)

        return question, answers

    def generate_place_value_and_rounding_question(self):
        """Generates a question on place value or rounding."""
        question_type = random.choice(['place_value', 'rounding'])
        number = random.uniform(10, 1000)
        answer = 0

        if question_type == 'place_value':
            place = random.choice(['tens', 'hundreds', 'thousands'])
            question = f"What is the value of the digit in the {place} place in the number {int(number)}?"
            if place == 'tens':
                answer = (number // 10) % 10 * 10
            elif place == 'hundreds':
                answer = (number // 100) % 10 * 100
            elif place == 'thousands':
                answer = (number // 1000) % 10 * 1000
        else:  # rounding
            precision = random.choice([1, 2, 3, 4, 10, 100])
            if precision < 10:
                question = f"Round {number:.4f} to {precision} decimal place(s)."
                answer = round(number, precision)
            else:
                question = f"Round {int(number)} to the nearest {precision}."
                answer = round(int(number) / precision) * precision

        return question, answer


if __name__ == "__main__":
    q = NumberOperations()
    q, a = q.generate_factors_and_multiples_question()
    print(f"Q:{q}, A:{a}")