from datasets import load_dataset
from utils import clean_text


def task3():
    pr_task_type_table = load_dataset(
        "hao-li/AIDev", "pr_task_type", split="train"
    ).to_pandas()

    column_mapping = {
        "id": "PRID",
        "title": "PRTITLE",
        "reason": "PRREASON",
        "type": "PRTYPE",
        "confidence": "CONFIDENCE",
    }

    filtered_table = pr_task_type_table[list(column_mapping.keys())].rename(
        columns=column_mapping
    )

    # Clean text columns
    filtered_table["PRTITLE"] = filtered_table["PRTITLE"].apply(
        lambda x: clean_text(x) if isinstance(x, str) else x
    )
    filtered_table["PRREASON"] = filtered_table["PRREASON"].apply(
        lambda x: clean_text(x) if isinstance(x, str) else x
    )
    filtered_table["PRTYPE"] = filtered_table["PRTYPE"].apply(
        lambda x: clean_text(x) if isinstance(x, str) else x
    )

    filtered_table.to_csv("generated_csv_files/task3.csv", index=False)
