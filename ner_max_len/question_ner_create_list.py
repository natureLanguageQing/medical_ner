import csv

import pandas as pd

from ner_max_len import ICD_10

question_list = []
question_count = {}
questions = pd.read_csv("questions.csv").values.tolist()
for i in questions:
    question = i[0].strip()
    if not isinstance(question, str):
        continue
    if "&nbsp" in question:
        question = question.strip("&nbsp")
    if "哪个医院" in question:
        continue
    if "哪家医院" in question:
        continue
    if question not in question_list:
        question_list.append(question)
    print(question)
    if question in question_count.keys():
        question_count[question] += 1
    else:
        question_count[question] = 1
for question, count in question_count.items():
    print(question, count)
fp = open('question_entity_label.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(fp)
question_ner = {}
writer.writerow(("question", "entity"))
for i in ICD_10:
    for j in question_list:
        if i[0] in j:
            label = 0
            if j in question_ner.keys():
                for question_ner_label in question_ner.keys():
                    if i[0] in question_ner_label[0]:
                        label = 1
                if label == 0:
                    question_ner[j].append(i[0])
                    question_ner[j].append("ICD_10")
            else:
                question_ner[j] = [i[0], "ICD_10"]
for i, j in question_ner.items():
    c = [i] + j
    writer.writerow(c)
