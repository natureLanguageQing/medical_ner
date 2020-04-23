import os

import pandas as pd

department_count = pd.read_csv(os.path.join("../export/department_count.csv")).values.tolist()
disease_count = pd.read_csv(os.path.join("../export/disease_count.csv")).values.tolist()

questions = pd.read_csv(os.path.join("../export/questions.csv")).values.tolist()

disease_entity = pd.read_csv(os.path.join("../entity/disease_entity.csv")).values.tolist()
department_entity = pd.read_csv(os.path.join("../entity/department_entity.csv")).values.tolist()
ICD_10 = pd.read_csv(os.path.join("../entity/ICD-10.csv")).values.tolist()