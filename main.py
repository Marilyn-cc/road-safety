"""
Group 8 - Capstone Project (DSA 8103)
Members: Christine, Emmanuel, Rehema, Marilyne, Andrew

08_Road_Accidents - Menu-Driven Analysis Program
Use Core Python only (no external libraries)

"""

DATA_FILE = "08_Road_Accidents.csv"  # We pulled the sheet "08_Road_Accidents from the 'Capstone_Dataset.xlsx' workbook and saved it
                                     #  as a CSV file for easier processing

VALID_SEVERITIES = {"Minor", "Serious", "Fatal"} # as per the question, there are only 3 valid severities


# DATA LOADING / CLEANING (Coding Tasks 1 & 2)

def load_records(file): # function to load records from CSV file
# Read the CSV and store records as a list of dictionaries.
# Standardize capitalization differences in accident causes.
# Returns: list of dicts (raw, not yet validated).

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
    Check a single record against the validation rules.
    Returns: (is_valid: bool, reasons: list[str])
    """

    reasons = []

    # check: vehicles involved must be a non-negative integer
    if record["vehicles_involved"] < 0:
        reasons.append("Vehicles involved cannot be negative")

    # Check: casualties must be a non-negative integer
    if record["casualties"] < 0:
        reasons.append("Casualties cannot be negative")

    # check: severity must be Minor, Serious, or Fatal
    if record["severity"] not in VALID_SEVERITIES:
        reasons.append(
            "Severity must be Minor, Serious, or Fatal"
        )

    # Check: location must be provided
    if not record["location"].strip():
        reasons.append("Location cannot be blank")

    # check: cause must be provided
    if not record["cause"].strip():
        reasons.append("Cause cannot be blank")

    # Check: time period must be provided
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


# Menu option 1: Function to display accident records_______________

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



# Menu option 2: Function to analyse severity

def analyse_severity(valid_records):
    """
    (severity part): Count accidents by severity.
    Calculate percentage of fatal accidents.
    """
    print("\n" + "=" * 60) # goes into a new line and puts a seperator in the output  -> ==============================
    print("SEVERITY ANALYSIS") #prints the heading of the option output               -> SEVERITY ANALYSIS
    print("=" * 60)    # puts closing a seperator in the output            -> ==============================
    
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
    total_casualties = sum(record["casualties"] for record in valid_records)
    print(f"Total casualties: {total_casualties}")
    print("\nAccidents by severity:")
    for severity, count in sorted(severity_counts.items()):
        percentage = (count / total) * 100
        print(f"  {severity}: {count} ({percentage:.1f}%)")
    
    #  Calculate percentage of fatal accidents
    fatal_count = severity_counts.get("Fatal", 0)
    fatal_percentage = (fatal_count / total) * 100 if total > 0 else 0
    print(f"\nFatal accidents: {fatal_count}")
    print(f"Percentage of fatal accidents: {fatal_percentage:.2f}%")


# Menu option 3: function to analyse causes of accidents

def analyse_causes(valid_records):
    """
      Count accidents by cause.
     Identify most common cause.
    """
    print("\n" + "=" * 60) # new line and separator in the output  -> ==============================
    print("CAUSE ANALYSIS") # prints the heading of the option output -> CAUSE ANALYSIS
    print("=" * 60) # puts closing a seperator in the output            -> ==============================
    
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
    
    #  Find most common cause
    if cause_counts:
        most_common = max(cause_counts, key=cause_counts.get)
        print(f"\nMost common cause: {most_common}")
        print(f"Number of accidents: {cause_counts[most_common]}")



# Menu option 4: Analyse locations and time periods

def analyse_locations_and_time(valid_records):
    """
     Location with most accidents, location with most casualties.
     Time period with most accidents.
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
    
    
    #  Location with most casualties #(corrected code to show multiple locations if tied)
    if location_casualties:
        max_casualties = max(location_casualties.values())

        most_casualty_locations = [
            location
            for location, casualties in location_casualties.items()
            if casualties == max_casualties
        ]

        print("\nLocation(s) with most casualties:")
        for location in most_casualty_locations:
            print(f"  {location}: {max_casualties} casualties")
    
    #  Time period with most accidents
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


