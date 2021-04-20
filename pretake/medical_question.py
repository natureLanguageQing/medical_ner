import json

import pandas as pd
from tqdm import tqdm

from ner_max_len import ICD_10, department_entity, disease_entity

DRUG_entity = open("../entity/drug.txt", encoding="utf-8").readlines()


def index_of_str(s1, s2, label):
    """
    判断s2在s1中的开始索引与结束索引
    :param s1:
    :param s2:
    :param label:
    :return:
    """
    s2 = s2.rstrip("\n")
    dex = 0
    index = []
    lt = s1.split(s2)
    num = len(lt)
    for i in range(num - 1):
        dex += len(lt[i])
        index.append([dex, len(s2) + dex, s2, label])
        dex += len(s2)
    return index


ner_label = {}


def list_ner_label(entity_message, entity_label):
    for i in entity_message:

        if len(i[0]) > 2:
            ner_label[i[0]] = entity_label


list_ner_label(ICD_10, "ICD_10")
list_ner_label(disease_entity, "disease_entity")
list_ner_label(department_entity, "department_entity")


def list_ner_file_label(entity_message, entity_label):
    for i in entity_message:
        i = i.replace("\n", "")
        if len(i.strip()) > 2:
            ner_label[i] = entity_label


list_ner_file_label(DRUG_entity, "DRUG_entity")


def label_append_max(labels, label):
    """
    新增实体进行验证
    :param labels:实体集合
    :param label: 当前实体
    :return:
    """
    if isinstance(label, int):
        return
    if len(labels) == 0:
        labels.extend(label)
        return

    elif len(labels) > 0:
        label = label[0]

        for in_label in range(len(labels)):
            if isinstance(label, list):
                if labels[in_label][0] < label[0] < labels[in_label][1] and \
                        label[1] - label[0] > labels[in_label][1] - labels[in_label][0]:
                    labels[in_label] = label


def medical_ner(export_path):
    fp = open(export_path, 'w', newline='', encoding='utf-8')

    if isinstance(medical_questions, list):

        for medical_question in tqdm(medical_questions):
            if isinstance(medical_question, list):

                for medical_message in medical_question:
                    if isinstance(medical_message, str):

                        medical_message = medical_message.strip()
                        medical_message = medical_message.replace("\n", "")
                        medical_message = medical_message.replace("\r", "")
                        medical_message = medical_message.replace(" ", "")
                    else:
                        continue
                    label_index_list = []
                    for i, j in ner_label.items():
                        if i in medical_message:
                            label_index = index_of_str(medical_message, i, j)
                            if len(label_index) >= 1:
                                label_append_max(label_index_list, label_index)

                    if len(label_index_list) > 2 and len(medical_message) > 10:
                        entity_dict_label = {"text": medical_message, "labels": label_index_list}
                        entity_dict_label = json.dumps(entity_dict_label, ensure_ascii=False)
                        fp.write(entity_dict_label + "\n")


if __name__ == '__main__':
    medical_questions = pd.read_csv("../medical_question/all_data.csv").drop_duplicates().values.tolist()

    medical_ner('question_entity_2021.json')
