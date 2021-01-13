import json

clean_medical_ner_entities_new = open("clean_medical_ner_entities_new.json", "r", encoding="utf-8")
export = []
export_labels = []
error = []
index = 0


def start_clean(clean_medical_ner_entity_one, start_word, index=None, text=None):
    """

    :param text:
    :param clean_medical_ner_entity_one:
    :param start_word:
    :param index:
    :return:
    """

    if clean_medical_ner_entity_one["entity"].startswith(start_word):
        error.append({"entity": clean_medical_ner_entity_one, "text": text})
        clean_medical_ner_entity_one["start_offset"] += 1
        clean_medical_ner_entity_one["entity"] = clean_medical_ner_entity_one["entity"].replace(start_word, "")
        index += 1
    return index


for i in clean_medical_ner_entities_new.readlines():
    clean_medical_ner_entities_one = json.loads(i)
    print(clean_medical_ner_entities_one)
    for clean_medical_ner_entity in clean_medical_ner_entities_one:
        new_ner = {"entity": []}

        for clean_medical_ner_entity_index in range(len(clean_medical_ner_entity['annotations'])):

            clean_medical_ner_entity_one = clean_medical_ner_entity['annotations'][clean_medical_ner_entity_index]
            if {clean_medical_ner_entity_one["entity"], clean_medical_ner_entity_one["label"]} not in export_labels:
                export_labels.append({clean_medical_ner_entity_one["entity"], clean_medical_ner_entity_one["label"]})
            index = start_clean(clean_medical_ner_entity_one, "反", index, clean_medical_ner_entity['text'])
            index = start_clean(clean_medical_ner_entity_one, "含", index, clean_medical_ner_entity['text'])
            new_ner["entity"].append(clean_medical_ner_entity_one)
        new_ner['id'] = clean_medical_ner_entity['id']
        new_ner['text'] = clean_medical_ner_entity['text']
        export.append(new_ner)
print(index)
json.dump(error, open("error.json", "w", encoding="utf-8"), ensure_ascii=False)

json.dump(export, open("clean_medical_ner_entities.json", "w", encoding="utf-8"), ensure_ascii=False)
# json.dump(export_labels, open("export_labels.json", "w", encoding="utf-8"), ensure_ascii=False)
