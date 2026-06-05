"""this module contains functions related to serialization and deserialization"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}

    for child in root:
        value = child.text

        if value == "True":
            value = True
        elif value == "False":
            value = False
        else:
            try:
                value = int(value)
            except ValueError:
                pass

        data[child.tag] = value

    return data
