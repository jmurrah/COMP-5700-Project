from datasets import load_dataset


def task2():
    all_repo_table = load_dataset(
        "hao-li/AIDev", "all_repository", split="train"
    ).to_pandas()

    column_mapping = {
        "id": "REPOID",
        "language": "LANG",
        "stars": "STARS",
        "url": "REPOURL",
    }

    filtered_table = all_repo_table[list(column_mapping.keys())].rename(
        columns=column_mapping
    )
    filtered_table.to_csv("generated_csv_files/task2.csv", index=False)
