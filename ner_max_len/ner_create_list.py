import csv

from ner_max_len import questions, ICD_10

question_list = []
question_count = {}
for i in questions:
    question = i[2].strip()
    if not isinstance(question, str):
        continue
    if "&nbsp" in question:
        question = question.strip("&nbsp")
    if "哪个医院好" in question:
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
fp = open('question_entity_list.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(fp)
question_ner = {}
writer.writerow(("question", "entity"))
for i in ICD_10:
    for j in question_list:
        if i[0] in j:
            if j in question_ner.keys():
                question_ner[j].append(i[0])
            else:
                question_ner[j] = [i[0]]
for i, j in question_ner.items():
    c = [i] + j
    writer.writerow((c))