# Menu option 5: View invalid records

def view_invalid_records(invalid_records):
    """
     Display invalid records and reasons for rejection.
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


# Menu option 6: View safety summary

def view_safety_summary(valid_records, invalid_records):
    """
    Display an overall safety summary containing the main findings
    from the accident records, severity, causes, locations,
    time periods and validation results.
    """

    print("\n" + "=" * 60)
    print("SAFETY SUMMARY")
    print("=" * 60)

    if not valid_records:
        print("No valid records available.")
        return

    #
    # 1. GENERAL ACCIDENT AND CASUALTY SUMMARY
    # 

    total_accidents = len(valid_records)
    total_casualties = sum(
        record["casualties"] for record in valid_records
    )


    print("\n" + "-" * 60)
    print("1. GENERAL SUMMARY")
    print("-" * 60)

    print(f"Total valid accidents       : {total_accidents}")
    print(f"Total casualties            : {total_casualties}")
    print(f"Total invalid records       : {len(invalid_records)}")


    # 
    # 2. SEVERITY ANALYSIS
    # 

    severity_counts = {}

    for record in valid_records:
        severity = record["severity"]
        severity_counts[severity] = severity_counts.get(severity, 0) + 1

    print("\n" + "-" * 60)
    print("2. SEVERITY ANALYSIS")
    print("-" * 60)

    for severity, count in sorted(severity_counts.items()):
        percentage = (count / total_accidents) * 100
        print(f"{severity}: {count} accidents ({percentage:.1f}%)")

    fatal_count = severity_counts.get("Fatal", 0)
    fatal_percentage = (fatal_count / total_accidents) * 100

    print(f"\nFatal accidents            : {fatal_count}")
    print(f"Percentage of fatal cases  : {fatal_percentage:.2f}%")


    # 
    # 3. CAUSE ANALYSIS
    # 

    cause_counts = {}

    for record in valid_records:
        cause = record["cause"]
        cause_counts[cause] = cause_counts.get(cause, 0) + 1

    print("\n" + "-" * 60)
    print("3. CAUSE ANALYSIS")
    print("-" * 60)

    for cause, count in sorted(
        cause_counts.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        percentage = (count / total_accidents) * 100
        print(f"{cause}: {count} accidents ({percentage:.1f}%)")

    if cause_counts:
        max_cause_count = max(cause_counts.values())

        most_common_causes = [
            cause
            for cause, count in cause_counts.items()
            if count == max_cause_count
        ]

        print("\nMost common cause(s):")

        for cause in most_common_causes:
            print(f"  {cause}: {max_cause_count} accidents")


    # 
    # 4. LOCATION ANALYSIS
    # 

    location_accidents = {}
    location_casualties = {}

    for record in valid_records:
        location = record["location"]

        location_accidents[location] = (
            location_accidents.get(location, 0) + 1
        )

        location_casualties[location] = (
            location_casualties.get(location, 0)
            + record["casualties"]
        )

    print("\n" + "-" * 60)
    print("4. LOCATION ANALYSIS")
    print("-" * 60)

    # Location with most accidents
    max_location_accidents = max(location_accidents.values())

    most_accident_locations = [
        location
        for location, count in location_accidents.items()
        if count == max_location_accidents
    ]

    print("\nLocation(s) with most accidents:")

    for location in most_accident_locations:
        print(f"  {location}: {max_location_accidents} accidents")

    # Location with most casualties
    max_location_casualties = max(location_casualties.values())

    most_casualty_locations = [
        location
        for location, casualties in location_casualties.items()
        if casualties == max_location_casualties
    ]

    print("\nLocation(s) with most casualties:")

    for location in most_casualty_locations:
        print(f"  {location}: {max_location_casualties} casualties")


    # 
    # 5. TIME PERIOD ANALYSIS
    # 

    time_period_counts = {}

    for record in valid_records:
        period = record["time_period"]

        time_period_counts[period] = (
            time_period_counts.get(period, 0) + 1
        )

    print("\n" + "-" * 60)
    print("5. TIME PERIOD ANALYSIS")
    print("-" * 60)

    for period, count in sorted(
        time_period_counts.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        percentage = (count / total_accidents) * 100
        print(f"{period}: {count} accidents ({percentage:.1f}%)")

    max_time_count = max(time_period_counts.values())

    busiest_periods = [
        period
        for period, count in time_period_counts.items()
        if count == max_time_count
    ]

    print("\nTime period(s) with most accidents:")

    for period in busiest_periods:
        print(f"  {period}: {max_time_count} accidents")


    # 
    # 6. INVALID RECORD SUMMARY
    # 

    print("\n" + "-" * 60)
    print("6. DATA VALIDATION SUMMARY")
    print("-" * 60)

    print(f"Valid records   : {total_accidents}")
    print(f"Invalid records : {len(invalid_records)}")

    if invalid_records:
        print("\nInvalid records identified:")

        for record, reasons in invalid_records:
            print(f"  {record['accident_id']}: ", end="")

            print("; ".join(reasons))


    # 
    # 7. OVERALL SAFETY FINDINGS
    # 

    print("\n" + "=" * 60)
    print("OVERALL SAFETY FINDINGS")
    print("=" * 60)

    print(f"\n• {total_accidents} valid accidents were analysed.")
    print(f"• A total of {total_casualties} casualties were recorded.")

    print("\n• Severity:")
    print(
        f"  Fatal accidents accounted for "
        f"{fatal_percentage:.2f}% of all valid accidents."
    )

    if cause_counts:
        print("\n• Leading cause:")
        for cause in most_common_causes:
            print(f"  {cause} ({max_cause_count} accidents)")

    print("\n• Highest-risk location by accident count:")
    for location in most_accident_locations:
        print(f"  {location} ({max_location_accidents} accidents)")

    print("\n• Location with the most casualties:")
    for location in most_casualty_locations:
        print(f"  {location} ({max_location_casualties} casualties)")

    print("\n• Busiest time period:")
    for period in busiest_periods:
        print(f"  {period} ({max_time_count} accidents)")

    print("\n" + "=" * 60)


# RUN THE MENU AND DISPLAY OPTIONS AND INPUT SECTION.

all_records = load_records(DATA_FILE)
valid_records, invalid_records = split_valid_invalid(all_records)

while True:
    print("\n" + "8" * 60) #added some formating of the title and menu options to make it more readable
    print("ROAD ACCIDENTS ANALYSIS MENU") #capitalized the title of the menu to make it distinguishable from the menu options
    print("8" * 60)#  footer of the menu options -> 888 - corresponding to group 8
    print("1. View accident records")
    print("2. Analyse severity")
    print("3. Analyse causes")
    print("4. Analyse locations and time periods") # ANDREW TASK (completed)
    print("5. View invalid records")
    print("6. View safety summary")
    print("7. Exit")
    print("8" * 60) #separate the menu options from the input section to make it more readable

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
        view_safety_summary(valid_records, invalid_records)
    elif choice == "7": # Exit the program leaving a goodbye message to the user
        print("\nExiting program. Stay safe on the roads!")
        print("Thank you for using the Road Accidents Analysis Program.")
        print("\n" + "<" *22 + "88 Goodbye! 88" + ">" *22 + "\n") #added some formatting to the goodbye message 
        break
    else:
        print(f"\n\033[31mInvalid choice '{choice}'. Please make a menu choice between 1 and 7.\033[0m") # tested. #added new line to make the error message more readable and distinguishable from input options
        # included the invalid choice in the error message to make it more informative for the user -acw
        #adjusted the error message to make it more user-friendly and informative, guiding the user to select a valid option from the menu.
        #"\n\033[31m message \033[0m" in print makes the output red in color to make it more distinguishable from the menu options and other outputs.
