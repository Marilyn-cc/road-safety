# Project 8: Road-Accident Records Analyser

## Overview

The **Road-Accident Records Analyser** is a menu-driven Python program developed to analyse road-accident records and identify accident patterns, common causes, accident severity, risky locations, and high-risk time periods.

The program uses **Core Python only** and reads accident records from a CSV file. The records are stored as a list of dictionaries, with each dictionary representing an accident.

## Objectives

The program aims to:

* Validate road-accident records.
* Standardize capitalization differences in accident causes.
* Calculate total accidents and casualties.
* Analyse accidents by severity and cause.
* Identify the most common accident cause.
* Identify locations with the most accidents and casualties.
* Identify the time period with the most accidents.
* Calculate the percentage of fatal accidents.
* Display invalid records together with their reasons for rejection.

## Validation

The program checks that:

* Vehicles involved are non-negative integers.
* Casualties are non-negative integers.
* Severity is `Minor`, `Serious`, or `Fatal`.
* Location, cause, and time period are provided.

Invalid records are separated from valid records and displayed with the reasons for rejection.
Accident causes are standardized using capitalization formatting so that recognized capitalization differences are treated consistently.

## Menu

The program provides seven menu options:

```text
1. View accident records
2. Analyse severity
3. Analyse causes
4. Analyse locations and time periods
5. View invalid records
6. View safety summary
7. Exit
```

The menu repeats until the user selects **Exit**. Invalid menu selections display an error message.

## Analysis

The program provides the following analyses:

* **Severity:** counts accidents by Minor, Serious, and Fatal severity and calculates the fatal accident percentage.
* **Causes:** counts accidents by cause and identifies the most common cause.
* **Locations:** identifies the locations with the most accidents and casualties.
* **Time periods:** identifies the time period with the most accidents.
* **Safety summary:** displays total accidents, total casualties, severity statistics, fatal accident rate, and most common cause.

## Project Structure

```text
Project_8_Road_Accidents/
│
├── README.md
├── main.py
├── tests.md
├── .gitignore
│
└── docs/
    └── algorithm.pdf
```

* `main.py` — Main Python program.
* `README.md` — Project overview and instructions.
* `tests.md` — Completed test cases.
* `algorithm.pdf` — Pseudocode or flowchart.
* `.gitignore` — Files excluded from Git tracking.

## Requirements

* Python 3
* Core Python only
* CSV dataset: `08_Road_Accidents.csv`

## Running the Program

Place the CSV file in the project directory and ensure the filename matches the `DATA_FILE` variable in `main.py`.

Run the program from the terminal:

```bash
python main.py
```

Follow the menu prompts to perform the different analyses.

## Testing

The program is tested using normal, invalid, boundary, search, and menu-control test cases. The completed tests are documented in `tests.md`.

## Version Control

Git is used to track the progressive development of the project. The repository contains meaningful commits documenting development and the final version is tagged:

```text
v1.0
```

The commit history can be inspected using:

```bash
git log --oneline
```
