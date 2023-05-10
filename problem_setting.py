import os
import csv

answers = []
with open('amc12/amc12_ans.csv', mode='r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        answers.append(row)

print(answers[0][0])