# Testing Documentation

## 1. Testing Approach

## 2. Test Cases

### Test Case 1: Load CSV Records
    Loaded 20 records from 08_Road_Accidents.csv

### ACCIDENT RECORDS

Record 1:
  Accident ID: A001
  Location: Mombasa Road
  County: Kiambu
  Time Period: Afternoon
  Cause: Unsafe Overtaking
  Severity: Serious
  Vehicles Involved: 2
  Casualties: 1

Record 2:
  Accident ID: A002
  Location: Waiyaki Way
  County: Nakuru
  Time Period: Evening
  Cause: Pedestrian Crossing
  Severity: Fatal
  Vehicles Involved: 3
  Casualties: 2

Record 3:
  Accident ID: A003
  Location: Nakuru-Eldoret Rd
  County: Kisumu
  Time Period: Night
  Cause: Poor Visibility
  Severity: Minor
  Vehicles Involved: 4
  Casualties: 3

Record 4:
  Accident ID: A004
  Location: Kisumu-Kakamega Rd
  County: Kajiado
  Time Period: Morning
  Cause: Mechanical Failure
  Severity: Serious
  Vehicles Involved: 1
  Casualties: 4

Record 5:
  Accident ID: A005
  Location: Thika Road
  County: Nairobi
  Time Period: Afternoon
  Cause: Speeding
  Severity: Fatal
  Vehicles Involved: 2
  Casualties: 0

Record 6:
  Accident ID: A006
  Location: Mombasa Road
  County: Kiambu
  Time Period: Evening
  Cause: Unsafe Overtaking
  Severity: Minor
  Vehicles Involved: 3
  Casualties: 1

Record 7:
  Accident ID: A008
  Location: Nakuru-Eldoret Rd
  County: Kisumu
  Time Period: Morning
  Cause: Poor Visibility
  Severity: Fatal
  Vehicles Involved: 1
  Casualties: 3

Record 8:
  Accident ID: A009
  Location: Kisumu-Kakamega Rd
  County: Kajiado
  Time Period: Afternoon
  Cause: Mechanical Failure
  Severity: Minor
  Vehicles Involved: 2
  Casualties: 4

Record 9:
  Accident ID: A010
  Location: Thika Road
  County: Nairobi
  Time Period: Evening
  Cause: Speeding
  Severity: Serious
  Vehicles Involved: 3
  Casualties: 0

Record 10:
  Accident ID: A011
  Location: Mombasa Road
  County: Kiambu
  Time Period: Night
  Cause: Unsafe Overtaking
  Severity: Fatal
  Vehicles Involved: 4
  Casualties: 1

Record 11:
  Accident ID: A012
  Location: Waiyaki Way
  County: Nakuru
  Time Period: Morning
  Cause: Pedestrian Crossing
  Severity: Minor
  Vehicles Involved: 1
  Casualties: 2

Record 12:
  Accident ID: A013
  Location: Nakuru-Eldoret Rd
  County: Kisumu
  Time Period: Afternoon
  Cause: Poor Visibility
  Severity: Serious
  Vehicles Involved: 2
  Casualties: 3

Record 13:
  Accident ID: A015
  Location: Thika Road
  County: Nairobi
  Time Period: Night
  Cause: Speeding
  Severity: Minor
  Vehicles Involved: 4
  Casualties: 0

Record 14:
  Accident ID: A016
  Location: Mombasa Road
  County: Kiambu
  Time Period: Morning
  Cause: Unsafe Overtaking
  Severity: Serious
  Vehicles Involved: 1
  Casualties: 1

Record 15:
  Accident ID: A017
  Location: Waiyaki Way
  County: Nakuru
  Time Period: Afternoon
  Cause: Pedestrian Crossing
  Severity: Fatal
  Vehicles Involved: 2
  Casualties: 2

Record 16:
  Accident ID: A018
  Location: Nakuru-Eldoret Rd
  County: Kisumu
  Time Period: Evening
  Cause: Speeding
  Severity: Minor
  Vehicles Involved: 3
  Casualties: 3

Record 17:
  Accident ID: A019
  Location: Kisumu-Kakamega Rd
  County: Kajiado
  Time Period: Night
  Cause: Mechanical Failure
  Severity: Serious
  Vehicles Involved: 4
  Casualties: 4

