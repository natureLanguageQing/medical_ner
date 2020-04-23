import os

import pandas as pd

question_entity_all_label = pd.read_csv(os.path.join("question_entity_all_label.csv")).values.tolist()

pd.DataFrame(question_entity_all_label[:200]).to_csv("question_entity_demo.csv", index=False)
