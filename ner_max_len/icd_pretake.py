import pandas as pd

icd_message = pd.read_csv("../export/疾病诊断编码库ICD-10.csv").values.tolist()
icd_disease = []
for i in icd_message:
    print(i)
    print(i[2].strip())
    if i[2].strip() not in icd_disease:
        icd_disease.append(i[2].strip())
pd.DataFrame(icd_disease).to_csv("../export/ICD-10.csv", index=False)
