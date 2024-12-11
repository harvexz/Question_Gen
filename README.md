# GCSE AQA Foundation Question Generator

This project is a Python-based tool designed to generate GCSE AQA Foundation-level exam questions. It focuses on key topics, starting with number operations, to help students practice and revise effectively. The program runs a simple command-line menu, making it accessible and easy to use.

Features
•	Generates questions from GCSE Foundation topics.
•	Current topics include:
•	Number Operations: Basic arithmetic, factors and multiples, and place value/rounding.
•	Cycles through different types of questions in a mix.
•	Designed for efficient practice and preparation.

## Installation

To set up the project on your local machine:
1.	Clone the repository:

    git clone https://github.com/harvexz/Question_Gen


2.	Navigate to the project directory:

    cd <project-directory>

## Usage

The program is run directly from the command line using Python:
1.	Run the program:

    python3 main.py


2.	Follow the interactive menu to specify the number of questions you want. The tool will generate a mix of questions and display them in order.

Example interaction:


    Enter the number of questions you want to generate: 5
    
    Q1: What is 15 + 7?
    Q2: List all the factors of 36.
    Q3: Round 732.45 to the nearest 100.
    Q4: What is 45 - 9?
    Q5: What is the value of the digit in the tens place in the number 129?


## Requirements
•	Python 3.6 or higher: Ensure you have Python installed. Download here.

## Project Structure

The project follows a modular structure to ensure scalability and maintainability.

    project-directory/
    │
    ├── main.py
    │   - The entry point for the program. Handles user input and generates questions using the topic files.
    │
    ├── topics/
    │   └── number_operations.py
    │       - Contains the `NumberOperations` class.
    │       - Functions:
    │           - `generate_basic_arithmetic_question`: Generates addition, subtraction, multiplication, or division questions.
    │           - `generate_factors_and_multiples_question`: Generates factors and multiples questions.
    │           - `generate_place_value_and_rounding_question`: Generates place value or rounding questions.
    │   └── fractions_decimals_percentages.py
    │       - Contains the `FractionsDecimalsPercentages` class.
    │       - Functions:
    │           - `generate_conversion_question`: Generates convertion between fractions, decimals, and percentages questions.
    │           - `generate_calculation_question`: Generates fraction and percentage questions.


## How It Works

Topic Files:

•	Each topic is implemented in its own Python file under the topics/ directory.

•	For example, number_operations.py includes the logic for generating number operation questions.

2.	Question Cycling:

•	The program cycles through the question types: arithmetic, factors/multiples, and place value/rounding.

•	If the user requests n questions, the program generates one of each type in order until n is reached.

3.	Future Expansion:

•	Additional topics can be added by creating new Python files in the topics/ directory and implementing a class with similar methods.