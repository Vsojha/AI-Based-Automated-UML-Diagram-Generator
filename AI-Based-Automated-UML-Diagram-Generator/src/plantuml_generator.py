def generate_plantuml(classes, attributes, methods, relationships):
    uml = "@startuml\n\n"

    for cls in classes:
        uml += f"class {cls} {{\n"

        if cls in attributes:
            for attr in attributes[cls]:
                uml += f"  -{attr}\n"

        if cls in methods:
            for method in methods[cls]:
                uml += f"  +{method}()\n"

        uml += "}\n\n"

    for rel in relationships:
        uml += f"{rel[0]} --> {rel[1]}\n"

    uml += "\n@enduml"
    return uml