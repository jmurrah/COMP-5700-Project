from datasets import load_dataset


def task4():
    pr_commit_details_table = load_dataset(
        "hao-li/AIDev", "pr_commit_details", split="train"
    ).to_pandas()

    column_mapping = {
        "pr_id": "PRID",
        "sha": "PRSHA",
        "message": "PRCOMMITMESSAGE",
        "filename": "PRFILE",
        "status": "PRSTATUS",
        "additions": "PRADDS",
        "deletions": "PRDELSS",
        "changes": "PRCHANGECOUNT",
        "patch": "PRDIFF",  # NOTE: remove special characters in the diff to avoid string encoding errors
    }

    filtered_table = pr_commit_details_table[list(column_mapping.keys())].rename(
        columns=column_mapping
    )
    filtered_table.to_csv("generated_csv_files/task4.csv", index=False)
