question_entity_label = set(open("question_entity_label_faster.json", "r", encoding="utf-8").readlines())
print(len(open("question_entity_label_faster.json", "r", encoding="utf-8").readlines()))
print(len(question_entity_label))

f = open("question_entity_label_faster_set.json", "w", encoding="utf-8")
for i in question_entity_label:
    f.writelines(i)
f = open("question_entity_label_faster_part.json", "w", encoding="utf-8")
for i in list(question_entity_label)[:2000]:
    f.writelines(i)
