from xml.etree import ElementTree

root = ElementTree.Element("student")

first_name = ElementTree.SubElement(root, "firstName")
first_name.text = "Greg"

second_name = ElementTree.SubElement(root, "secondName")
second_name.text = "Dean"

scores = ElementTree.SubElement(root, "scores")

module1 = ElementTree.SubElement(scores, "module1")
module1.text = "100"

module2 = ElementTree.SubElement(scores, "module2")
module2.text = "80"

module3 = ElementTree.SubElement(scores, "module3")
module3.text = "90"

tree = ElementTree.ElementTree(root)
tree.write("student.xml")