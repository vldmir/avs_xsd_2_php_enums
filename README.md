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
   
   <?xml version="1.0" encoding="UTF-8"?>
```
<xs:schema xmlns:avs="http://ddex.net/xml/avs/avs"
           xmlns:xs="http://www.w3.org/2001/XMLSchema"
           targetNamespace="http://ddex.net/xml/avs/avs"
           elementFormDefault="unqualified"
           attributeFormDefault="unqualified">
   <xs:annotation>
      <xs:documentation>© 2006-2015 Digital Data Exchange, LLC (DDEX)</xs:documentation>
   </xs:annotation>
   <xs:annotation>
      <xs:documentation>This XML Schema Definition file is, together with all DDEX standards, subject to two licences: If you wish to evaluate whether the standard meets your needs please have a look at the Evaluation Licence at https://kb.ddex.net/display/HBK/Evaluation+Licence+for+DDEX+Standards. If you want to implement and use this DDEX standard, please take out an Implementation Licence. For details please go to http://ddex.net/apply-ddex-implementation-licence.</xs:documentation>
   </xs:annotation>
   <xs:simpleType name="AccessLimitation">
      <xs:annotation>
         <xs:documentation source="ddex:Definition">A Type of limitation on the access of a site.</xs:documentation>
      </xs:annotation>
      <xs:restriction base="xs:string">
         <xs:enumeration value="NoLimitation">
            <xs:annotation>
               <xs:documentation source="ddex:Definition">Unlimited access.</xs:documentation>
            </xs:annotation>
         </xs:enumeration>
         <xs:enumeration value="PrivateAccessOnly">
            <xs:annotation>
               <xs:documentation source="ddex:Definition">Restricted access.</xs:documentation>
            </xs:annotation>
         </xs:enumeration>
      </xs:restriction>
   </xs:simpleType>
   ...
```

3. **Run the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the script using Python:

     ```bash
     python xsd_avs_to_php_enum.py
     ```

4. **Input Required Details:**
   - When prompted, enter the full path to your XSD file.
   - Enter the namespace URI used in the XSD file.

5. **Generated PHP Enums:**
   - The script will create a directory named `export` with a subdirectory labeled with the current date and time, suffixed with `_enums`.
   - Inside this subdirectory, you'll find the generated PHP enum classes.

## Output Structure

*  export/
* └── YYYYMMDD_HHMMSS_enums/ 
* ├─── EnumClass1.php
* ├─── EnumClass2.php
* └─── ...

Each PHP file corresponds to a simple type enumeration defined in the provided XSD file and includes the specified PHP namespace at the top.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/vldmir/avs_xsd_2_php_enums/issues).

## License

[MIT](https://choosealicense.com/licenses/mit/)