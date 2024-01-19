# PHP Enum Generator from XSD AVS( Allowed Value Sets ) file 

This Python script automatically generates PHP enum classes from a given XML Schema Definition (XSD) file. It's designed to read XSD files, extract simple type definitions, and create corresponding PHP enum classes with appropriate documentation comments.

## Prerequisites

- Python 3.6 or higher
- An XSD file with simple type enumerations

## Installation

No additional installation is required, as the script uses Python's built-in libraries.

## Usage

1. **Clone or Download the Script:**
   - Clone this repository or download the script to your local machine.

2. **Prepare Your XSD File:**
   - Ensure your XSD file is accessible and note down its path.

3. **Run the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the script using Python:

     ```bash
     python xsd_to_php_enum.py
     ```

4. **Input Required Details:**
   - When prompted, enter the full path to your XSD file.
   - Enter the namespace URI used in the XSD file.

5. **Generated PHP Enums:**
   - The script will create a directory named `export` with a subdirectory labeled with the current date and time, suffixed with `_enums`.
   - Inside this subdirectory, you'll find the generated PHP enum classes.

## Output Structure

