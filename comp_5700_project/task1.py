from datasets import load_dataset
from utils import clean_text


def task1():
    all_pr_table = load_dataset(
        "hao-li/AIDev", "all_pull_request", split="train"
    ).to_pandas()

    column_mapping = {
        "title": "TITLE",
        "id": "ID",
        "agent": "AGENTNAME",
        "body": "BODYSTRING",
        "repo_id": "REPOID",
        "repo_url": "REPOURL",
    }

    filtered_table = all_pr_table[list(column_mapping.keys())].rename(
        columns=column_mapping
    )

    # Clean text columns
    filtered_table["TITLE"] = filtered_table["TITLE"].apply(
        lambda x: clean_text(x) if isinstance(x, str) else x
    )
    filtered_table["AGENTNAME"] = filtered_table["AGENTNAME"].apply(
        lambda x: clean_text(x) if isinstance(x, str) else x
    )
    filtered_table["BODYSTRING"] = filtered_table["BODYSTRING"].apply(
        lambda x: clean_text(x, preserve_newlines=True) if isinstance(x, str) else x
    )
    filtered_table["REPOURL"] = filtered_table["REPOURL"].apply(
        lambda x: clean_text(x) if isinstance(x, str) else x
    )

    filtered_table.to_csv("generated_csv_files/task1.csv", index=False)
