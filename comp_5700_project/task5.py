import pandas as pd

SECURITY_KEYWORDS = [
    "race",
    "racy",
    "buffer",
    "overflow",
    "stack",
    "integer",
    "signedness",
    "underflow",
    "improper",
    "unauthenticated",
    "gain access",
    "permission",
    "cross site",
    "css",
    "xss",
    "denial service",
    "dos",
    "crash",
    "deadlock",
    "injection",
    "request forgery",
    "csrf",
    "xsrf",
    "forged",
    "security",
    "vulnerability",
    "vulnerable",
    "exploit",
    "attack",
    "bypass",
    "backdoor",
    "threat",
    "expose",
    "breach",
    "violate",
    "fatal",
    "blacklist",
    "overrun",
    "insecure",
]


def has_security_keyword(text):
    return any(keyword in text.lower() for keyword in SECURITY_KEYWORDS)


def task5():
    print("Starting Task 5...")
    task1_csv = pd.read_csv("generated_csv_files/task1.csv", low_memory=False)
    task2_csv = pd.read_csv(
        "generated_csv_files/task2.csv",
        low_memory=False,
    )  # NOTE: doesn't have any data needed for task5
    task3_csv = pd.read_csv("generated_csv_files/task3.csv", low_memory=False)
    task4_csv = pd.read_csv(
        "generated_csv_files/task4.csv",
        low_memory=False,
    )  # NOTE: doesn't have any data needed for task5

    merged_data = pd.merge(
        task1_csv[["ID", "AGENTNAME", "TITLE", "BODYSTRING"]],
        task3_csv[["PRID", "PRTYPE", "CONFIDENCE"]],
        left_on="ID",
        right_on="PRID",
        how="inner",
    )
    merged_data["SECURITY"] = merged_data.apply(
        lambda row: has_security_keyword(
            str(row["TITLE"]) + " " + str(row["BODYSTRING"])
        ),
        axis=1,
    ).astype(int)

    result_df = pd.DataFrame(
        {
            "ID": merged_data["ID"],
            "AGENT": merged_data["AGENTNAME"],
            "TYPE": merged_data["PRTYPE"],
            "CONFIDENCE": merged_data["CONFIDENCE"],
            "SECURITY": merged_data["SECURITY"],
        }
    )
    result_df.to_csv("generated_csv_files/task5.csv", index=False)
