import os

import pandas as pd

from ner_max_len import department_count, disease_count

index = 0
else_index = 0
department_entity = []
disease_entity = []
for department, count in department_count:
    if department.endswith("科"):
        print(department)
        index += 1
        print("index:", index)
        if department not in department_entity:
            department_entity.append(department)
    else:
        print(department)
        if department not in disease_entity:
            disease_entity.append(department)
        else_index += 1
        print("else_index", else_index)
for disease, count in disease_count:
    if disease.endswith("科"):
        print(disease)
        index += 1
        print("disease_diseases", index)
        if disease not in department_entity:
            department_entity.append(disease)
    else:
        if disease not in disease_entity:
            disease_entity.append(disease)

