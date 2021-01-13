import csv

import pandas as pd
import tqdm

from ner_max_len import ICD_10

question_list = []
question_count = {}
questions = pd.read_csv("questions.csv").values.tolist()[:50000]
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
    if question in question_count.keys():
        question_count[question] += 1
    else:
        question_count[question] = 1

fp = open('question_entity_label_min_length_2.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(fp)
question_ner = {}
writer.writerow(("question", "entity", "entity_label", "entity", "entity_label", "entity", "entity_label", "entity",
                 "entity_label", "entity", "entity_label", "entity", "entity_label", "entity", "entity_label", "entity",
                 "entity_label"))
for i in tqdm.tqdm(ICD_10):
    for j in question_list:
        if i[0] in j:
            label = 0
            if j in question_ner.keys():
                for question_ner_label in question_ner.keys():
                    for values in question_ner[question_ner_label]:

                        if values != "ICD_10" and i[0] in values:
                            label = 1
                if label == 0 and len(i[0]) > 2:
                    question_ner[j].append(i[0])
                    question_ner[j].append("ICD_10")
            else:
                if len(i[0]) > 2:
                    question_ner[j] = [i[0], "ICD_10"]

for i, j in question_ner.items():
    c = [i] + j
    writer.writerow(c)
