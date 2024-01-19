import os
import xml.etree.ElementTree as ET
from datetime import datetime

def parse_xsd_and_generate_php(file_path, php_namespace):
    # Create export and date-time directories
    export_dir = 'export'
    datetime_dir = datetime.now().strftime("%Y%m%d_%H%M%S") + '_enums'
    path = os.path.join(export_dir, datetime_dir)
    os.makedirs(path, exist_ok=True)

    # Parse the XSD file
    tree = ET.parse(file_path)
    root = tree.getroot()

    namespace = {'xs': 'http://www.w3.org/2001/XMLSchema'}

    for simpleType in root.findall('xs:simpleType', namespace):
        name = simpleType.get('name')
        php_class = generate_php_enum(name, simpleType, namespace, php_namespace)
        write_to_file(name, php_class, path)

def generate_php_enum(name, simpleType, namespace, php_namespace):
    php_code = f"<?php\n\nnamespace {php_namespace};\n\n"
    php_code += f"enum {name}: string {{\n"
    for enumeration in simpleType.findall('.//xs:enumeration', namespace):
        value = enumeration.get('value')
        documentation = enumeration.find('.//xs:documentation', namespace)
        doc_comment = f"    /**\n     * {documentation.text}\n     */\n" if documentation is not None else ""
        php_code += doc_comment + f"    case {value} = '{value}';\n"
    php_code += "}\n"
    return php_code

def write_to_file(name, php_class, path):
    file_path = os.path.join(path, f"{name}.php")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(php_class)

# Get user input for the file path and PHP namespace
xsd_file_path = input("Enter the path to the XSD file: ")
php_namespace = input("Enter the desired PHP namespace (e.g., App\\Services\\Export\\Enums): ")
parse_xsd_and_generate_php(xsd_file_path, php_namespace)
