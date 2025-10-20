from datasets import load_dataset


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
    filtered_table.to_csv("generated_csv_files/task3.csv", index=False)
