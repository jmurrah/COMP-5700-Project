from datasets import load_dataset
from utils import clean_text, clean_diff_text


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

    # Clean text columns
    filtered_table["PRSHA"] = filtered_table["PRSHA"].apply(
        lambda x: clean_text(x) if isinstance(x, str) else x
    )
    filtered_table["PRCOMMITMESSAGE"] = filtered_table["PRCOMMITMESSAGE"].apply(
        lambda x: clean_text(x) if isinstance(x, str) else x
    )
    filtered_table["PRFILE"] = filtered_table["PRFILE"].apply(
        lambda x: clean_text(x) if isinstance(x, str) else x
    )
    filtered_table["PRSTATUS"] = filtered_table["PRSTATUS"].apply(
        lambda x: clean_text(x) if isinstance(x, str) else x
    )
    filtered_table["PRDIFF"] = filtered_table["PRDIFF"].apply(
        lambda x: clean_diff_text(x) if isinstance(x, str) else x
    )

    filtered_table.to_csv("generated_csv_files/task4.csv", index=False)
