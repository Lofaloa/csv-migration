# csv-migration
Simple command line tool that migrate one csv schema to another.

## About
This tool first objective is to help me clean data that was extracted from the different banking applications I am using. The idea is to unify the different schemas so that I can import them in a Google Sheet file.

## Features
You specify a source CSV file with a set of rules and the utility should produce the expected target CSV file.

## Stuff I should pay attention to
- Input file validation 🛡
    - Schema validation. Has the file the expected columns? Do we want the input file to strictly contain the expected columns? What if a column does not exist? 
    - Data validation: has the data the expected format or data type? Is a value optional?
    - Validation error handling: log it? ignore it? abort? fix it?

- Mapping
    - Map a column to another
    - Ignore columns?
    - Create new columns with computed value

- Filtering
    - Exclude rows with some values
    - Exclude rows with values outside of a range 

- Formatting
    - Should the column data be reformatted?
    - Is data correctly formatted?

- Implementation
    - Command line interface
    - JavaScript, TypeScript, Python?
    - Libraries?
