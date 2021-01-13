import pandas as pd

icd_message = pd.read_excel("../export/最新全国街道乡镇级以上行政区划代码表.xls").values.tolist()
icd_disease = []
for i in icd_message:
    print(i)
    print(i[2].strip())
    if i[2].strip() not in icd_disease:
        icd_disease.append(i[2].strip())
pd.DataFrame(icd_disease).to_csv("../export/region.csv", index=False)
