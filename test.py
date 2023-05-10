from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
import openai
import os
import csv
os.environ['OPENAI_API_KEY'] = 

openai = OpenAI(
    model_name = "text-davinci-003"
)

template = """Answer the following problem by choosing one of the multiple
choice answers, A, B, C, D, or E. 

Question: {question}

Choices: (A) {A} (B) {B} (C) {C} (D) {D} (E) {E}

"""

def generate_prompt_template(template, input_variables):
    prompt_template = PromptTemplate(
        input_variables = input_variables,
        template = template
    )
    return prompt_template



prompt_template = generate_prompt_template(template, ["question","A","B","C","D","E"])
problems = []
ans_choices = []

with open('amc12/amc12_choices.csv', mode='r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        ans_choices.append(row)


with open('amc12/amc12_problems.txt', 'r') as file:
    # Read all the lines in the file
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        problems.append(line)

def getProblems(problem_file):
    problems = []
    with open(problem_file, mode='r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            problems.append(row)
    return problems



filled_prompt = prompt_template.format(
    question = problems[0],
    A = ans_choices[0][0],
    B = ans_choices[0][1],
    C = ans_choices[0][2],
    D = ans_choices[0][3],
    E = ans_choices[0][4],
)


openai = OpenAI(
    model_name="text-davinci-003",
)

print(problems)
