import csv
import os
import pandas as pd
from tqdm import tqdm

path = "../medical_question_answer"
medical_question_answers = os.listdir(path)
index = 1
entity_dict = {}
exports = []
for i in medical_question_answers:
    medical_question = pd.read_csv(os.path.join(path, i)).drop_duplicates().values.tolist()
    for i in medical_question:
        export = []
        for j in i:
            if isinstance(j, str):
                export.append(j)
        exports.append(export)
pd.DataFrame(exports).drop_duplicates().to_csv('question_entity_train.csv', index=False)


def pre_take(medical_questions):
    """
    数据预处理 清洗后 去重
    :param medical_questions:
    :return:
    """
    export = []
    for medical_question in tqdm(medical_questions):
        if isinstance(medical_question, list):

            for medical_message in medical_question:
                if isinstance(medical_message, str):
                    if "https" in medical_message:
                        continue
                    medical_message = medical_message.strip()
                    medical_message = medical_message.replace("\n", "")
                    medical_message = medical_message.replace("\r", "")
                    medical_message = medical_message.replace(" ", "")
                    export.append(medical_message)
    pd.DataFrame(export).drop_duplicates().iloc[0:2000].to_csv("../medical_question/all_data_part.csv", index=False)
if __name__ == '__main__':
    pre_take(pd.read_csv("../medical_question/all_data_set.csv").drop_duplicates().values.tolist())