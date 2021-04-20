# 数据去重
question_entity_label = set(open("../match_machine/question_entity_label.json", "r", encoding="utf-8").readlines())
print(len(open("../match_machine/question_entity_label.json", "r", encoding="utf-8").readlines()))
print(len(question_entity_label))

f = open("../match_machine/question_entity_label.json", "w", encoding="utf-8")
for i in question_entity_label:
    f.writelines(i)
f = open("../match_machine/question_entity_label_faster_part.json", "w", encoding="utf-8")
for i in list(question_entity_label)[:2000]:
    f.writelines(i)
