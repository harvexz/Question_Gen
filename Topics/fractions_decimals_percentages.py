import random
from fractions import Fraction

class FractionsDecimalsPercentages:
    def __init__(self):
        pass

    def generate_conversion_question(self):
        """Generates a question for converting between fractions, decimals, and percentages."""
        conversion_type = random.choice(['fraction_to_decimal', 'fraction_to_percentage', 'decimal_to_fraction',
                                         'decimal_to_percentage', 'percentage_to_fraction', 'percentage_to_decimal'])
        question = ""
        answer = None

        if conversion_type == 'fraction_to_decimal':
            numerator = random.randint(1, 20)
            denominator = random.randint(2, 20)
            fraction = Fraction(numerator, denominator)
            question = f"Convert the fraction {numerator}/{denominator} to a decimal."
            answer = round(numerator / denominator, 2)

        elif conversion_type == 'fraction_to_percentage':
            numerator = random.randint(1, 20)
            denominator = random.randint(2, 20)
            fraction = Fraction(numerator, denominator)
            question = f"Convert the fraction {numerator}/{denominator} to a percentage."
            answer = round((numerator / denominator) * 100, 2)

        elif conversion_type == 'decimal_to_fraction':
            decimal = round(random.uniform(0.1, 10), 2)
            fraction = Fraction(decimal).limit_denominator()
            question = f"Convert the decimal {decimal} to a fraction."
            answer = f"{fraction.numerator}/{fraction.denominator}"

        elif conversion_type == 'decimal_to_percentage':
            decimal = round(random.uniform(0.1, 10), 2)
            question = f"Convert the decimal {decimal} to a percentage."
            answer = round(decimal * 100, 2)

        elif conversion_type == 'percentage_to_fraction':
            percentage = random.randint(1, 100)
            fraction = Fraction(percentage, 100).limit_denominator()
            question = f"Convert the percentage {percentage}% to a fraction."
            answer = f"{fraction.numerator}/{fraction.denominator}"

        elif conversion_type == 'percentage_to_decimal':
            percentage = random.randint(1, 100)
            question = f"Convert the percentage {percentage}% to a decimal."
            answer = round(percentage / 100, 2)

        return question, answer

    def generate_calculation_question(self):
        """Generates a question for percentage and fraction calculations."""
        calculation_type = random.choice(['percentage_of_amount', 'percentage_increase', 'percentage_decrease',
                                          'fraction_addition', 'fraction_subtraction', 'fraction_multiplication', 'fraction_division'])
        question = ""
        answer = None

        if calculation_type == 'percentage_of_amount':
            percentage = random.randint(1, 100)
            amount = random.randint(10, 1000)
            question = f"What is {percentage}% of {amount}?"
            answer = round((percentage / 100) * amount, 2)

        elif calculation_type == 'percentage_increase':
            amount = random.randint(10, 1000)
            percentage = random.randint(1, 100)
            question = f"Increase {amount} by {percentage}%."
            answer = round(amount * (1 + (percentage / 100)), 2)

        elif calculation_type == 'percentage_decrease':
            amount = random.randint(10, 1000)
            percentage = random.randint(1, 100)
            question = f"Decrease {amount} by {percentage}%."
            answer = round(amount * (1 - (percentage / 100)), 2)

        elif calculation_type == 'fraction_addition':
            fraction1 = Fraction(random.randint(1, 10), random.randint(2, 10))
            fraction2 = Fraction(random.randint(1, 10), random.randint(2, 10))
            question = f"Add the fractions {fraction1.numerator}/{fraction1.denominator} and {fraction2.numerator}/{fraction2.denominator}."
            answer = fraction1 + fraction2

        elif calculation_type == 'fraction_subtraction':
            fraction1 = Fraction(random.randint(1, 10), random.randint(2, 10))
            fraction2 = Fraction(random.randint(1, 10), random.randint(2, 10))
            question = f"Subtract the fraction {fraction2.numerator}/{fraction2.denominator} from {fraction1.numerator}/{fraction1.denominator}."
            answer = fraction1 - fraction2

        elif calculation_type == 'fraction_multiplication':
            fraction1 = Fraction(random.randint(1, 10), random.randint(2, 10))
            fraction2 = Fraction(random.randint(1, 10), random.randint(2, 10))
            question = f"Multiply the fractions {fraction1.numerator}/{fraction1.denominator} and {fraction2.numerator}/{fraction2.denominator}."
            answer = fraction1 * fraction2

        elif calculation_type == 'fraction_division':
            fraction1 = Fraction(random.randint(1, 10), random.randint(2, 10))
            fraction2 = Fraction(random.randint(1, 10), random.randint(2, 10))
            question = f"Divide the fraction {fraction1.numerator}/{fraction1.denominator} by {fraction2.numerator}/{fraction2.denominator}."
            answer = fraction1 / fraction2

        return question, answer