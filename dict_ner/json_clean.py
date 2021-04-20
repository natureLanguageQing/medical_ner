import json
# 清洗json数据 question_entity 数据
fp = open('../match_machine/question_entity.json', 'r', newline='', encoding='utf-8')
write = open('../match_machine/question_entity_clean.json', 'w', newline='', encoding='utf-8')

for question_entity in fp.readlines():
    question_entity_data = json.loads(question_entity)
    labels = question_entity_data['labels']
    export_list = []
    for label_index in range(1, len(labels)):
        now_label = labels[label_index]
        last_label = labels[label_index - 1]
        if last_label[1] > now_label[0]:
            print(last_label, now_label)
            if last_label[1] - last_label[0] > now_label[1] - now_label[0]:
                continue
            elif last_label in export_list:

                export_list.remove(last_label)
                export_list.append(now_label)
        else:
            export_list.append(now_label)
    question_entity_data["labels"] = export_list
    entity_dict_label = json.dumps(question_entity_data, ensure_ascii=False)

    write.write(entity_dict_label + "\n")
