import pandas as pd

medical_dicts_drop_duplicates = pd.read_csv("../match_machine/question_entity_label.json", sep=" ",
                                            encoding="utf-8").drop_duplicates()
print(medical_dicts_drop_duplicates.head())
