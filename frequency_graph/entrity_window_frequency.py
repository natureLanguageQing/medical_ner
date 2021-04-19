import json
# 做实体跳表 关系可视化
question_entity = open("../match_machine/question_entity.json", encoding="utf-8")
for i in question_entity.readlines():
    question_entity_dict: dict = json.loads(i)
    print(question_entity_dict["labels"])
    print(len(question_entity_dict["labels"]))
    print(question_entity_dict["text"])
    for label in question_entity_dict["labels"]:
        print(question_entity_dict["text"][label[0]:label[1]], label[2])
