"""
08_Road_Accidents - Menu-Driven Analysis Program
Core Python only (no external libraries)
"""

DATA_FILE = "08_Road_Accidents.csv"  # update with actual filename

VALID_SEVERITIES = {"Minor", "Serious", "Fatal"}


# ---------------------------------------------------------
# DATA LOADING / CLEANING (Coding Tasks 1 & 2)
# ---------------------------------------------------------

def load_records(file):
    """
    Task 1: Read the CSV and store records as a list of dictionaries.
    Task 2: Standardize capitalization differences in accident causes.
    Returns: list of dicts (raw, not yet validated).
    """
    import csv

    records = []

    with open(file, newline="", encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:

            # Standardize cause capitalization
            row["cause"] = row["cause"].strip().title()

            # Convert numeric fields from strings to integers
            row["vehicles_involved"] = int(row["vehicles_involved"])
            row["casualties"] = int(row["casualties"])

            records.append(row)

    return records


def validate_record(record):
    """
    Task 3: Check a single record against the validation rules.
    Returns: (is_valid: bool, reasons: list[str])
    """

    reasons = []

    # Rule 1: vehicles involved must be a non-negative integer
    if record["vehicles_involved"] < 0:
        reasons.append("Vehicles involved cannot be negative")

    # Rule 2: casualties must be a non-negative integer
    if record["casualties"] < 0:
        reasons.append("Casualties cannot be negative")

    # Rule 3: severity must be Minor, Serious, or Fatal
    if record["severity"] not in VALID_SEVERITIES:
        reasons.append(
            "Severity must be Minor, Serious, or Fatal"
        )

    # Rule 4: location must be provided
    if not record["location"].strip():
        reasons.append("Location cannot be blank")

    # Rule 5: cause must be provided
    if not record["cause"].strip():
        reasons.append("Cause cannot be blank")

    # Rule 6: time period must be provided
    if not record["time_period"].strip():
        reasons.append("Time period cannot be blank")

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
    """
    Display all valid accident records in a readable format
    """
    print("\n" + "=" * 60)
    print("ACCIDENT RECORDS")
    print("=" * 60)
    
    if not valid_records:
        print("No valid records to display.")
        return
    
    for i, record in enumerate(valid_records, 1):
        print(f"\nRecord {i}:")
        print(f"  Accident ID: {record['accident_id']}")
        print(f"  Location: {record['location']}")
        print(f"  County: {record['county']}")
        print(f"  Time Period: {record['time_period']}")
        print(f"  Cause: {record['cause']}")
        print(f"  Severity: {record['severity']}")
        print(f"  Vehicles Involved: {record['vehicles_involved']}")
        print(f"  Casualties: {record['casualties']}")
        print("-" * 40)


# ---------------------------------------------------------
# MENU OPTION 2: Analyse severity
# ---------------------------------------------------------

def analyse_severity(valid_records):
    """
    Task 5 (severity part): Count accidents by severity.
    Task 9: Calculate percentage of fatal accidents.
    """
    print("\n" + "=" * 60)
    print("SEVERITY ANALYSIS")
    print("=" * 60)
    
    if not valid_records:
        print("No valid records to analyze.")
        return
    
    # Tally counts per severity
    severity_counts = {}
    for record in valid_records:
        severity = record["severity"]
        severity_counts[severity] = severity_counts.get(severity, 0) + 1
    
    total = len(valid_records)
    
    # Display results
    print(f"\nTotal accidents: {total}")
    print("\nAccidents by severity:")
    for severity, count in sorted(severity_counts.items()):
        percentage = (count / total) * 100
        print(f"  {severity}: {count} ({percentage:.1f}%)")
    
    # Task 9: Calculate percentage of fatal accidents
    fatal_count = severity_counts.get("Fatal", 0)
    fatal_percentage = (fatal_count / total) * 100 if total > 0 else 0
    print(f"\nFatal accidents: {fatal_count}")
    print(f"Percentage of fatal accidents: {fatal_percentage:.2f}%")


# ---------------------------------------------------------
# MENU OPTION 3: Analyse causes of accidents
# ---------------------------------------------------------

def analyse_causes(valid_records):
    """
    Task 5 (cause part): Count accidents by cause.
    Task 6: Identify most common cause.
    """
    print("\n" + "=" * 60)
    print("CAUSE ANALYSIS")
    print("=" * 60)
    
    if not valid_records:
        print("No valid records to analyze.")
        return
    
    # Tally counts per cause
    cause_counts = {}
    for record in valid_records:
        cause = record["cause"]
        cause_counts[cause] = cause_counts.get(cause, 0) + 1
    
    total = len(valid_records)
    
    # Display results
    print("\nAccidents by cause:")
    for cause, count in sorted(cause_counts.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total) * 100
        print(f"  {cause}: {count} ({percentage:.1f}%)")
    
    # Task 6: Find most common cause
    if cause_counts:
        most_common = max(cause_counts, key=cause_counts.get)
        print(f"\nMost common cause: {most_common}")
        print(f"Number of accidents: {cause_counts[most_common]}")


# ---------------------------------------------------------
# MENU OPTION 4: Analyse locations and time periods
# ---------------------------------------------------------

def analyse_locations_and_time(valid_records):
    """
    Task 7: Location with most accidents, location with most casualties.
    Task 8: Time period with most accidents.
    """
    print("\n" + "=" * 60)
    print("LOCATION AND TIME PERIOD ANALYSIS")
    print("=" * 60)
    
    if not valid_records:
        print("No valid records to analyze.")
        return
    
    # Tally accident count per location
    location_accidents = {}
    # Tally casualty sum per location
    location_casualties = {}
    
    for record in valid_records:
        location = record["location"]
        
        # Count accidents by location
        location_accidents[location] = location_accidents.get(location, 0) + 1
        
        # Sum casualties by location
        location_casualties[location] = location_casualties.get(location, 0) + record["casualties"]
    
    # Display location statistics
    print("\nAccidents by location:")
    for location, count in sorted(location_accidents.items(), key=lambda x: x[1], reverse=True):
        print(f"  {location}: {count} accidents")
    
    print("\nCasualties by location:")
    for location, casualties in sorted(location_casualties.items(), key=lambda x: x[1], reverse=True):
        print(f"  {location}: {casualties} casualties")
    
    # Task 7: Location with most accidents
    if location_accidents:
        most_accident_loc = max(location_accidents, key=location_accidents.get)
        print(f"\nLocation with most accidents: {most_accident_loc}")
        print(f"  {location_accidents[most_accident_loc]} accidents")
    
    # Task 7: Location with most casualties
    if location_casualties:
        most_casualty_loc = max(location_casualties, key=location_casualties.get)
        print(f"\nLocation with most casualties: {most_casualty_loc}")
        print(f"  {location_casualties[most_casualty_loc]} casualties")
    
    # Task 8: Time period with most accidents
    time_period_counts = {}
    for record in valid_records:
        period = record["time_period"]
        time_period_counts[period] = time_period_counts.get(period, 0) + 1
    
    print("\nAccidents by time period:")
    for period, count in sorted(time_period_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {period}: {count} accidents")
    
    if time_period_counts:
        max_count = max(time_period_counts.values())
        most_common_periods = [period for period, count in time_period_counts.items() if count == max_count]
        print(f"\nTime period(s) with most accidents: {', '.join(most_common_periods)}")
        print(f"  {max_count} accidents")


# ---------------------------------------------------------
# MENU OPTION 5: View invalid records
# ---------------------------------------------------------

def view_invalid_records(invalid_records):
    """
    Task 3: Display invalid records and reasons for rejection.
    """
    print("\n" + "=" * 60)
    print("INVALID RECORDS")
    print("=" * 60)
    
    if not invalid_records:
        print("All records are valid!")
        return
    
    print(f"\nTotal invalid records: {len(invalid_records)}")
    print("-" * 60)
    
    for record, reasons in invalid_records:
        print(f"\nAccident ID: {record['accident_id']}")
        print(f"  Location: {record['location']}")
        print(f"  Severity: {record['severity']}")
        print(f"  Casualties: {record['casualties']}")
        print("  Reasons for rejection:")
        for reason in reasons:
            print(f"    - {reason}")
        print("-" * 40)


# ---------------------------------------------------------
# MENU OPTION 6: View safety summary
# ---------------------------------------------------------

def view_safety_summary(valid_records):
    """
    Task 4: Total accidents and total casualties.
    """
    print("\n" + "=" * 60)
    print("SAFETY SUMMARY")
    print("=" * 60)
    
    if not valid_records:
        print("No valid records available.")
        return
    
    # Task 4: Total accidents and total casualties
    total_accidents = len(valid_records)
    total_casualties = sum(record["casualties"] for record in valid_records)

    print("\n" + "-" * 40)
    print("ACCIDENT AND CASUALTY SUMMARY")
    print("-" * 40)
    print(f"Total Accidents             : {total_accidents:,}")
    print(f"Total Casualties            : {total_casualties:,}")

    # Average casualties per accident
    average_casualties = total_casualties / total_accidents if total_accidents > 0 else 0
    print(f"Average Casualties/Accident : {average_casualties:.2f}")
    print("-" * 40)
    
    # Additional summary statistics
    print("\n" + "-" * 40)
    print("Additional Statistics:")
    
    # Average casualties per accident
    avg_casualties = total_casualties / total_accidents if total_accidents > 0 else 0
    print(f"  Average casualties per accident: {avg_casualties:.2f}")
    
    # Severity breakdown
    severity_counts = {}
    for record in valid_records:
        severity = record["severity"]
        severity_counts[severity] = severity_counts.get(severity, 0) + 1
    
    print("  Severity breakdown:")
    for severity, count in sorted(severity_counts.items()):
        percentage = (count / total_accidents) * 100
        print(f"    {severity}: {count} ({percentage:.1f}%)")
    
    # Fatal percentage
    fatal_count = severity_counts.get("Fatal", 0)
    fatal_percentage = (fatal_count / total_accidents) * 100
    print(f"  Fatal accident rate: {fatal_percentage:.1f}%")
    
    # Most common cause
    cause_counts = {}
    for record in valid_records:
        cause = record["cause"]
        cause_counts[cause] = cause_counts.get(cause, 0) + 1
    
    if cause_counts:
        most_common_cause = max(cause_counts, key=cause_counts.get)
        print(f"  Most common cause: {most_common_cause}")
        print(f"    ({cause_counts[most_common_cause]} accidents)")


# ---------------------------------------------------------
# MAIN MENU LOOP
# ---------------------------------------------------------

def main():
    """
    Main function to run the program
    """
    try:
        all_records = load_records(DATA_FILE)
    except FileNotFoundError:
        print(f"Error: File '{DATA_FILE}' not found.")
        print("Please update the DATA_FILE variable with the correct path.")
        return
    except Exception as e:
        print(f"Error loading file: {e}")
        return
    
    print(f"\nLoaded {len(all_records)} records from {DATA_FILE}")
    
    valid_records, invalid_records = split_valid_invalid(all_records)
    print(f"Valid records: {len(valid_records)}")
    print(f"Invalid records: {len(invalid_records)}")
    
    while True:
        print("\n" + "=" * 50)
        print("Road Accidents Analysis Menu")
        print("=" * 50)
        print("1. View accident records")
        print("2. Analyse severity")
        print("3. Analyse causes")
        print("4. Analyse locations and time periods")
        print("5. View invalid records")
        print("6. View safety summary")
        print("7. Exit")
        print("=" * 50)

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
            print("\nExiting program. Stay safe on the roads!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


# ---------------------------------------------------------
# SCRIPT EXECUTION
# ---------------------------------------------------------

if __name__ == "__main__":
    main()