Record 18:
  Accident ID: A020
  Location: Thika Road
  County: Nairobi
  Time Period: Morning
  Cause: Speeding
  Severity: Fatal
  Vehicles Involved: 1
  Casualties: 0

### Test Case 2: Checked for valid and invalid records
    Valid records: 18
    Invalid records: 2

### Test Case From the input Menu for all the function
Road Accidents Analysis Menu
1. View accident records
2. Analyse severity
3. Analyse causes
4. Analyse locations and time periods
5. View invalid records
6. View safety summary
7. Exit

### SEVERITY ANALYSIS


Total accidents: 18

Accidents by severity:
  Fatal: 6 (33.3%)
  Minor: 6 (33.3%)
  Serious: 6 (33.3%)

Fatal accidents: 6
Percentage of fatal accidents: 33.33%


### CAUSE ANALYSIS


Accidents by cause:
  Speeding: 5 (27.8%)
  Unsafe Overtaking: 4 (22.2%)
  Pedestrian Crossing: 3 (16.7%)
  Poor Visibility: 3 (16.7%)
  Mechanical Failure: 3 (16.7%)

Most common cause: Speeding
Number of accidents: 5


### LOCATION AND TIME PERIOD ANALYSIS


Accidents by location:
  Mombasa Road: 4 accidents
  Nakuru-Eldoret Rd: 4 accidents
  Thika Road: 4 accidents
  Waiyaki Way: 3 accidents
  Kisumu-Kakamega Rd: 3 accidents

Casualties by location:
  Nakuru-Eldoret Rd: 12 casualties
  Kisumu-Kakamega Rd: 12 casualties
  Waiyaki Way: 6 casualties
  Mombasa Road: 4 casualties
  Thika Road: 0 casualties

Location with most accidents: Mombasa Road
  4 accidents

Location with most casualties: Nakuru-Eldoret Rd
  12 casualties

Accidents by time period:
  Afternoon: 5 accidents
  Morning: 5 accidents
  Evening: 4 accidents
  Night: 4 accidents

Time period(s) with most accidents: Afternoon, Morning
  5 accidents


### INVALID RECORDS


Total invalid records: 2


Accident ID: A007
  Location: Waiyaki Way
  Severity: Serious
  Casualties: -1
  Reasons for rejection:
    - Casualties cannot be negative

Accident ID: A014
  Location: Kisumu-Kakamega Rd
  Severity: Critical
  Casualties: 4
  Reasons for rejection:
    - Severity must be Minor, Serious, or Fatal



### SAFETY SUMMARY


Total accidents: 18
Total casualties: 34


Additional Statistics:
  Average casualties per accident: 1.89
  Severity breakdown:
    Fatal: 6 (33.3%)
    Minor: 6 (33.3%)
    Serious: 6 (33.3%)
  Fatal accident rate: 33.3%
  Most common cause: Speeding
    (5 accidents)

### Checked for invalid choice 
Enter your choice (1-7): 9
Invalid choice. Please enter a number between 1 and 7.

updated the invalid choice message to be: 
Invalid choice '{choice}'. Please make a menu choice between 1 and 7."


# After Testing 
We discovered that option 4 shows only one location with most casualties when in reality there were two locations with the most casualties so we corrected the function.

### LOCATION AND TIME PERIOD ANALYSIS


Location(s) with most casualties:
  Nakuru-Eldoret Rd: 12 casualties
  Kisumu-Kakamega Rd: 12 casualties

### Severity Analysis 
Included total casualties as output

Total accidents: 18
Total casualties: 34

Accidents by severity:
  Fatal: 6 (33.3%)
  Minor: 6 (33.3%)
  Serious: 6 (33.3%)

Fatal accidents: 6
Percentage of fatal accidents: 33.33%


## 4. Conclusion

The testing of the Road Accident Records Analyser confirmed that the program performs its intended functions correctly. The system was tested for record validation, data processing, accident analysis, identification of common causes and locations, casualty calculations, severity analysis, and handling of invalid records.

The tests showed that valid accident records were processed correctly, while invalid records were identified and rejected with appropriate reasons. The analysis functions also produced the expected results from the dataset, including accident counts, casualty totals, most common causes, risky locations, and fatal accident percentages.

Overall, the Road Accident Records Analyser met the specified functional requirements and demonstrated that the program can reliably process and analyse road accident records. The testing also helped identify and correct errors during development, improving the accuracy and reliability of the final system.
