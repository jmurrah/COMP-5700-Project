from datasets import load_dataset


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
    filtered_table.to_csv("generated_csv_files/task1.csv", index=False)
