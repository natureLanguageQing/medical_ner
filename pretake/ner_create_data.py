import pandas as pd

medical_dicts_drop_duplicates = pd.read_csv("question_entity_ICD_10_train.csv",
                                            encoding="utf-8").drop_duplicates().values.tolist()
export = []

ids = 2000
with open("question_entity_ICD_10_train_words.txt",
          "w",
          encoding="utf-8") as write_file:
    for i in medical_dicts_drop_duplicates:
        for i in i:
            if isinstance(i, str) and len(i) > 15:
                if i not in export:
                    export.append(i)
    for i in export:
        write_file.writelines(i.strip())
