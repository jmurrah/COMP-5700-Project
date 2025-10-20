# COMP-5700-Project

Course Project for COMP-5700 Secure Software Process

## Rubric

https://github.com/paser-group/continuous-secsoft/tree/master/fall25-ssp/project

## Group Members

Jacob Murrah, Cooper Jackson, JD Wilks

## Downloading Poetry

This project uses Poetry as it's dependency manager.

```
https://python-poetry.org/docs/
```

## Installation

```
poetry install
```

## Running

```
poetry run python3 comp_5700_project/main.py
```

## Output

All generated CSV files will be placed in the generated_csv_files/ folder.

- task1.csv
- task2.csv
- task3.csv
- task4.csv
- task5.csv

## Project Structure

```
COMP-5700-Project/
├── comp_5700_project/          # Source code directory
│   ├── __init__.py
│   ├── main.py                 # Main execution script
│   ├── task1.py                # Task implementation files
│   ├── task2.py
│   ├── task3.py
│   ├── task4.py
│   ├── task5.py
│   └── utils.py                # Utility functions
├── generated_csv_files/        # Output directory
│   └── README.md               # Documentation for output files
├── poetry.lock                 # Poetry dependency lock file
├── pyproject.toml              # Project configuration
└── README.md                   # This file
```
