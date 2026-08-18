"""
08_Road_Accidents - Menu-Driven Analysis Program
Core Python only (no external libraries)
"""

DATA_FILE = "08_Road_Accidents.csv"  # update with actual filename

VALID_SEVERITIES = {"Minor", "Serious", "Fatal"}


# ---------------------------------------------------------
# DATA LOADING / CLEANING (Coding Tasks 1 & 2)
# ---------------------------------------------------------

def load_records(filename):
    """
    Task 1: Read the CSV and store records as a list of dictionaries.
    Task 2: Standardize capitalization differences in accident causes.
    Returns: list of dicts (raw, not yet validated).
    """
    records = []
    # TODO: open file, read with csv.DictReader
    # TODO: for each row, standardize row["cause"] casing (e.g. .strip().title())
    # TODO: append cleaned row (dict) to records
    return records


def validate_record(record):
    """
    Task 3: Check a single record against the validation rules.
    Returns: (is_valid: bool, reasons: list[str])
    """
    reasons = []

    # Rule 1: vehicles and casualties must be non-negative integers
    # TODO: check record["vehicles"], record["casualties"]

    # Rule 2: severity must be Minor, Serious, or Fatal
    # TODO: check record["severity"] in VALID_SEVERITIES

    # Rule 3: location, cause, time period must be provided (not blank)
    # TODO: check record["location"], record["cause"], record["time_period"]

    is_valid = len(reasons) == 0
    return is_valid, reasons


def split_valid_invalid(records):
    """
    Runs validate_record() over all records.
    Returns: (valid_records, invalid_records_with_reasons)
    invalid_records_with_reasons is a list of (record, reasons) tuples.
    """
    valid_records = []
    invalid_records = []

    for record in records:
        is_valid, reasons = validate_record(record)
        if is_valid:
            valid_records.append(record)
        else:
            invalid_records.append((record, reasons))

    return valid_records, invalid_records


# ---------------------------------------------------------
# MENU OPTION 1: View accident records
# ---------------------------------------------------------

def view_accident_records(valid_records):
    # TODO: print each record in a readable format
    pass


# ---------------------------------------------------------
# MENU OPTION 2: Analyse severity
# ---------------------------------------------------------

def analyse_severity(valid_records):
    """
    Task 5 (severity part): Count accidents by severity.
    Task 9: Calculate percentage of fatal accidents.
    """
    # TODO: tally counts per severity (Minor / Serious / Fatal)
    # TODO: fatal_percentage = (fatal_count / total) * 100
    pass


# ---------------------------------------------------------
# MENU OPTION 3: Analyse causes
# ---------------------------------------------------------

def analyse_causes(valid_records):
    """
    Task 5 (cause part): Count accidents by cause.
    Task 6: Identify most common cause.
    """
    # TODO: tally counts per cause
    # TODO: find cause with max count
    pass


# ---------------------------------------------------------
# MENU OPTION 4: Analyse locations and time periods
# ---------------------------------------------------------

def analyse_locations_and_time(valid_records):
    """
    Task 7: Location with most accidents, location with most casualties.
    Task 8: Time period with most accidents.
    """
    # TODO: tally accident count per location
    # TODO: tally casualty sum per location
    # TODO: tally accident count per time period
    pass


# ---------------------------------------------------------
# MENU OPTION 5: View invalid records
# ---------------------------------------------------------

def view_invalid_records(invalid_records):
    """
    Task 3: Display invalid records and reasons for rejection.
    """
    # TODO: loop through invalid_records, print record + reasons
    pass



# MENU OPTION 6: View safety summary

def view_safety_summary(valid_records):
    """
    Task 4: Total accidents and total casualties.
    """
    # TODO: total_accidents = len(valid_records)
    # TODO: total_casualties = sum(...)
    pass



# MAIN MENU LOOP


all_records = load_records(DATA_FILE)
valid_records, invalid_records = split_valid_invalid(all_records)

while True:
    print("\nRoad Accidents Analysis Menu")
    print("1. View accident records")
    print("2. Analyse severity")
    print("3. Analyse causes")
    print("4. Analyse locations and time periods")
    print("5. View invalid records")
    print("6. View safety summary")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ").strip()

    if choice == "1":
        view_accident_records(valid_records)
    elif choice == "2":
        analyse_severity(valid_records)
    elif choice == "3":
        analyse_causes(valid_records)
    elif choice == "4":
        analyse_locations_and_time(valid_records)
    elif choice == "5":
        view_invalid_records(invalid_records)
    elif choice == "6":
        view_safety_summary(valid_records)
    elif choice == "7":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")



 
