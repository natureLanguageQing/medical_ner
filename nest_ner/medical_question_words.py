import json

import pandas as pd
from tqdm import tqdm

from ner_max_len import ICD_10, department_entity, disease_entity
from nest_ner.nest_ner_base import list_ner_file_label, list_ner_csv_label, list_ner_label, medical_one

if __name__ == '__main__':
    DRUG_entity = open("../entity/drug.txt", encoding="utf-8").readlines()
    body_entity = open("../entity/body.csv", encoding="utf-8").readlines()
    list_ner_file_label(DRUG_entity, "DRUG_entity")
    list_ner_file_label(body_entity, "body_entity")
    list_ner_csv_label("../entity/region.csv", "region")

    list_ner_label(ICD_10, "ICD_10")
    list_ner_label(disease_entity, "disease_entity")
    list_ner_label(department_entity, "department_entity")

    medical_one(
        "主动脉夹层的治疗，心胸内科，心胸外科和肿瘤科都可以治疗。使用藿香正气片和藿香正气水效果较好，")
